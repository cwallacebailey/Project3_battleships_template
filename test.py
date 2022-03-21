""" testing module"""

destroyer_destroyed = False  # pylint: disable=C0103


class Test():
    """
    test
    """
    def __init__(self, destroyer_destroyed):
        self.test = self.tester()

    def tester(self):
        """
        anything
        """
        destroyer_destroyed = True
        print(destroyer_destroyed)
        return destroyer_destroyed


Test(destroyer_destroyed)
