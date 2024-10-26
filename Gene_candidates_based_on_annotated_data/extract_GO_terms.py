import re
import sys


def main():
    file_path = sys.argv[1]
    GOAccession = ""
    with open(file_path, 'r') as file:
        for line in file:
            line_arr = re.split(r"\t+", line)
            GOAccession += line_arr[3]
            GOAccession += "\n"

    output_file_path = "../../part1/ensemble/extract_go_accession/dscamGoAccession.txt"
    with open(output_file_path, 'a') as file:
        file.write(GOAccession)


main()
