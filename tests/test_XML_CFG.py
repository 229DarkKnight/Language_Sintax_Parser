# --- Theory of Automata --- #
# Project 2
# Sabrina Guilarte and Richard Rodriguez

# --> Pytest for XML CFG Implementation 

import pytest
from CFG import Grammar

def test_XML_CFG1():
    general_grammar = Grammar()

    # Test random tags and content
    xml_str1 = general_grammar.read_string_from_file('XML_Sample1.txt')
    xml_str1 = general_grammar.fix_str(xml_str1)
    xml_result1 = general_grammar.cyk_parse(xml_str1, general_grammar.available_grammars['XML'])
    assert xml_result1 == True

def test_XML_CFG2():
    general_grammar = Grammar()

    # Test "note" xml
    xml_str2 = general_grammar.read_string_from_file('XML_Sample2.txt')
    xml_str2 = general_grammar.fix_str(xml_str2)
    xml_result2 = general_grammar.cyk_parse(xml_str2, general_grammar.available_grammars['XML'])
    assert xml_result2 == True

def test_XML_CFG3():
    general_grammar = Grammar()

    # Test "menu" xml
    xml_str3 = general_grammar.read_string_from_file('XML_Sample3.txt')
    xml_str3 = general_grammar.fix_str(xml_str3)
    xml_result3 = general_grammar.cyk_parse(xml_str3, general_grammar.available_grammars['XML'])
    assert xml_result3 == True

def test_XML_CFG4():
    general_grammar = Grammar()

    # Test wrong format
    xml_str4 = general_grammar.read_string_from_file('XML_Sample4.txt')
    xml_str4 = general_grammar.fix_str(xml_str4)
    xml_result4 = general_grammar.cyk_parse(xml_str4, general_grammar.available_grammars['XML'])
    assert xml_result4 == False
