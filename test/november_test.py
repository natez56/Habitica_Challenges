""" Author: Lumral
    Date: 11/20/ 2018
    Description: Test cases for symbol_puzzle_solver.py.
    How to Run:
    1) pip install -U pytest
    2) Navigate to inside the test directory and type the command
       pytest.
    3) Alternatively you can test specific functions using the command:
       pytest -k "TestPuzzleSolver and test_gen_puzzle_solutions" or
       pytest -k "TestPuzzleSolver and test_format_string"
"""

import pytest
from context import symbol_puzzle_solver as sp
import collections as col

# Arithmetic test case solutions found at:
# http://bach.istc.kobe-u.ac.jp/llp/crypt.html

# Other solutions verified against results from:
# https://www.dcode.fr/cryptarithm-solver


class TestPuzzleSolver():
    """Tests both format_string and gen_puzzle_solutions functions."""
    def test_gen_puzzle_solutions(self):
        """Test generalized solution of arithmetic puzzle solver."""
        test_list = [
            # Arithmetic tests.
            "SEND + MORE = MONEY",
            "TRE + CINQUE + CINQUE = TREDICI",
            "a+B=c",

            # Subtraction tests.
            "ADG - BC = C",

            # Multiplication tests.
            "ad * bc = CBB",

            # Division tests.
            "add / bc = c",

            # Exponentiation tests.
            "a ** c = cd",

            # Parenthesis mixed case.
            "(ab + b) * ac / d = dc",

            # No solution.
            "A + B = AB"
        ]

        solution_list = [
            # Addition solutions.
            ["9567 + 1085 = 10652"],
            ["184 + 923054 + 923054 = 1846292"],
            ["8 + 1 = 9", "7 + 2 = 9", "7 + 1 = 8", "6 + 3 = 9", "6 + 2 = 8",
             "6 + 1 = 7", "5 + 4 = 9", "5 + 3 = 8", "5 + 2 = 7", "5 + 1 = 6",
             "4 + 5 = 9", "4 + 3 = 7", "4 + 2 = 6", "4 + 1 = 5", "3 + 6 = 9",
             "3 + 5 = 8", "3 + 4 = 7", "3 + 2 = 5", "3 + 1 = 4", "2 + 7 = 9",
             "2 + 6 = 8", "2 + 5 = 7", "2 + 4 = 6", "2 + 3 = 5", "2 + 1 = 3",
             "1 + 8 = 9", "1 + 7 = 8", "1 + 6 = 7", "1 + 5 = 6", "1 + 4 = 5",
             "1 + 3 = 4", "1 + 2 = 3"],

            # Subtraction solutions.
            ["102 - 96 = 6", "104 - 97 = 7", "106 - 98 = 8"],

            # Multiplication solutions.
            ["14 * 23 = 322", "14 * 69 = 966"],

            # Division solutions.
            ["144 / 72 = 2", "399 / 57 = 7", "544 / 68 = 8"],

            # Exponentiation solutions.
            ["2 ** 6 = 64"],

            # Parenthesis and multiple different operators case.
            ["( 13 + 3 ) * 10 / 4 = 40", "( 18 + 8 ) * 15 / 6 = 65",
             "( 26 + 6 ) * 20 / 8 = 80"],

            # No solution
            []
        ]

        for i, test in enumerate(test_list):
            assert (col.Counter(list(sp.gen_puzzle_solutions(test))) ==
                    col.Counter(solution_list[i]))

    def test_format_string(self):
        """Tests to make sure input string formatting is correct."""
        test_list = [
            # Addition format.
            "A+B=C",
            "A+b=C",

            # Subtraction.
            "al  -  bt = cv",

            # Multiplication.
            "Dv * cd * v6 = LL",

            # Division.
            "1/ER=CD",

            # Exponentiation.
            "LS **CD=BG",
            "LS^CD=5",

            # Brackets.
            "(SEND + MORE  ) +MON = MONEY",
        ]

        solution_list = [
            "a + b = c",
            "a + b = c",
            "al - bt = cv",
            "dv * cd * v6 = ll",
            "1 / er = cd",
            "ls ** cd = bg",
            "ls ** cd = 5",
            "( send + more ) + mon = money",
        ]

        for i, test in enumerate(test_list):
            assert sp.format_string(test) == solution_list[i]
