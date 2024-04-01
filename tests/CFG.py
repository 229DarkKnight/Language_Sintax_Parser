# --- Theory of Automata --- #
# Project 2
# Sabrina Guilarte and Richard Rodriguez

# --> Grammar Implementation

import nltk
from typing import Optional

class Grammar:    
    def __init__(self):
        self.available_grammars = {'XML': '', 'HTML': '', 'MATRIX': ''}

        Grammar.save_string_as_dict_def('XML_CFG.txt', 'XML', self.available_grammars)
        Grammar.save_string_as_dict_def('HTML_CFG.txt', 'HTML', self.available_grammars)
        Grammar.save_string_as_dict_def('MATRIX_CFG.txt', 'MATRIX', self.available_grammars)
    
    #----------------------
    
    @staticmethod
    def read_string_from_file(file_path: str) -> Optional[str]:
        try:
            with open(file_path, 'r') as file:
                string_data = file.read()
                return string_data
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            return None
    
    #----------------------

    @staticmethod
    def save_string_as_dict_def(file_path: str, key: str, dictionary: dict) -> bool:
        string_data = Grammar.read_string_from_file(file_path)
        
        if string_data:
            string_data = nltk.CFG.fromstring(string_data)
            dictionary[key] = string_data
            print(f"String from file '{file_path}' saved as definition of key '{key}' in the dictionary.")
            return True
        else:
            print("String data could not be retrieved.")
            return False
    
    #----------------------

    @staticmethod
    def fix_str(program_str: str) -> str:
        return ''.join(program_str.split()).lower()
    
    #----------------------

    @staticmethod
    def fix_str_html(program_str: str) -> str:
        inside_tag = False
        result = ''
        for char in program_str:
            if char == '<':
                inside_tag = True
            elif char == '>':
                inside_tag = False
            if ( char.isspace() or char in ('\n', '\t') ) and not inside_tag:
                continue
            result += char
        return result.lower()

    #----------------------

    @staticmethod
    def cyk_parse(string: str, grammar: str) -> bool:
        # Convert the grammar to Chomsky Normal Form
        cnf_grammar = grammar.chomsky_normal_form()

        # Treat each character in the string as a separate token
        tokens = list(string)

        # Initialize the parse table
        n = len(tokens)
        table = [[set() for _ in range(n)] for _ in range(n)]

        # Fill in the table for substrings of length 1 (i.e., individual tokens)
        for i, token in enumerate(tokens):
            for prod in cnf_grammar.productions(rhs=token):
                table[i][i].add(prod.lhs())

        # Fill in the table for substrings of length 2 to n
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                for k in range(i, j):
                    for prod in cnf_grammar.productions():
                        if len(prod.rhs()) == 2:
                            B, C = prod.rhs()
                            if B in table[i][k] and C in table[k + 1][j]:
                                table[i][j].add(prod.lhs())

        # Check if the start symbol of the grammar is in the top-right cell of the table
        return cnf_grammar.start() in table[0][n - 1]
