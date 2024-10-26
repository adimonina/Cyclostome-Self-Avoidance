import pandas as pd
import os
import sys


def create_df_per_rname(file_path):

    df = pd.read_csv(file_path)

    base_name = os.path.splitext(os.path.basename(file_path))[0]
    i = 0

    for rname, group in df.groupby('rname'):
        rname_df = group

        output_file = f"rnames_csv/{base_name}_{rname}.csv"

        rname_df.to_csv(output_file, index=False)

        print(f"--{i}-- Created file: {output_file}")
        i+=1


ERR7132687_csv_path = sys.argv[1]
ERR7132707_csv_path = sys.argv[2]

create_df_per_rname(ERR7132687_csv_path)
create_df_per_rname(ERR7132707_csv_path)
