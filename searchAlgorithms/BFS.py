from searchable.SearchableXPuzzle import SearchableXPuzzle


def BFS(problem):
    """
    Used to find goal state using the BFS algorithm

    :param problem: x puzzle problem
    :return: route to goal state
    """
    if not isinstance(problem, SearchableXPuzzle):
        raise Exception('problem must be instance of SearchableXPuzzle')

    queue, oList, cList = [], {}, {}
    initState = problem.startState
    queue.append(initState)
    while len(queue) > 0:
        currState = queue.pop(0)
        if problem.isGoalState(currState):
            return problem.getRoute(currState)
        for state in problem.getAllPossibleStates(currState):
            stateHash = state.getHashKey()
            if stateHash in cList:
                continue
            if stateHash in oList and state.stateCost >= oList[stateHash].stateCost:
                continue
            oList[stateHash] = state
            queue.append(state)
        currentStateHash = currState.getHashKey()
        if currentStateHash in oList:
            del oList[currentStateHash]
        cList[currentStateHash] = currState
    return None
