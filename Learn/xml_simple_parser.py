'''Simple XML parser using ElementTree package'''

import xml.etree.ElementTree as ET
from pathlib import Path

class XMLUtility:
    """This class reads/write xml content of different files"""

    def __init__(self, xml_file_name):
        """Initialze the root element class and use the data in other places"""
        #This class doesn't need init, since it is static class and method.
        #self.tree = ET.parse(xml_file_name)
        #self.root_elem = self.tree.getroot()
        #pass

    @staticmethod
    def search_tag(tag_name_to_search, xml_file_name):
        """Search a specific tag node inside all the xml file and return list"""
        tree = ET.parse(xml_file_name)
        root_elem = tree.getroot()
        tag_value_list = []
        for search_item in root_elem.iter(tag_name_to_search):
            tag_value_list.append(search_item.text)
        return tag_value_list

    @staticmethod
    def remove_xml_node(node_name_to_remove, file_name):
        """Remove a specific xml node with the given inputs
           it remove the first node it found, not the entire tags in xml"""
        tree = ET.parse(file_name)
        root_elem = tree.getroot()
        for child in root_elem:
            if child.tag == node_name_to_remove:
                root_elem.remove(child)
            cn_find = child.find(node_name_to_remove)
            if cn_find is None:
                continue
            child.remove(cn_find)
        tree.write(file_name, 'UTF-8', True)


    @staticmethod
    def create_xml_file(root_node_name, dict_values, file_name):
        """Create a new xml file with the given inputs"""
        root_node = ET.Element(root_node_name)
        for dict_key, dict_val in dict_values.items():
            dict_item = ET.SubElement(root_node, dict_key)
            #dict_item.set("order", index)
            #index += 1
            if isinstance(dict_val, dict):
                for grand_dict_key, grand_dict_val in dict_val.items():
                    grand_dict_item = ET.SubElement(dict_item, grand_dict_key)
                    if not isinstance(grand_dict_val, dict):
                        grand_dict_item.text = grand_dict_val
            else:
                dict_item.text = dict_val
        ET.dump(root_node)
        tree = ET.ElementTree(root_node)
        tree.write(file_name, 'UTF-8', True)

    @staticmethod
    def print_all_content(xml_file_name):
        """print all the contents of XML file with tag and attribute"""
        tree = ET.parse(xml_file_name)
        root_elem = tree.getroot()
        for child in root_elem:
            print("Tag: {0} \tText: {1} \tAttributes: {2}". \
                  format(child.tag, child.text, child.attrib))
            for grand_child in child:
                print("Tag: {0} \tText: {1} \tAttributes: {2}". \
                      format(grand_child.tag, grand_child.text, grand_child.attrib))

if __name__ == "__main__":
    try:
        OUTPUT_FILE = input("Enter output file path where XML to be saved:")
        XML_DICT = {"book1":{"author":"Pandi", "title":"1stBook", "YOP":"2020"},\
           "book2":{"author":"Rajan", "title":"2ndBook", "YOP":"2021"}}
        XMLUtility.create_xml_file("books", XML_DICT, OUTPUT_FILE)

        XMLUtility.remove_xml_node("author", OUTPUT_FILE)
        XMLUtility.remove_xml_node("book2", OUTPUT_FILE)

        INPUT_FILE = input("Enter XML File path: ")
        FILE_PATH = Path(INPUT_FILE)
        if FILE_PATH.exists() and FILE_PATH.is_file():
            XMLUtility.print_all_content(INPUT_FILE)
            SEARCH_TAG = input("Enter tag to search: ")
            print("Following are the values of search item :{0}".format(SEARCH_TAG))
            for item in XMLUtility.search_tag(SEARCH_TAG, INPUT_FILE):
                print(item)
    except ValueError as ex:
        print("Exceptions on Value {0}".format(str(ex)))
    except Exception as ex:#pylint: disable=broad-except
        print("Unknown exception {0}".format(str(ex)))
