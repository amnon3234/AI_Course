from searchable.SearchableXPuzzle import SearchableXPuzzle


def DFS(problem, currentState, maxDepth):
    print('checking for ', currentState.stateValue)
    if problem.isGoalState(currentState):
        print('found')
        return True
    if maxDepth <= 0:
        return False
    for state in problem.getAllPossibleStates(currentState):
        if DFS(problem, state, maxDepth - 1):
            return True
    return False


def run(problem):
    if not isinstance(problem, SearchableXPuzzle):
        raise Exception('problem must be instance of SearchableXPuzzle')
    depth = 0
    initState = problem.startState
    while not DFS(problem, initState, depth):
        depth += 1
