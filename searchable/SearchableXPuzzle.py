import copy

from searchable.SearchableState import SearchableState


# search for the empty place in the state
def search_for_pos(state, rowAndColAmount):
    for row in range(rowAndColAmount):
        for col in range(rowAndColAmount):
            if state.stateValue[row][col] == 0:
                return row, col


# generate a new state
def generate_state(currState, zeroRow, zeroCol, swapRow, swapCol):
    temp = copy.deepcopy(currState.stateValue)
    temp[zeroRow][zeroCol] = temp[swapRow][swapCol]
    temp[swapRow][swapCol] = 0
    return SearchableState(temp)


class SearchableXPuzzle:

    def __init__(self, startState, goalState):
        """
        :param startState problem start state as a matrix
        :param goalState problem goal state as a matrix
        """
        self.rowAndColAmount = len(startState)
        self.startState = SearchableState(startState)
        self.goalState = SearchableState(goalState)
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
            newState = generate_state(state, row, col, row - 1, col)
            newState.stateFather = state
            newState.stateCost = state.stateCost + 1
            neighbors.append(newState)

        if row != self.rowAndColAmount - 1:
            newState = generate_state(state, row, col, row + 1, col)
            newState.stateCost = state.stateCost + 1
            newState.stateFather = state
            neighbors.append(newState)

        if col != 0:
            newState = generate_state(state, row, col, row, col - 1)
            newState.stateCost = state.stateCost + 1
            newState.stateFather = state
            neighbors.append(newState)

        if col != self.rowAndColAmount - 1:
            newState = generate_state(state, row, col, row, col + 1)
            newState.stateCost = state.stateCost + 1
            newState.stateFather = state
            neighbors.append(newState)

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
        currentState = state
        fatherState = state.stateFather
        route = []
        while fatherState is not None:
            currRow, currCol = search_for_pos(currentState, self.rowAndColAmount)
            fatherRow, fatherCol = search_for_pos(fatherState, self.rowAndColAmount)
            if currRow < fatherRow:
                route.append('D')
            elif currRow > fatherRow:
                route.append('U')
            elif currCol < fatherCol:
                route.append('R')
            else:
                route.append('L')
            currentState = fatherState
            fatherState = currentState.stateFather
        route.reverse()
        return route
