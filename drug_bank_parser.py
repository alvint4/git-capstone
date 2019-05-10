import pickle
import xml.etree.ElementTree as Etree


class DrugBankParser:
    __xml_path__ = None

    def __init__(self, xml_path):
        self.__xml_path__ = xml_path

    def __compute_drugs_dict__(self):
        drugs = {}

        for event, element in Etree.iterparse(self.__xml_path__, events=['start', 'end']):

            if element.tag == "{http://www.drugbank.ca}drug":
                drug = {'id': [], 'pubmed-id': None}
                name = None

                for elem in element.iter():
                    # if elem.tag == '{http://www.drugbank.ca}indication':
                    #     tmp.append(elem.text)
                    if elem.tag == '{http://www.drugbank.ca}drugbank-id':
                        drug['id'].append(elem.text)
                    elif elem.tag == '{http://www.drugbank.ca}name':
                        name = elem.text
                    elif elem.tag == '{http://www.drugbank.ca}pubmed-id':

                        drug['pubmed-id'] = elem.text
                    elif elem.tag == '{http://www.drugbank.ca}indication':
                        drug['indication'] = elem.text
                    elif elem.tag == '{http://www.drugbank.ca}synonym' or elem.tag == '{http://www.drugbank.ca}synonyms':
                        drug['synonym'] = elem.text
                    elif elem.tag == '{http://www.drugbank.ca}mechanism-of-action':
                        drug['mechanism-of-action'] = elem.text
                    elif elem.tag == '{http://www.drugbank.ca}absorption':
                        drug['absorption'] = elem.text
                    elif elem.tag == '{http://www.drugbank.ca}pharmacodynamics':
                        drug['pharmacodynamics'] = elem.text
                    elif elem.tag == '{http://www.drugbank.ca}route-of-elimination}':
                        drug['route-of-elimination'] = elem.text
                if name is not None:
                    drugs[name] = drug

            element.clear()

        return drugs

    def parse(self):
        pickled_file_name = "drug_list.pkl"

        try:
            raise FileNotFoundError
            drugs = pickle.load(open(pickled_file_name, "rb"))
        except FileNotFoundError:
            drugs = self.__compute_drugs_dict__()
            pickle.dump(drugs, open(pickled_file_name, "wb"))

        return drugs
