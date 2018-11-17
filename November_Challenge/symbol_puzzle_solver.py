import string
import itertools as it


def format_string(string):
    """Format string to normalize spaces."""
    operators = ['+', '-', '*', '/', '=', '(', ')']
    string = string.replace(' ', '')

    for operator in operators:
        string = string.replace(operator, " " + operator + " ")

    string = string.replace('*  *', '**')
    string = string.replace('^', '**')

    return string.lower()


def gen_puzzle_solutions(input_string):
    """Solves symbolic puzzles for all basize math operations."""
    string = format_string(input_string)

    lead_chars = set(x[0] for x in string.split() if x.isalpha())
    char_set = set(x for x in string if x.isalpha())

    if len(char_set) > 10:
        print("Invalid input string, too many distinct letters.")
        raise StopIteration

    for nums in it.permutations('0123456789', len(char_set)):
        char_dict = dict(zip(char_set, nums))

        if '0' not in [char_dict[x] for x in lead_chars]:
            expression = string

            for key in char_dict:
                expression = expression.replace(key, char_dict[key])

            LHS, RHS = expression.split('=')

            try:
                if eval(LHS) == eval(RHS):
                    yield expression
            except (ArithmeticError, SyntaxError):
                pass


def main():
    print(*gen_puzzle_solutions('SEND + MORE = MONEY'), sep='\n')


if __name__ == '__main__':
    main()