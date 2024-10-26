#!/bin/sh

# Environment setup
ANNOTATION_FILE="dscamAnnotation.txt"

# extract GO_terms_list
python extract_GO_terms.py $ANNOTATION_FILE

# for each GO, extract gene list related to GO term
python download_genes_related_for_GO.py $ANNOTATION_FILE
