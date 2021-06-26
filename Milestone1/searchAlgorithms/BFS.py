from searchable.SearchableXPuzzle import SearchableXPuzzle


def bfs(problem):
    """
    Used to find goal state using the BFS algorithm

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
        for state in problem.get_all_possible_states(current_state):
            state_hash = state.get_hash_key()
            if state_hash in c_list:
                continue
            if state_hash in o_list and state.stateCost >= o_list[state_hash].stateCost:
                continue
            o_list[state_hash] = state
            queue.append(state)
        current_state_hash = current_state.get_hash_key()
        if current_state_hash in o_list:
            del o_list[current_state_hash]
        c_list[current_state_hash] = current_state
    return None
