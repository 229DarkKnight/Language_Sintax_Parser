# --- Theory of Automata --- #
# Project 2
# Sabrina Guilarte and Richard Rodriguez

# --> CLI Implementation

from CFG import Grammar

class CLI:
    @staticmethod
    def run(general_grammar: Grammar) -> bool:
        flag = False
        automaton = None

        print("Welcome to our CFG Parser!")
        print("Type 'help' at any time for a list of the available commands.")

        while True:
            print('')
            user_input = input("CFG Parser> ").strip().lower()
            print('')

            if user_input == 'help':
                print("Available Commands:")
                print("  - xml: Test if a given .txt file complies with the XML syntax")
                print("  - html: Test if a given .txt file complies with the HTML syntax")
                print("  - matrix: Test if a given .txt file complies with the syntax of our own language, inspired by the Matrix movies")
                print("  - exit: Leave the program")
                continue

            elif user_input in ('xml', 'html', 'matrix'):
                file_path = input("Enter the path to the .txt file: ")
                print('Analyzing file...')
                result = CLI.check_str(file_path, user_input.upper(), general_grammar) #-----------------------
                if result:
                    print('Accepted! The given string follows', user_input, 'grammar.')
                elif type(result) is type(None):
                    continue
                else:
                    print('Rejected. The given string does not follow', user_input, 'grammar.')

            elif user_input == 'exit':
                print("Thank you for using our CFG Parser. Goodbye!")
                break

            else:
                print("Unknown command. Type 'help' for a list of commands.")

    @staticmethod
    def check_str(file_path: str, chosen_CFG: str, general_grammar: Grammar) -> bool:
        string = general_grammar.read_string_from_file(file_path)
        if type(string) is type(None):
            return string

        if chosen_CFG == 'HTML':
            string = general_grammar.fix_str_html(string)
        else:
            string = general_grammar.fix_str(string)
        
        result = general_grammar.cyk_parse(string, general_grammar.available_grammars[chosen_CFG])
        return result


# --------------------------------------------------------
if __name__ == "__main__": # without this pytest crashed
    general_grammar = Grammar()
    CLI.run(general_grammar)
