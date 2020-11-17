import unittest

from xo import *

class TestXAndOFunction(unittest.TestCase):
    def setUp(self):
        self.board3by3 = [-1, -1, -1, -1, 0, -1, 1, 1, 1]
        self.board4by4 = [-1, -1, -1, -1, 0, 0, 0, 0, 1, 1, 0, 0, -1, 1, 0, -1]

    def test_empty_board(self):
        self.assertEqual(getEmptyBoard(3), [-1] * 9)
        self.assertEqual(getEmptyBoard(4), [-1] * 16)
        self.assertEqual(getEmptyBoard(5), [-1] * 25)

    def test_next_player(self):
        self.assertEqual(getNextPlayer(0), 1)
        self.assertEqual(getNextPlayer(1), 0)

    def test_get_index(self):
        self.assertEqual(getIndex(3, 1, 1), 0)
        self.assertEqual(getIndex(3, 1, 2), 1)
        self.assertEqual(getIndex(3, 1, 3), 2)
        self.assertEqual(getIndex(3, 2, 1), 3)
        self.assertEqual(getIndex(3, 2, 2), 4)
        self.assertEqual(getIndex(3, 2, 3), 5)
        self.assertEqual(getIndex(3, 3, 1), 6)
        self.assertEqual(getIndex(3, 3, 2), 7)
        self.assertEqual(getIndex(3, 3, 3), 8)        
        self.assertEqual(getIndex(4, 1, 1), 0)
        self.assertEqual(getIndex(4, 1, 2), 1)
        self.assertEqual(getIndex(4, 2, 1), 4)
        self.assertEqual(getIndex(4, 4, 1), 12)
        self.assertEqual(getIndex(4, 4, 4), 15)
        self.assertEqual(getIndex(5, 1, 1), 0)
        self.assertEqual(getIndex(5, 5, 5), 24)

    def test_player_view(self):
        self.assertEqual(getPlayerView(0), 'x')
        self.assertEqual(getPlayerView(1), 'o')
        self.assertEqual(getPlayerView(-1), ' ')

    def test_extract_row(self):
        self.assertEqual(extractRow(self.board3by3, 3, 1), self.board3by3[:3])
        self.assertEqual(extractRow(self.board3by3, 3, 2), self.board3by3[3:6])
        self.assertEqual(extractRow(self.board3by3, 3, 3), self.board3by3[6:])
        self.assertEqual(extractRow(self.board4by4, 4, 1), self.board4by4[:4])
        self.assertEqual(extractRow(self.board4by4, 4, 2), self.board4by4[4:8])
        self.assertEqual(extractRow(self.board4by4, 4, 3), self.board4by4[8:12])
        self.assertEqual(extractRow(self.board4by4, 4, 4), self.board4by4[12:])

    def test_extract_col(self):
        self.assertEqual(extractCol(self.board3by3, 3, 1), [-1, -1, 1])
        self.assertEqual(extractCol(self.board3by3, 3, 2), [-1, 0, 1])
        self.assertEqual(extractCol(self.board3by3, 3, 3), [-1, -1, 1])
        self.assertEqual(extractCol(self.board4by4, 4, 1), [-1, 0, 1, -1])
        self.assertEqual(extractCol(self.board4by4, 4, 2), [-1, 0, 1, 1])
        self.assertEqual(extractCol(self.board4by4, 4, 3), [-1, 0, 0, 0])
        self.assertEqual(extractCol(self.board4by4, 4, 4), [-1, 0, 0, -1])

    def test_extract_diag(self):
        self.assertEqual(extractLeadDiagonal(self.board3by3, 3), [-1, 0, 1])
        self.assertEqual(extractLesserDiagonal(self.board3by3, 3), [-1, 0, 1])
        self.assertEqual(extractLeadDiagonal(self.board4by4, 4), [-1, 0, 0, -1])
        self.assertEqual(extractLesserDiagonal(self.board4by4, 4), [-1, 0, 1, -1])
        

    def test_row_view(self):
        self.assertEqual(getRowRepr(self.board3by3, 3, 1), ' | | ')
        self.assertEqual(getRowRepr(self.board3by3, 3, 2), ' |x| ')
        self.assertEqual(getRowRepr(self.board3by3, 3, 3), 'o|o|o')
        self.assertEqual(getRowRepr(self.board4by4, 4, 1), ' | | | ')
        self.assertEqual(getRowRepr(self.board4by4, 4, 2), 'x|x|x|x')
        self.assertEqual(getRowRepr(self.board4by4, 4, 3), 'o|o|x|x')
        self.assertEqual(getRowRepr(self.board4by4, 4, 4), ' |o|x| ')

    def test_separator(self):
        self.assertEqual(getSeparator(3), '-+-+-')
        self.assertEqual(getSeparator(4), '-+-+-+-')

    def test_board_view(self):
        self.assertEqual(getBoardRepr(self.board3by3, 3), ' | | \n-+-+-\n |x| \n-+-+-\no|o|o\n')
        self.assertEqual(getBoardRepr(self.board4by4, 4), ' | | | \n-+-+-+-\nx|x|x|x\n-+-+-+-\no|o|x|x\n-+-+-+-\n |o|x| \n')

    def test_count_distinct(self):
        self.assertEqual(countDistinct([]), 0)
        self.assertEqual(countDistinct([7]), 1)
        self.assertEqual(countDistinct([3, 3]), 1)
        self.assertEqual(countDistinct([5, 6]), 2)
        self.assertEqual(countDistinct([5, 6, 7, 8, 9]), 5)
        self.assertEqual(countDistinct([0, 0, 0, 0, 0]), 1)
        self.assertEqual(countDistinct([2, -1, 2, -1, 2]), 2)

    def test_has_one(self):
        self.assertFalse(hasOneDistinct([]))
        self.assertTrue(hasOneDistinct([7]))
        self.assertTrue(hasOneDistinct([8, 8, 8, 8]))
        self.assertFalse(hasOneDistinct([0, 1, 0, 1]))
        self.assertFalse(hasOneDistinct([-1, -2, -3, -4]))

    def test_subsequence_winner(self):
        self.assertEqual(getSubsequenceWinner([0, 0, 0]), 0)
        self.assertEqual(getSubsequenceWinner([1, 1, 1, 1, 1]), 1)
        self.assertEqual(getSubsequenceWinner([0, 1, 1, 1]), -1)
        self.assertEqual(getSubsequenceWinner([-1, -1, -1, -1]), -1)
        self.assertEqual(getSubsequenceWinner([-1, 1, 1, 1]), -1)
        self.assertEqual(getSubsequenceWinner([-1, 0, 0, 0]), -1)

    def test_subsequences(self):
        self.assertEqual(getSubsequences([1, 2, 3], 3), [[1, 2, 3]])
        self.assertEqual(getSubsequences([1, 2, 3], 2), [[1, 2], [2, 3]])
        self.assertEqual(getSubsequences([1, 2, 3, 4], 3), [[1, 2, 3], [2, 3, 4]])
        self.assertEqual(getSubsequences([1, 2, 3, 4], 2), [[1, 2], [2, 3], [3, 4]])

    def test_sequences(self):
        self.assertEqual(
            set(map(tuple, getSequences(self.board3by3, 3))),
            {(-1, -1, -1), (-1, -1, 1), (-1, 0, -1), (-1, 0, 1), (1, 1, 1)})

    def test_subsequences(self):
        self.assertEqual(
            set(map(tuple, getBoardSubsequences(self.board3by3, 3, 2))),
            {(-1, -1), (-1, 1), (-1, 0), (0, -1), (0, 1), (1, 1)})

    def test_winner(self):
        self.assertEqual(getWinner(getEmptyBoard(3), 3, 3), -1)
        self.assertEqual(getWinner(self.board3by3, 3, 3), 1)
        self.assertEqual(getWinner(self.board4by4, 4, 4), 0)


if __name__ == '__main__':
    unittest.main()
