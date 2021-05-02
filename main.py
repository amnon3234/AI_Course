# temp values
from searchAlgorithms.BFS import BFS
from searchable.SearchableXPuzzle import SearchableXPuzzle
from searchAlgorithms.IDS import IDS

# CR: In python we use snakeCase and not camelCase
# like : def generate_goal_state(matrix_length):
# need to change all the files :\
def generateGoalState(matrixLength):
    matrix = []
    for row in range(matrixLength):
        matrixRow = []
        for col in range(matrixLength):
            matrixRow.append(row * matrixLength + col + 1)
        matrix.append(matrixRow)
    matrix[matrixLength - 1][matrixLength - 1] = 0
    return matrix


def stringToMatrix(string, matrixLength):
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
    startState = stringToMatrix(state, size)
    goalState = generateGoalState(size)
    problem = SearchableXPuzzle(startState, goalState)

    # CR : Why not switch case?
    if algo == 1:
        routeToGoal = IDS(problem)
        #CR : in python3, print function has been replaced by the print() function, meaning that we have to wrap the object that we want to print in parantheses.
        print routeToGoal
    elif algo == 2:
        # CR : same as above
        routeToGoal = BFS(problem)
        print routeToGoal
    elif algo == 3:
        pass


main()
