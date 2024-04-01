# --- Theory of Automata --- #
# Project 2
# Sabrina Guilarte and Richard Rodriguez

# --> Pytest for Grammar, CLI, and CFG Implementations 

import pytest
from CFG import Grammar

def test_MATRIX_CFG1():
    general_grammar = Grammar()

    # Test constant assignments, main, and variable assignments
    matrix_str1 = general_grammar.read_string_from_file('Matrix_Sample1.txt')
    matrix_str1 = general_grammar.fix_str(matrix_str1)
    matrix_result1 = general_grammar.cyk_parse(matrix_str1, general_grammar.available_grammars['MATRIX'])
    assert matrix_result1 == True

def test_MATRIX_CFG3():
    general_grammar = Grammar()

    # Test for-loops
    matrix_str3 = general_grammar.read_string_from_file('Matrix_Sample3.txt')
    matrix_str3 = general_grammar.fix_str(matrix_str3)
    matrix_result3 = general_grammar.cyk_parse(matrix_str3, general_grammar.available_grammars['MATRIX'])
    assert matrix_result3 == True

def test_MATRIX_CFG4():
    general_grammar = Grammar()

    # Test while-loops
    matrix_str4 = general_grammar.read_string_from_file('Matrix_Sample4.txt')
    matrix_str4 = general_grammar.fix_str(matrix_str4)
    matrix_result4 = general_grammar.cyk_parse(matrix_str4, general_grammar.available_grammars['MATRIX'])
    assert matrix_result4 == True

def test_MATRIX_CFG5():
    general_grammar = Grammar()

    # Test function calls and prints
    matrix_str5 = general_grammar.read_string_from_file('Matrix_Sample5.txt')
    matrix_str5 = general_grammar.fix_str(matrix_str5)
    matrix_result5 = general_grammar.cyk_parse(matrix_str5, general_grammar.available_grammars['MATRIX'])
    assert matrix_result5 == True

def test_MATRIX_CFG6():
    general_grammar = Grammar()

    # Test if-elif-else
    matrix_str6 = general_grammar.read_string_from_file('Matrix_Sample6.txt')
    matrix_str6 = general_grammar.fix_str(matrix_str6)
    matrix_result6 = general_grammar.cyk_parse(matrix_str6, general_grammar.available_grammars['MATRIX'])
    assert matrix_result6 == True

def test_MATRIX_CFG7():
    general_grammar = Grammar()

    # Test switch-statement
    matrix_str7 = general_grammar.read_string_from_file('Matrix_Sample7.txt')
    matrix_str7 = general_grammar.fix_str(matrix_str7)
    matrix_result7 = general_grammar.cyk_parse(matrix_str7, general_grammar.available_grammars['MATRIX'])
    assert matrix_result7 == True

def test_MATRIX_CFG8():
    general_grammar = Grammar()

    # Test wrong format
    matrix_str8 = general_grammar.read_string_from_file('Matrix_Sample8.txt')
    matrix_str8 = general_grammar.fix_str(matrix_str8)
    matrix_result8 = general_grammar.cyk_parse(matrix_str8, general_grammar.available_grammars['MATRIX'])
    assert matrix_result8 == False

def test_MATRIX_CFG9():
    general_grammar = Grammar()

    # Test recursion
    matrix_str9 = general_grammar.read_string_from_file('Matrix_Sample9.txt')
    matrix_str9 = general_grammar.fix_str(matrix_str9)
    matrix_result9 = general_grammar.cyk_parse(matrix_str9, general_grammar.available_grammars['MATRIX'])
    assert matrix_result9 == True
