# temp values
from searchAlgorithms.BFS import BFS
from searchable.SearchableXPuzzle import SearchableXPuzzle
from searchAlgorithms.IDS import IDS

def generate_goal_state(matrixLength):
    matrix = []
    for row in range(matrixLength):
        matrixRow = []
        for col in range(matrixLength):
            matrixRow.append(row * matrixLength + col + 1)
        matrix.append(matrixRow)
    matrix[matrixLength - 1][matrixLength - 1] = 0
    return matrix


def string_to_matrix(string, matrixLength):
    temp = string.split('-')
    matrix = []
    for row in range(matrixLength):
        matrixRow = []
        for col in range(matrixLength):
            matrixRow.append(int(temp[(row * matrixLength) + col]))
        matrix.append(matrixRow)
    return matrix


def main():
    iFile = open("input.txt", "r")
    algo, size, state = int(iFile.readline().replace('\n', '')), int(iFile.readline().replace('\n', '')), \
                        iFile.readline().replace('\n', '')
    startState = string_to_matrix(state, size)
    goalState = generate_goal_state(size)
    problem = SearchableXPuzzle(startState, goalState)

    match algo:
        case 1:
            routeToGoal = IDS(problem)
            print(routeToGoal)
        case 2:
            routeToGoal = BFS(problem)
            print(routeToGoal)
        default:
            pass


main()
