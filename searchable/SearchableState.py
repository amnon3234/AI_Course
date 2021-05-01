import sys


class SearchableState:
    def __init__(self, stateValue):
        """
        :param stateValue: matrix of values
        """
        self.stateValue = stateValue
        self.stateCost = sys.maxint
        self.stateFather = None

    def compareTo(self, other):
        """
        Used to determine who will come first in a sort

        :param other: SearchableState instance
        :return: 0 for equality, - self < other, + self > other
        """
        self.checkInstance(other)
        return self.stateCost - other.stateCost

    def getHashKey(self):
        """
        Used to get a unique hash key for any state with the same value

        :return: hashKey string
        """
        hashString = ''
        for row in self.stateValue:
            for col in row:
                hashString += str(col) + '-'
        return hashString

    def __str__(self):
        """
        Override the default to string function to print state values
        """
        return str(self.stateValue)

    def __eq__(self, other):
        """
        Override the default == to determine equality by state value

        :param other: SearchableState instance
        :return: self == other ? True : False
        """
        self.checkInstance(other)
        return self.stateValue == other.stateValue

    def __ne__(self, other):
        """
        Override the default != to determine inequality by state value

        :param other: SearchableState instance
        :return: self != other ? True : False
        """
        return not self.__eq__(other)

    @staticmethod
    def checkInstance(var):
        if not isinstance(var, SearchableState):
            raise Exception('state must be an instance of searchable state')
