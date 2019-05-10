from argparse import ArgumentParser
from os import listdir, path
from sys import argv

from drug_bank_parser import DrugBankParser
from i2b2_parser import I2b2Parser


def main():
    parser = ArgumentParser(prog="i2b2 data parser")
    parser.add_argument("--data-dir", help="Path of directory containing i2b2 files.", required=True)
    parser.add_argument("--drug-bank-xml-path", help="Path to drug bank xml file.", required=True)
    args = parser.parse_args(argv[1:])

    drug_bank_parser = DrugBankParser(xml_path=args.drug_bank_xml_path)
    drugs_dict = drug_bank_parser.parse()
    print(drugs_dict)
    # for file_name in listdir(args.data_dir):
    #     file_path = path.join(args.data_dir, file_name)
    #     parser = I2b2Parser(file_path)
    #     print(parser.info(drugs_dict))


if __name__ == "__main__":
    main()
