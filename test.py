import pytest
import numpy as np
from BackTrack import checkList, checkAllRow, checkAllColumn, checkSquare

valid_sudoku = np.array([
    [3, 1, 6, 5, 7, 8, 4, 9, 2],
    [5, 2, 9, 1, 3, 4, 7, 6, 8],
    [4, 8, 7, 6, 2, 9, 5, 3, 1],
    [2, 6, 3, 4, 1, 5, 9, 8, 7],
    [9, 7, 4, 8, 6, 3, 1, 2, 5],
    [8, 5, 1, 7, 9, 2, 6, 4, 3],
    [1, 3, 8, 9, 4, 7, 2, 5, 6],
    [6, 9, 2, 3, 5, 1, 8, 7, 4],
    [7, 4, 5, 2, 8, 6, 3, 1, 9]
])

# Duplicate 3 in row 2
invalid_row_sudoku = np.array([
    [3, 1, 6, 5, 7, 8, 4, 9, 2],
    [5, 2, 9, 1, 3, 3, 7, 6, 8],
    [4, 8, 7, 6, 2, 9, 5, 3, 1],
    [2, 6, 3, 4, 1, 5, 9, 8, 7],
    [9, 7, 4, 8, 6, 3, 1, 2, 5],
    [8, 5, 1, 7, 9, 2, 6, 4, 3],
    [1, 3, 8, 9, 4, 7, 2, 5, 6], 
    [6, 9, 2, 3, 5, 1, 8, 7, 4],
    [7, 4, 5, 2, 8, 6, 3, 1, 9] 
])

# Duplicate 4 in column 8
invalid_col_sudoku = np.array([
    [3, 1, 6, 5, 7, 8, 4, 9, 2],
    [5, 2, 9, 1, 3, 4, 7, 6, 8],
    [4, 8, 7, 6, 2, 9, 5, 3, 1],
    [2, 6, 3, 4, 1, 5, 9, 8, 7],
    [9, 7, 4, 8, 6, 3, 1, 2, 5],
    [8, 5, 1, 7, 9, 2, 6, 4, 3],
    [1, 3, 8, 9, 4, 7, 2, 4, 6],
    [6, 9, 2, 3, 5, 1, 8, 7, 4],
    [7, 4, 5, 2, 8, 6, 3, 1, 9] 
])

# Duplicate 1 in bottom-right square
invalid_square_sudoku = np.array([
    [3, 1, 6, 5, 7, 8, 4, 9, 2],
    [5, 2, 9, 1, 3, 4, 7, 6, 8],
    [4, 8, 7, 6, 2, 9, 5, 3, 1],
    [2, 6, 3, 4, 1, 5, 9, 8, 7],
    [9, 7, 4, 8, 6, 3, 1, 2, 5],
    [8, 5, 1, 7, 9, 2, 6, 4, 3],
    [1, 3, 8, 9, 4, 7, 2, 5, 6],
    [6, 9, 2, 3, 5, 1, 8, 1, 4],
    [7, 4, 5, 2, 8, 6, 3, 1, 9]  
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