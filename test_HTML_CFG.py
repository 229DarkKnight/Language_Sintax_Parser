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

def test_HTML_CFG9():
    general_grammar = Grammar()

    # Test <div>
    html_str9 = general_grammar.read_string_from_file('HTML_Sample9.txt')
    html_str9 = general_grammar.fix_str_html(html_str9)
    html_result9 = general_grammar.cyk_parse(html_str9, general_grammar.available_grammars['HTML'])
    assert html_result9 == True

def test_HTML_CFG10():
    general_grammar = Grammar()

    # Test <br>
    html_str10 = general_grammar.read_string_from_file('HTML_Sample10.txt')
    html_str10 = general_grammar.fix_str_html(html_str10)
    html_result10 = general_grammar.cyk_parse(html_str10, general_grammar.available_grammars['HTML'])
    assert html_result10 == True

def test_HTML_CFG11():
    general_grammar = Grammar()

    # Test <strong>
    html_str11 = general_grammar.read_string_from_file('HTML_Sample11.txt')
    html_str11 = general_grammar.fix_str_html(html_str11)
    html_result11 = general_grammar.cyk_parse(html_str11, general_grammar.available_grammars['HTML'])
    assert html_result11 == True

def test_HTML_CFG12():
    general_grammar = Grammar()

    # Test <span>
    html_str12 = general_grammar.read_string_from_file('HTML_Sample12.txt')
    html_str12 = general_grammar.fix_str_html(html_str12)
    html_result12 = general_grammar.cyk_parse(html_str12, general_grammar.available_grammars['HTML'])
    assert html_result12 == True

def test_HTML_CFG13():
    general_grammar = Grammar()

    # Test <em>
    html_str13 = general_grammar.read_string_from_file('HTML_Sample13.txt')
    html_str13 = general_grammar.fix_str_html(html_str13)
    html_result13 = general_grammar.cyk_parse(html_str13, general_grammar.available_grammars['HTML'])
    assert html_result13 == True

def test_HTML_CFG14():
    general_grammar = Grammar()

    # Test <hr>
    html_str14 = general_grammar.read_string_from_file('HTML_Sample14.txt')
    html_str14 = general_grammar.fix_str_html(html_str14)
    html_result14 = general_grammar.cyk_parse(html_str14, general_grammar.available_grammars['HTML'])
    assert html_result14 == True

def test_HTML_CFG15():
    general_grammar = Grammar()

    # Test <form> and <input>
    html_str15 = general_grammar.read_string_from_file('HTML_Sample15.txt')
    html_str15 = general_grammar.fix_str_html(html_str15)
    html_result15 = general_grammar.cyk_parse(html_str15, general_grammar.available_grammars['HTML'])
    assert html_result15 == True

def test_HTML_CFG16():
    general_grammar = Grammar()

    # Test <textarea>
    html_str16 = general_grammar.read_string_from_file('HTML_Sample16.txt')
    html_str16 = general_grammar.fix_str_html(html_str16)
    html_result16 = general_grammar.cyk_parse(html_str16, general_grammar.available_grammars['HTML'])
    assert html_result16 == True
