import pytest
import numpy as np
from BackTrack import checkList, checkAllRow, checkAllColumn, checkSquare

valid_sudoku = np.array([
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
])

# Duplicate 7 in row 9
invalid_row_sudoku = np.array([
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 7]  
])

# Duplicate 5 in column 9
invalid_col_sudoku = np.array([
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 5]  
])

# Duplicate 8 in bottom-right square
invalid_square_sudoku = np.array([
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 8]  
])

def test_checkList_complete():
    # complete ones
    complete_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result, remaining = checkList(complete_list)
    assert result is True
    assert remaining == []
    # incomplete ones
    incomplete_list = [1, 2, 3, 4, 5, 6, 7, 8, 8]  # Missing 9, duplicate 8
    result, remaining = checkList(incomplete_list)
    assert result is False
    assert sorted(remaining) == [9]
    # checkList duplicates
    duplicate_list = [1, 2, 3, 4, 5, 6, 7, 8, 8]  # Duplicate 8
    result, remaining = checkList(duplicate_list)
    assert result is False
    assert 9 in remaining  # 9 is missing because of the duplicate
    # checkList empty
    result, remaining = checkList([])
    assert result is False
    assert sorted(remaining) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_checkAllRow():
    assert checkAllRow(valid_sudoku) is True
    assert checkAllRow(invalid_row_sudoku) is False

def test_checkAllColumn():
    assert checkAllColumn(valid_sudoku) is True
    assert checkAllColumn(invalid_col_sudoku) is False

def test_checkSquare():
    assert checkSquare(valid_sudoku) is True
    assert checkSquare(invalid_square_sudoku) is False