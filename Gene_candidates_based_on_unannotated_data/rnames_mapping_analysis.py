import csv
import pandas as pd
import os


def remove_overlapping_rows(input_file, output_file):
    df = pd.read_csv(input_file)

    df_sorted = df.sort_values(by='pos')

    rows_lst = []

    row_to_add = df_sorted.iloc[0].to_list()

    max_end = df_sorted.iloc[0]['pos'] + df_sorted.iloc[0]['qwidth']

    count = 0
    total_count = 0
    for index, row in df_sorted.iterrows():

        total_count+=1
        current_pos = row['pos']
        current_end = current_pos + row['qwidth']
        is_not_last = total_count != df_sorted.shape[0]

        if current_pos < max_end:
            count += 1
            if current_end > max_end:
                max_end = current_end
            if is_not_last:
                continue
            else:
                row_to_add = row_to_add[0:2] + [max_end] + [max(1, count)]
                rows_lst.append(row_to_add)
        else:
            row_to_add = row_to_add[0:2] + [max_end] + [max(1, count)]
            rows_lst.append(row_to_add)
            row_to_add = row.to_list()
            max_end = row['pos'] + row['qwidth']
            count = 1
            if not is_not_last:
                row_to_add = row_to_add[0:2] + [max_end] + [max(1, count)]
                rows_lst.append(row_to_add)

    output_df = pd.DataFrame(rows_lst, columns=['rname', 'pos', 'end', 'readsNum'])
    output_df.to_csv(output_file, index=False)


def remove_overlapping_rows_for_all_files(input_dir, output_dir):
    i = 0
    for filename in os.listdir(input_dir):
        print(filename)
        file_path = os.path.join(input_dir, filename)
        output_filename = filename.split('.')
        output_filename = output_filename[0] + '_without_overlap.csv'
        output_file = os.path.join(output_dir, output_filename)
        remove_overlapping_rows(file_path, output_file)
        i += 1


def main():
    remove_overlapping_rows_for_all_files('rnames_csv', '../../part2/DGE/step3- Analysis/3/output_non_overlapping')


main()
