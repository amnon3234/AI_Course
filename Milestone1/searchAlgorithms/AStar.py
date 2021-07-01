from searchable.SearchableXPuzzle import SearchableXPuzzle


def best_value(o_list):
    f = o_list[0].f
    index = 0
    for i, item in enumerate(o_list):
        if i == 0:
            continue
        if item.f < f:
            f = item.f
            index = i

    return o_list[index], index


def a_star(problem):
    """
    Used to find goal state using the AStar algorithm

    :param problem: x puzzle problem
    :return: route to goal state
    """
    if not isinstance(problem, SearchableXPuzzle):
        raise Exception('problem must be instance of SearchableXPuzzle')

    o_list, c_list = [], []
    init_state = problem.startState
    o_list.append(init_state)
    while o_list:
        current_state, index = best_value(o_list)
        if problem.is_goal_state(current_state):
            return problem.get_route(current_state)
        o_list.pop(index)
        c_list.append(current_state)

        for move in problem.get_all_possible_states(current_state):
            ok = False  # checking in closedList
            for i, item in enumerate(c_list):
                if item == move:
                    ok = True
                    break
            if not ok:  # not in closed list
                new_g = current_state.g + 1
                present = False

                # openList includes move
                for j, item in enumerate(o_list):
                    if item == move:
                        present = True
                        if new_g < o_list[j].g:
                            o_list[j].g = new_g
                            o_list[j].f = o_list[j].g + o_list[j].h
                            o_list[j].parent = current_state
                if not present:
                    move.g = new_g
                    move.h = move.manhattan()
                    move.f = move.g + move.h
                    move.parent = current_state
                    o_list.append(move)

        return None