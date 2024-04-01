# --- Theory of Automata --- #
# Project 2
# Sabrina Guilarte and Richard Rodriguez

# --> Pytest for Grammar and CLI Implementation

from CFG import Grammar
from CLI import CLI

import pytest

def test_init_grammar():
    general_grammar = Grammar()

    #check for correct keys in available_grammars dictionary
    assert general_grammar.available_grammars.get('XML') is not None
    assert general_grammar.available_grammars.get('HTML') is not None
    assert general_grammar.available_grammars.get('MATRIX') is not None

    #check that definitions in available_grammars dictionary are no longer empty strings
    assert  general_grammar.available_grammars['XML'] != ''
    assert  general_grammar.available_grammars['HTML'] != ''
    assert  general_grammar.available_grammars['MATRIX'] != ''

def test_read_string_from_file():

    assert Grammar.read_string_from_file('XML_CFG.txt') is not None
    assert Grammar.read_string_from_file('HTML_CFG.txt') is not None
    assert Grammar.read_string_from_file('MATRIX_CFG.txt') is not None
    assert Grammar.read_string_from_file('a.txt') is None

def test_save_string_as_dict_def():

    general_grammar = Grammar()
    assert Grammar.save_string_as_dict_def('XML_CFG.txt', 'XML', general_grammar.available_grammars) == True
    assert Grammar.save_string_as_dict_def('HTML_CFG.txt', 'HTML', general_grammar.available_grammars) == True
    assert Grammar.save_string_as_dict_def('MATRIX_CFG.txt', 'MATRIX', general_grammar.available_grammars) == True
    assert Grammar.save_string_as_dict_def('a.txt', 'b', general_grammar.available_grammars) == False

def test_check_str():
    general_grammar = Grammar()
    assert CLI.check_str('XML_Sample1.txt', 'XML', general_grammar) is not None
    assert CLI.check_str('HTML_Sample1.txt', 'HTML', general_grammar) is not None
    assert CLI.check_str('Matrix_Sample1.txt', 'MATRIX', general_grammar) is not None
    assert CLI.check_str('a.txt', 'b', general_grammar) is None
