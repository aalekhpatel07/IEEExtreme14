def solve(a, b):
    return a + b


def driver():
    a, b = list(map(int, input().split(' ')))
    print(solve(a, b))
    return


def main():
    driver()
    return

#
# if __name__ == '__main__':
#     main()

# When submitting uncomment above and remove the following!


def file_driver(contents):
    # contents contains lines of data.
    # If just the first line is required, take the first row.
    if len(contents) == 0:
        # No input
        return

    result = None
    for row in contents:
        a, b = list(map(int, row.split(' ')))
        result = solve(a, b)
    return result


class Addition:
    def __init__(self, input_data):
        self.output = file_driver(input_data)
        pass
