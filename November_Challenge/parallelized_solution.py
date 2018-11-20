import string
import itertools as it
from multiprocessing import Pool
import time


def format_string(string):
    """Format string to normalize spaces."""
    operators = ['+', '-', '*', '/', '=', '(', ')']
    string = string.replace(' ', '')

    for operator in operators:
        string = string.replace(operator, " " + operator + " ")

    string = string.replace('*  *', '**')
    string = string.replace('^', '**')

    return string.lower()


class Solver():
    def __init__(self, char_set, lead_chars, string):
        self.char_set = char_set
        self.lead_chars = lead_chars
        self.string = string

    def __call__(self, nums):
        return self.solve_case(nums)

    def solve_case(self, nums):
        char_dict = dict(zip(self.char_set, nums))

        if '0' not in [char_dict[x] for x in self.lead_chars]:
            expression = self.string

            for key in char_dict:
                expression = expression.replace(key, char_dict[key])

            LHS, RHS = expression.split('=')

            try:
                if eval(LHS) == eval(RHS):
                    return expression
            except (ArithmeticError, SyntaxError):
                pass


def gen_puzzle_solutions(input_string):
    """Solves symbolic puzzles for all basize math operations."""
    string = format_string(input_string)

    lead_chars = set(x[0] for x in string.split() if x.isalpha())
    char_set = set(x for x in string if x.isalpha())

    if len(char_set) > 10:
        print("Invalid input string, too many distinct letters.")
        raise StopIteration

    agents = 5
    chunksize = 3
    with Pool(processes=agents) as pool:
        result = pool.map(Solver(char_set, lead_chars, string), list(it.permutations('0123456789', len(char_set))), chunksize)

    for solution in result:
        if solution is not None:
            yield solution


def main():
    print(*gen_puzzle_solutions('SEND + MORE = MONEY'), sep='\n')
    print(*gen_puzzle_solutions('SEND + MORE = MONEY'), sep='\n')
    print(*gen_puzzle_solutions('SEND + MORE = MONEY'), sep='\n')


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- {} seconds ---".format(time.time() - start_time))

test_cases = [
        'SEND + MORE = MONEY',
        'VIOLIN * 2 + VIOLA = TRIO + SONATA',
        'SEND + A + TAD + MORE = MONEY',
        'ZEROES + ONES = BINARY',
        'DCLIZ + DLXVI = MCCXXV',
        'COUPLE + COUPLE = QUARTET',
        'FISH + N + CHIPS = SUPPER',
        'SATURN + URANUS + NEPTUNE + PLUTO = PLANETS',
        'EARTH + AIR + FIRE + WATER = NATURE',
        ('AN + ACCELERATING + INFERENTIAL + ENGINEERING + TALE + ' +
            'ELITE + GRANT + FEE + ET + CETERA = ARTIFICIAL + INTELLIGENCE'),
        'TWO * TWO = SQUARE',
        'HIP * HIP = HURRAY',
        'PI * R ** 2 = AREA',
        'NORTH / SOUTH = EAST / WEST',
        'NAUGHT ** 2 = ZERO ** 3',
        'I + THINK + IT + BE + THINE = INDEED',
        'DO + YOU + FEEL = LUCKY',
        'NOW + WE + KNOW + THE = TRUTH',
        'SORRY + TO + BE + A + PARTY = POOPER',
        'SORRY + TO + BUST + YOUR = BUBBLE',
        'STEEL + BELTED = RADIALS',
        'ABRA + CADABRA + ABRA + CADABRA = HOUDINI',
        'I + GUESS + THE + TRUTH = HURTS',
        'LETS + CUT + TO + THE = CHASE',
        'THATS + THE + THEORY = ANYWAY',
        '1/(2*X-Y) = 1',
    ]

