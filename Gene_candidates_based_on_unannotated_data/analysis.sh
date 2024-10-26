#!/bin/sh

# Environment setup
ERR7132687_BAM_FILE="./ERR7132687_Aligned.out.bam"
ERR7132687_CSV="ERR7132687.csv"
ERR7132707_BAM_FILE="./ERR7132707_Aligned.out.bam"
ERR7132707_CSV="ERR7132707.csv"

# Convert BAM files to CSV for later analysis
Rscript bam_to_CSV.R $ERR7132687_BAM_FILE $ERR7132687_CSV
Rscript bam_to_CSV.R $ERR7132707_BAM_FILE $ERR7132707_CSV

python split_by_rname.py $ERR7132687_CSV $ERR7132707_CSV

python rnames_mapping_analysis.py

python brain_heart_ratio.py

python rnames_analysis_graph
