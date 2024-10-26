import os
import pandas as pd

# Directory containing the CSV files
dir_path = 'output_non_overlapping'


def is_overlapping(pos_brain, end_brain, reads_brain, pos_heart):
    if end_brain < pos_heart or end_heart < pos_brain:  # no overlap
        return False
    return True


# Get list of all files in the directory
all_files = os.listdir(dir_path)

# Separate files into two groups based on their prefixes
files_2687 = [f for f in all_files if f.startswith('ERR7132687')]
files_2707 = [f for f in all_files if f.startswith('ERR7132707')]

# Create a dictionary for quick lookup of files in ERR7132707
file_2707_dict = {f.split('_')[1].replace('.csv', ''): f for f in files_2707}

# Iterate over files in ERR7132687
for file_2687 in files_2687:
    rname = file_2687.split('_')[1].replace('.csv', '')
    print(f"Processing Rname: {rname}")
    file_2687_path = os.path.join(dir_path, file_2687)

    # Load the ERR7132687 file
    df_2687_sorted = pd.read_csv(file_2687_path).sort_values(by='pos')

    # Check if there is a matching file in ERR7132707
    if rname in file_2707_dict:
        file_2707_path = os.path.join(dir_path, file_2707_dict[rname])

        # Load the ERR7132707 file
        df_2707_sorted = pd.read_csv(file_2707_path).sort_values(by='pos')

        output_rows = []
        for index, row_brain in df_2687_sorted.iterrows():
            print(f"Checking in ERR7132687_{rname} row: {index}/{df_2687_sorted.shape[0]}")
            pos_brain = row_brain['pos']
            end_brain = row_brain['end']
            reads_brain = row_brain['readsNum']
            is_overlap_with_heart = False

            for index, row_heart in df_2707_sorted.iterrows():
                pos_heart = row_heart['pos']
                end_heart = row_heart['end']
                reads_heart = row_heart['readsNum']
                if end_brain < pos_heart:
                    break
                if is_overlapping(pos_brain, end_brain, reads_brain, pos_heart):
                    is_overlap_with_heart = True
                    output_rows.append(row_brain.tolist()[0:3] + [reads_brain, reads_heart, reads_brain / reads_heart
                                                                  ])
                    break
            if not is_overlap_with_heart:
                output_rows.append(row_brain.tolist()[0:3] + [reads_brain, 0, reads_brain
                                                              ])
        # Create a DataFrame for the output
        output_df = pd.DataFrame(output_rows, columns=['rname', 'pos', 'end', 'readsBrain', 'readsHeart',
                                                       'brain/heart'])

    else:
        # If no matching file in ERR7132707, keep all rows
        output_df = df_2687_sorted
        output_df.rename(
            columns={'rname': 'rname', 'pos': 'pos', 'end': 'end', 'readsNum': 'readsBrain'}, inplace=True)
        output_df['readsHeart'] = 0
        output_df['brain/heart'] = output_df['readsBrain']

    # Save the result to a new CSV file
    output_file_path = os.path.join('../../part2/DGE/step3- Analysis/4/output_reads_ratio_per_contig', f'ERR7132687_{rname}.csv')
    output_df.to_csv(output_file_path, index=False)

print("Non-overlapping rows extraction completed.")
