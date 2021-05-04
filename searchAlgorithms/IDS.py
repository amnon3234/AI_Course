from searchable.SearchableXPuzzle import SearchableXPuzzle


def DFS(problem, currentState, maxDepth, oList, cList):
    if problem.is_goal_state(currentState):
        return True, problem.get_route(currentState)
    if maxDepth <= 0:
        return False, None
    for state in problem.get_all_possible_states(currentState):
        stateHash = state.get_hash_key()
        if stateHash in cList:
            continue
        if stateHash in oList and state.stateCost >= oList[stateHash].stateCost:
            continue
        oList[stateHash] = state
        res, route = DFS(problem, state, maxDepth - 1, oList, cList)
        if res:
            return res, route

    currentStateHash = currentState.get_hash_key()
    if currentStateHash in oList:
        del oList[currentStateHash]
    cList[currentStateHash] = currentState
    return False, None


def IDS(problem):
    """
    Used to find goal state using the IDS algorithm

    :param problem: x puzzle problem
    :return: route to goal state
    """
    if not isinstance(problem, SearchableXPuzzle):
        raise Exception('problem must be instance of SearchableXPuzzle')
    depth = 0
    initState = problem.startState
    res, route = DFS(problem, initState, depth, {}, {})
    while not res:
        depth += 1
        res, route = DFS(problem, initState, depth, {}, {})
    return route
