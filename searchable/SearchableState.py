import sys


class SearchableState:
    def __init__(self, state_value):
        """
        :param state_value: matrix of values
        """
        self.stateValue = state_value
        self.stateCost = sys.maxsize
        self.stateFather = None

    def compare_to(self, other):
        """
        Used to determine who will come first in a sort

        :param other: SearchableState instance
        :return: 0 for equality, - self < other, + self > other
        """
        self.check_instance(other)
        return self.stateCost - other.stateCost

    def get_hash_key(self):
        """
        Used to get a unique hash key for any state with the same value

        :return: hashKey string
        """
        hash_string = ''
        for row in self.stateValue:
            for col in row:
                hash_string += str(col) + '-'
        return hash_string

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
        self.check_instance(other)
        return self.stateValue == other.stateValue

    def __ne__(self, other):
        """
        Override the default != to determine inequality by state value

        :param other: SearchableState instance
        :return: self != other ? True : False
        """
        return not self.__eq__(other)

    @staticmethod
    def check_instance(var):
        if not isinstance(var, SearchableState):
            raise Exception('state must be an instance of searchable state')
