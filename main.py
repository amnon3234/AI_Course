from searchAlgorithms.AStar import a_star
from searchAlgorithms.BFS import bfs
from searchAlgorithms.IDS import ids
from searchable.SearchableXPuzzle import SearchableXPuzzle


def generate_goal_state(matrix_length):
    matrix = []
    for row in range(matrix_length):
        matrix_row = []
        for col in range(matrix_length):
            matrix_row.append(row * matrix_length + col + 1)
        matrix.append(matrix_row)
    matrix[matrix_length - 1][matrix_length - 1] = 0
    return matrix


def string_to_matrix(string, matrix_length):
    temp = string.split('-')
    matrix = []
    for row in range(matrix_length):
        matrix_row = []
        for col in range(matrix_length):
            matrix_row.append(int(temp[(row * matrix_length) + col]))
        matrix.append(matrix_row)
    return matrix


def main():
    input_file = open("input.txt", "r")
    algo, size, state = int(input_file.readline().replace('\n', '')), int(
        input_file.readline().replace('\n', '')), input_file.readline().replace('\n', '')
    start_state = string_to_matrix(state, size)
    goal_state = generate_goal_state(size)
    problem = SearchableXPuzzle(start_state, goal_state)

    if algo == 1:
        route_to_goal = ids(problem)
        print(route_to_goal)
    elif algo == 2:
        route_to_goal = bfs(problem)
        print(route_to_goal)
    elif algo == 3:
        route_to_goal = a_star(problem)
        print(route_to_goal)
    else:
        pass

    # match algo:
    #     case 1:
    #         route_to_goal = ids(problem)
    #         print(route_to_goal)
    #     case 2:
    #         route_to_goal = bfs(problem)
    #         print(route_to_goal)
    #     default:
    #         pass


if __name__ == '__main__':
    main()
