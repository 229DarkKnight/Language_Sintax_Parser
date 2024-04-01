# --- Theory of Automata --- #
# Project 2
# Sabrina Guilarte and Richard Rodriguez

# --> Pytest for HTML CFG Implementation 

import pytest
from CFG import Grammar

def test_HTML_CFG1():
    general_grammar = Grammar()

    # Test body, heading, and paragraph
    html_str1 = general_grammar.read_string_from_file('HTML_Sample1.txt')
    html_str1 = general_grammar.fix_str_html(html_str1)
    html_result1 = general_grammar.cyk_parse(html_str1, general_grammar.available_grammars['HTML'])
    assert html_result1 == True

def test_HTML_CFG2():
    general_grammar = Grammar()

    # Test image
    html_str2 = general_grammar.read_string_from_file('HTML_Sample2.txt')
    html_str2 = general_grammar.fix_str_html(html_str2)
    html_result2 = general_grammar.cyk_parse(html_str2, general_grammar.available_grammars['HTML'])
    assert html_result2 == True

def test_HTML_CFG3():
    general_grammar = Grammar()

    # Test unordered list
    html_str3 = general_grammar.read_string_from_file('HTML_Sample3.txt')
    html_str3 = general_grammar.fix_str_html(html_str3)
    html_result3 = general_grammar.cyk_parse(html_str3, general_grammar.available_grammars['HTML'])
    assert html_result3 == True

def test_HTML_CFG4():
    general_grammar = Grammar()

    # Test ordered list
    html_str4 = general_grammar.read_string_from_file('HTML_Sample4.txt')
    html_str4 = general_grammar.fix_str_html(html_str4)
    html_result4 = general_grammar.cyk_parse(html_str4, general_grammar.available_grammars['HTML'])
    assert html_result4 == True

def test_HTML_CFG5():
    general_grammar = Grammar()

    # Test link
    html_str5 = general_grammar.read_string_from_file('HTML_Sample5.txt')
    html_str5 = general_grammar.fix_str_html(html_str5)
    html_result5 = general_grammar.cyk_parse(html_str5, general_grammar.available_grammars['HTML'])
    assert html_result5 == True

def test_HTML_CFG6():
    general_grammar = Grammar()

    # Test head and title
    html_str6 = general_grammar.read_string_from_file('HTML_Sample6.txt')
    html_str6 = general_grammar.fix_str_html(html_str6)
    html_result6 = general_grammar.cyk_parse(html_str6, general_grammar.available_grammars['HTML'])
    assert html_result6 == True

def test_HTML_CFG7():
    general_grammar = Grammar()

    # Test line breaks
    html_str7 = general_grammar.read_string_from_file('HTML_Sample7.txt')
    html_str7 = general_grammar.fix_str_html(html_str7)
    html_result7 = general_grammar.cyk_parse(html_str7, general_grammar.available_grammars['HTML'])
    assert html_result7 == True

def test_HTML_CFG8():
    general_grammar = Grammar()

    # Test wrong format
    html_str8 = general_grammar.read_string_from_file('HTML_Sample8.txt')
    html_str8 = general_grammar.fix_str_html(html_str8)
    html_result8 = general_grammar.cyk_parse(html_str8, general_grammar.available_grammars['HTML'])
    assert html_result8 == False
