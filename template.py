def solve():
    """
    Solve the given problem here.
    :return: Expected output.
    """
    return 0


def driver():
    """
    Write a driver that reads from system input.
    :return: Nothing.
    """
    # a, b = list(map(int, input().split(' ')))
    # Collect variables as required.

    print(solve())
    return


def main():
    """
    Call the driver.
    :return: Nothing.
    """
    driver()
    return


if __name__ == '__main__':
    main()

# ********************** SOLUTION ENDS **********************
# ********************** TESTING begins **********************


# The code that follows is for testing purposes only.
# This should not be submitted for judging.


def file_driver(contents):
    """
    Write a file driver that reads from
    a list of strings where each string
    correspond to a line of input.

    :param contents: All lines of the file
    that has the input data.
    :return: The calculated output.
    """
    result = None
    for row in contents:
        # a, b = list(map(int, row.split(' ')))
        # Collect the variables as required.
        pass

    result = solve()
    return result


class Problem:
    """
    The solution class for testing purposes.
    """
    def __init__(self, input_data):
        """
        Create an instance with the given data
        so that the output is populated as
        required.
        :param input_data: All lines of the file
        that has the input data.
        """
        self.output = file_driver(input_data)
        pass


# ********************** TESTING ENDS **********************
