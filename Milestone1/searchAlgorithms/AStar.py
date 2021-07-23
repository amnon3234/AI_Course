from searchable.SearchableXPuzzle import SearchableXPuzzle


def manhattan_distance(state):
    distance = 0
    n = len(state.stateValue)
    for i in range(n):
        for j in range(n):
            x, y = divmod(state.stateValue[i][j], n)
            distance += abs(x - i) + abs(y - j)
    return distance


def a_star(problem):
    """
    Used to find goal state using the AStar algorithm

    :param problem: x puzzle problem
    :return: route to goal state
    """
    if not isinstance(problem, SearchableXPuzzle):
        raise Exception('problem must be instance of SearchableXPuzzle')

    queue, o_list, c_list = [], {}, {}
    init_state = problem.startState
    queue.append(init_state)
    while len(queue) > 0:
        current_state = queue.pop(0)
        if problem.is_goal_state(current_state):
            return problem.get_route(current_state)
        shortest_route = 0
        for state in problem.get_all_possible_states(current_state):
            if manhattan_distance(state) < shortest_route:
                current_state = state
            shortest_route = manhattan_distance(state)
            state_hash = state.get_hash_key()
            o_list[state_hash] = state
            queue.append(state)
        current_state_hash = current_state.get_hash_key()
        if current_state_hash in o_list:
            del o_list[current_state_hash]
        c_list[current_state_hash] = current_state
