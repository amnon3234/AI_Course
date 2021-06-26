import copy

from searchable.SearchableState import SearchableState


# search for the empty place in the state
def search_for_pos(state, row_and_col_amount):
    for row in range(row_and_col_amount):
        for col in range(row_and_col_amount):
            if state.stateValue[row][col] == 0:
                return row, col


# generate a new state
def generate_state(current_state, zero_row, zero_col, swap_row, swap_col):
    temp = copy.deepcopy(current_state.stateValue)
    temp[zero_row][zero_col] = temp[swap_row][swap_col]
    temp[swap_row][swap_col] = 0
    return SearchableState(temp)


class SearchableXPuzzle:

    def __init__(self, start_state, goal_state):
        """
        :param start_state problem start state as a matrix
        :param goal_state problem goal state as a matrix
        """
        self.rowAndColAmount = len(start_state)
        self.startState = SearchableState(start_state)
        self.goalState = SearchableState(goal_state)
        self.startState.stateCost = 0

    def get_all_possible_states(self, state):
        """
        used to receive all relevant possible states.

        :param state: state to create neighbors to
        :return: array of neighbors states
        """
        SearchableState.check_instance(state)
        neighbors = []
        row, col = search_for_pos(state, self.rowAndColAmount)

        if row != 0:
            new_state = generate_state(state, row, col, row - 1, col)
            new_state.stateFather = state
            new_state.stateCost = state.stateCost + 1
            neighbors.append(new_state)

        if row != self.rowAndColAmount - 1:
            new_state = generate_state(state, row, col, row + 1, col)
            new_state.stateCost = state.stateCost + 1
            new_state.stateFather = state
            neighbors.append(new_state)

        if col != 0:
            new_state = generate_state(state, row, col, row, col - 1)
            new_state.stateCost = state.stateCost + 1
            new_state.stateFather = state
            neighbors.append(new_state)

        if col != self.rowAndColAmount - 1:
            new_state = generate_state(state, row, col, row, col + 1)
            new_state.stateCost = state.stateCost + 1
            new_state.stateFather = state
            neighbors.append(new_state)

        return neighbors

    def is_goal_state(self, state):
        """
        used to check if current state is the goal state

        :param state: state to check
        :return: state is goal state ? true : false
        """
        SearchableState.check_instance(state)
        return state == self.goalState

    def get_route(self, state):
        """
        used to receive the route from start state

        :param state:
        :return: route from start state to this state
        """
        SearchableState.check_instance(state)
        current_state = state
        father_state = state.stateFather
        route = []
        while father_state is not None:
            curr_row, curr_col = search_for_pos(current_state, self.rowAndColAmount)
            father_row, father_col = search_for_pos(father_state, self.rowAndColAmount)
            if curr_row < father_row:
                route.append('D')
            elif curr_row > father_row:
                route.append('U')
            elif curr_col < father_col:
                route.append('R')
            else:
                route.append('L')
            current_state = father_state
            father_state = current_state.stateFather
        route.reverse()
        return route

    def manhattan(self):
        inc = 0
        h = 0
        for i in range(3):
            for j in range(3):
                h += abs(inc - self.board[i][j])
            inc += 1
        return h
