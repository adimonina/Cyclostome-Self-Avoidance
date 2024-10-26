from biomart import BiomartServer
import re
import sys


def search_by_go(go_term):
    print(f"Downloading: {go_term}")
    filters = {
        'filters': {
            "biotype": "protein_coding",
            "transcript_biotype": "protein_coding",
            "with_tmhmm": "only",
            "go_parent_term": [go_term]
        }
    }
    response = ensembl.search(filters)
    return response.text


def write_output(go_accession, response):
    print(f"Writing output of: {go_accession}")
    with open(f'results/{go_accession.replace(":", "_")}.txt', 'a') as file:
        file.write(response)


def add_to_summary(go_accession, go_name, lines_count, index):
    print(f"Adding to summary: {go_accession}, {go_name}")
    with open('../../part1/ensemble/ensembel_filter/results/summary.txt', 'a') as file:
        file.write(f'{index} ---> {go_accession}\t{go_name}\t{lines_count}\n')


server = BiomartServer("http://www.ensembl.org/biomart")
ensembl_dataset = "pmarinus_gene_ensembl"
ensembl = server.datasets[ensembl_dataset]

input_file = sys.argv[1]

go_accession = []
go_names = []
with open(f'{input_file}', 'r') as file:
    for line in file:
        line_arr = re.split(r"\t+", line)
        if line_arr[4] not in go_accession:
            go_accession.append(line_arr[4])
            go_names.append(line_arr[0])

for i in range(len(go_accession)):
    print(f"{i} ---> Searching {go_accession[i]}")
    response = search_by_go(go_accession[i])
    lines_count = response.count("\n")
    write_output(go_accession[i], response)
    add_to_summary(go_accession[i], go_names[i], lines_count, i)
