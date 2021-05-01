from searchable.SearchableXPuzzle import SearchableXPuzzle


def DFS(problem, currentState, maxDepth, oList, cList):
    if problem.isGoalState(currentState):
        return True, problem.getRoute(currentState)
    if maxDepth <= 0:
        return False, None
    for state in problem.getAllPossibleStates(currentState):
        stateHash = state.getHashKey()
        if stateHash in cList:
            continue
        if stateHash in oList and state.stateCost >= oList[stateHash].stateCost:
            continue
        oList[stateHash] = state
        res, route = DFS(problem, state, maxDepth - 1, oList, cList)
        if res:
            return res, route

    currentStateHash = currentState.getHashKey()
    if currentStateHash in oList:
        del oList[currentStateHash]
    cList[currentStateHash] = currentState
    return False, None


def IDS(problem):
    if not isinstance(problem, SearchableXPuzzle):
        raise Exception('problem must be instance of SearchableXPuzzle')
    depth = 0
    initState = problem.startState
    res, route = DFS(problem, initState, depth, {}, {})
    while not res:
        depth += 1
        res, route = DFS(problem, initState, depth, {}, {})
    return route
