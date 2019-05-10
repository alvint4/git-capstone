import re
import xml.etree.ElementTree as Etree


class I2b2Parser:
    __file_path__ = None

    def __init__(self, file_path):
        self.__file_path__ = file_path

    def info(self, drugs_dict):
        tree = Etree.parse(self.__file_path__)
        root = tree.getroot()
        content = root[0].text

        info = {'drugs': []}
        add_drug = info['drugs'].extend

        pattern = re.compile(".*?(\(?\d{4}\D{0,3}\d{2}\D{0,3}\d{2}).*?", re.S)
        if pattern.findall(content) != []:
            record_date = pattern.findall(content)[0]
        else:
            record_date = []
        info["Record_date"] = record_date
        pattern = re.compile(".*?(\(?\d{3}\D{0,3}\d{3}\D{0,3}\d{4}).*?", re.S)
        phone = pattern.findall(content)
        info["Phone number"] = phone
        pattern = re.compile(".*?(\(?\d+\s[A-z]+\s[A-z]+).*?", re.S)
        address = pattern.findall(content)
        if address:
            address = address[0]
        info["Address"] = address
        pattern = re.compile(".*?(\(?\d{5}\D{0,5}).*?", re.S)
        zipcode = pattern.findall(content)
        if zipcode:
            zipcode = zipcode[0].split(" ")[0]
        info["Zip code"] = zipcode

        dosage_markers = ["qd", "mg", "tid", "qam", "units", "qpm"]

        for line in content.split('\n\n'):
            line_lower = line.lower()
            matched_marker = [marker for marker in dosage_markers if marker in line_lower]
            if matched_marker:
                words = [word for word in line.split() if word in drugs_dict]
                if words:
                    add_drug(words)

        return info
