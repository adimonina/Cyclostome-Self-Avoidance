#!/bin/sh

# Environment setup
GENOME_INDICES_OUTPUT_DIR="genome_indices"
RNA_FILES_DIR="ERR7132687/ERR7132687_RNA_trimmed_second.fastq,ERR7132689/ERR7132689_RNA_trimmed_second.fastq,ERR7132699/ERR7132699_RNA_trimmed_second.fastq,ERR7132707/ERR7132707_RNA_trimmed_second.fastq"
BAM_FILE_DIR="Aligned.out.bam"
SAM_FILE_DIR="Aligned.out.sam"
SORTED_BAM_DIR="Aligned.out.sorted.bam"
FILTERED_MAPPING_OUT_DIR="Aligned.out.sorted.filter.100.bam"
ERR7132687_BAM_FILE_PREFIX="./ERR7132687"
ERR7132707_BAM_FILE_PREFIX="./ERR7132707"

# Mapping
STAR --genomeDir $GENOME_INDICES_OUTPUT_DIR --readFilesIn $RNA_FILES_DIR --limitOutSJcollapsed 5000000

# Converting SAM file to BAM file - Reduce size for later
./samtools-1.20/samtools view -S -b -o $BAM_FILE_DIR $SAM_FILE_DIR

# Sorting the BAM file
./samtools-1.20/samtools sort $BAM_FILE_DIR -o $SORTED_BAM_DIR

# QualiMap - manual

# Filter mapping to improve mapping quality
./samtools-1.20/samtools view -q 200 -b $SORTED_BAM_DIR -o $FILTERED_MAPPING_OUT_DIR

# Qualimap - manual


# Mapping ERR7132687
STAR --genomeDir $GENOME_INDICES_OUTPUT_DIR --readFilesIn $RNA_FILES_DIR --limitOutSJcollapsed 5000000 --outFileNamePrefix $ERR7132687_BAM_FILE_PREFIX

# Mapping ERR7132707
STAR --genomeDir $GENOME_INDICES_OUTPUT_DIR --readFilesIn $RNA_FILES_DIR --limitOutSJcollapsed 5000000 --outFileNamePrefix $ERR7132707_BAM_FILE_PREFIX