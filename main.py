# temp values
from searchAlgorithms.BFS import BFS
from searchable.SearchableXPuzzle import SearchableXPuzzle
from searchAlgorithms.IDS import IDS

algoNumber = 1
rowColSize = 4
boardState = '1-2-3-4-5-6-7-8-9-10-11-12-13-0-14-15'
goalState = '1-2-3-4-5-6-7-8-9-10-11-12-13-14-15-0'


def stringToMatrix(string, matrixLength):
    temp = string.split('-')
    matrix = []
    for row in range(matrixLength):
        matrixRow = []
        for col in range(matrixLength):
            matrixRow.append(int(temp[(row * matrixLength) + col]))
        matrix.append(matrixRow)
    return matrix


problem = SearchableXPuzzle(stringToMatrix(boardState, rowColSize), stringToMatrix(goalState, rowColSize))
print(BFS(problem))
