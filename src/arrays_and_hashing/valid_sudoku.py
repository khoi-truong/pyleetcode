"""
Problem: Valid Sudoku
Leetcode: https://leetcode.com/problems/valid-sudoku/
"""

from abc import ABC, abstractmethod

# TODO: Add bitmask solution


class ValidSudokuSolution(ABC):
    """
    Abstract class for Valid Sudoku
    """

    @abstractmethod
    def is_valid_sudoku(self, board: list[list[str]]) -> bool:
        pass


class ValidSudokuHashSet(ValidSudokuSolution):
    """
    Solution: Hash set
    """

    def is_valid_sudoku(self, board: list[list[str]]) -> bool:
        seen_in_column = [set[str]() for _ in range(9)]
        seen_in_row = [set[str]() for _ in range(9)]
        seen_in_square = [set[str]() for _ in range(9)]

        for row in range(9):
            for column in range(9):
                element = board[row][column]
                if element == ".":
                    continue
                square_index = (row // 3) * 3 + (column // 3)
                seen = (
                    element in seen_in_row[row]
                    or element in seen_in_column[column]
                    or element in seen_in_square[square_index]
                )
                if seen:
                    return False
                seen_in_column[column].add(element)
                seen_in_row[row].add(element)
                seen_in_square[square_index].add(element)
        return True
