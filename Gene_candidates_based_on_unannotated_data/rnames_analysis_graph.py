import os
import pandas as pd
import matplotlib.pyplot as plt

# Define the path to the folder containing the files
folder_path = 'output_reads_ratio_per_contig'

# Initialize an empty list to store individual DataFrames
dataframe = []

# Loop over all files in the specified folder
for filename in os.listdir(folder_path):
    print(filename)
    # Construct the full file path
    file_path = os.path.join(folder_path, filename)

    # Check if it's a file (and not a directory)
    if os.path.isfile(file_path):
        # Read the file into a DataFrame (assuming they are CSV files)
        df = pd.read_csv(file_path)

        # Append the DataFrame to the list
        dataframe.append(df)

# Concatenate all DataFrames into a single DataFrame
merged_df = pd.concat(dataframe, ignore_index=True)

only_brain_reads = merged_df[merged_df['readsHeart'] <= 0]
overlap_reads = merged_df[merged_df['readsHeart'] > 0]

merged_df.to_csv('merged_output_reads_ratio_per_contig.csv', index=False)
only_brain_reads.to_csv('only_brain_output_reads_ratio_per_contig.csv', index=False)
overlap_reads.to_csv('overlap_output_reads_ratio_per_contig.csv', index=False)

only_brain_reads = pd.read_csv('../../part2/DGE/step3- Analysis/5/only_brain_output_reads_ratio_per_contig.csv')
overlap_reads = pd.read_csv('../../part2/DGE/step3- Analysis/5/overlap_output_reads_ratio_per_contig.csv')

filtered_rows = only_brain_reads[only_brain_reads['brain/heart'] > 2800]
print(filtered_rows)

brain_min = only_brain_reads['brain/heart'].min()
brain_max = only_brain_reads['brain/heart'].max()

only_brain_reads.hist('brain/heart', range=[brain_min, brain_max], bins=100) #range 1
plt.title('Distribution of #reads in Brain that appear only in brain')
plt.xlabel('#reads only in the brain')
plt.ylabel('log #posistions')
plt.yscale("log")
plt.savefig('brainOnly_AllRange.png')

only_brain_reads.hist('brain/heart', range=[2800, brain_max], bins=100) #range 2
plt.title('Distribution of #reads in Brain that appear only in brain')
plt.xlabel('#reads only in the brain')
plt.ylabel('#posistions')
plt.savefig('brainOnly_UpperRange.png')

only_brain_reads.hist('brain/heart', range=[brain_min, 2800], bins=100) #range 3
plt.title('Distribution of #reads in Brain that appear only in brain')
plt.xlabel('#reads only in the brain')
plt.ylabel('log #posistions')
plt.yscale("log")
plt.savefig('brainOnly_LowerRange.png')

########################################################################################

overlap_max = overlap_reads['brain/heart'].max()
overlap_min = overlap_reads['brain/heart'].min()

overlap_reads.hist(column='brain/heart', bins=100, range=[10000,overlap_max]) #range1
plt.title('Distribution of (#reads in Brain)/(#reads in Heart)')
plt.xlabel('#reads in the brain/heart')
plt.ylabel('#posistions')
plt.savefig('overlap_AllRange.png') #range1

overlap_reads.hist(column='brain/heart', bins=100, range=[20000,overlap_max]) #range2
plt.title('Distribution of (#reads in Brain)/(#reads in Heart)')
plt.xlabel('#reads in the brain/heart')
plt.ylabel('#posistions')
plt.savefig('overlap_UpperRange.png') #range2



