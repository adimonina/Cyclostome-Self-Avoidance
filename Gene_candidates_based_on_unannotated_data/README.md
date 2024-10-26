# Final project - Finding Lamprey's self avoideance of brain neuron gene related

Adi Monina

Tel-Aviv University

# Introduction



# Setup

## Download data
Download DNA sequence from Ensembl: [**Lamprey genome**](https://www.ensembl.org/Petromyzon_marinus/Info/Index)

Download 4 RNA sequence from ENA:  

<u>**heart, juvenile, female**</u> - [**SAMEA10418721**](https://www.ebi.ac.uk/ena/browser/view/SAMEA10418721) , [**SAMEA10418729**](https://www.ebi.ac.uk/ena/browser/view/SAMEA10418729)

<u>**brain, juvenile, female**</u> - [**SAMEA10418709**](https://www.ebi.ac.uk/ena/browser/view/SAMEA10418709) , [**SAMEA10418711**](https://www.ebi.ac.uk/ena/browser/view/SAMEA10418711)


## Installations
Download quast for DNA quality check in this [**link**](https://quast.sourceforge.net/docs/manual.html#sec1)

Download fastQC for RNA quality check in this [**link**](https://www.bioinformatics.babraham.ac.uk/projects/download.html#fastqc)

Download Trimmomatic for improving RNA quality in this [**link**](https://github.com/usadellab/Trimmomatic?tab=readme-ov-file#installation)

Download STAR for mapping in this [**link**](https://github.com/alexdobin/STAR?tab=readme-ov-file#compiling-from-sourcemapping)

Download QualiMap for mapping quality check in this [**link**](http://qualimap.conesalab.org/doc_html/intro.html#installation)

## Clone this repository
`git clone <GIT_URL>`

# Running
To run to whole pipeline, run the 3 scripts in the following order:
```console
./data.sh
./mapping.sh
./analysis.sh
```

# Results
overlap all range
![img_1.png](../../part2/img_1.png)

only brain all range 
![img_3.png](../../part2/img_3.png)