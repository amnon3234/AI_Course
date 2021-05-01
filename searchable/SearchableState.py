import sys


class SearchableState:
    def __init__(self, stateValue):
        self.stateValue = stateValue
        self.stateCost = sys.maxint
        self.stateFather = None

    def __eq__(self, other):
        if not isinstance(other, SearchableState):
            return False
        return self.stateValue == other.stateValue

    def __ne__(self, other):
        return not self.__eq__(other)

    def compareTo(self, other):
        if not isinstance(other, SearchableState):
            return False
        return self.stateCost - other.stateCost

    def __str__(self):
        return str(self.stateValue)
