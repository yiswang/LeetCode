#!/usr/bin/python

###############################################################################
#
# LeetCode question 36. Valid Sudoku
#
# Difficulty: Easy
#
# Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
# 
# The Sudoku board could be partially filled, where empty cells are filled with
# the character '.'.
# 
# 
# A partially filled sudoku which is valid.
# 
# Note: A valid Sudoku board (partially filled) is not necessarily solvable.
# Only the filled cells need to be validated.
#
###############################################################################

class Solution(object):
    def check_the_ch(self, ch, num_counts):
        if ch != "." and num_counts.get(ch) == 1:
            return False
        else:
            num_counts[ch] = 1
        return True

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Check each row
        for row_list in board:
            num_counts = {}
#             print row_list
            for ch in row_list:
                if not self.check_the_ch(ch, num_counts):
                    return False
#         print "\n"

        # Check each column
        for col in xrange(0, 9): 
            num_counts = {}
            print ""
            for row in xrange(0, 9):
                ch = board[row][col]
#                 print ch,
                if not self.check_the_ch(ch, num_counts):
                    return False
#         print "\n"

        # Check each sub-box
        for row_start in xrange(0, 9, 3): 
            for col_start in xrange(0, 9, 3):
                num_counts = {}
                for row in xrange(row_start, row_start+3):
                    for col in xrange(col_start, col_start+3):
                        ch = board[row][col]
                        if not self.check_the_ch(ch, num_counts):
                            return False
#         print "\n"

        return True


if __name__ == "__main__":
    test_cases = []

#     board = [[]]
#     test_cases.append(board)

    board = [
        ["5","3",".", ".","7",".", ".",".","."],
        ["6",".",".", "1","9","5", ".",".","."],
        [".","9","8", ".","7",".", ".","6","."],
        ["8",".",".", ".","6",".", ".",".","3"],
        ["4",".",".", "8",".","3", ".",".","1"],
        ["7",".",".", ".","2",".", ".",".","6"],
        [".","6",".", ".",".",".", "2","8","."],
        [".",".",".", "4","1","9", ".",".","5"],
        [".",".",".", ".","8",".", ".","7","9"],
    ]
    test_cases.append(board)

    solu = Solution()
    for board in test_cases:
        res = solu.isValidSudoku(board)
        print res


