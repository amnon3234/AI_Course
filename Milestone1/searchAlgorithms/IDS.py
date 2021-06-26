from searchable.SearchableXPuzzle import SearchableXPuzzle


def dfs(problem, current_state, max_depth, o_list, c_list):
    if problem.is_goal_state(current_state):
        return True, problem.get_route(current_state)
    if max_depth <= 0:
        return False, None
    for state in problem.get_all_possible_states(current_state):
        state_hash = state.get_hash_key()
        if state_hash in c_list:
            continue
        if state_hash in o_list and state.stateCost >= o_list[state_hash].stateCost:
            continue
        o_list[state_hash] = state
        res, route = dfs(problem, state, max_depth - 1, o_list, c_list)
        if res:
            return res, route

    current_state_hash = current_state.get_hash_key()
    if current_state_hash in o_list:
        del o_list[current_state_hash]
    c_list[current_state_hash] = current_state
    return False, None


def ids(problem):
    """
    Used to find goal state using the IDS algorithm

    :param problem: x puzzle problem
    :return: route to goal state
    """
    if not isinstance(problem, SearchableXPuzzle):
        raise Exception('problem must be instance of SearchableXPuzzle')
    depth = 0
    init_state = problem.startState
    res, route = dfs(problem, init_state, depth, {}, {})
    while not res:
        depth += 1
        res, route = dfs(problem, init_state, depth, {}, {})
    return route
