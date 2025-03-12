# func_py_xml_to_dict.py
import xml.etree.ElementTree as ET

def func_py_xml_to_dict(xml_string):
    def xml_to_dict(element):
        return {element.tag: {child.tag: xml_to_dict(child) if child else child.text for child in element}}

    root = ET.fromstring(xml_string)
    return xml_to_dict(root)

xml_data = """<root><user><name>Alice</name><age>30</age></user></root>"""
print(func_py_xml_to_dict(xml_data))
