from pathlib import Path
import os
import sys

TOP = Path('../IEEExtreme14')
DATA = (TOP / 'data')
DATA_INPUT = DATA / 'input'
DATA_OUTPUT = DATA / 'output'
PROBLEM = (TOP / 'solutions')


def given_problem(problem_name: str, input_test_case: str):
    """
    Run the problem in a shell and
    collect the outputs (not prints)
    and return it.

    :param problem_name: The name of the problem to be tested.
    :param input_test_case: The name of the input test case.
    :return: The calculated output.
    """
    command = f'python solutions/{problem_name.title()}.py < data/input/{input_test_case}'
    try:
        output = os.popen(command)
    except BrokenPipeError as e:
        print(e)
        output = None
    return output


def all_cases_per_problem(problem_name):
    """
    Given a problem name, test it
    against the test_cases defined
    in the data/input and data/output
    directories.

    :param problem_name: The name of the problem.
    :return: None
    """
    problem_name = problem_name.title()

    sample_cases_input = DATA_INPUT.glob(f'{problem_name}*')
    sample_cases_output = DATA_OUTPUT.glob(f'{problem_name}*')
    print(f'Testing Problem: {problem_name}')

    for case in zip(sorted(sample_cases_input), sorted(sample_cases_output)):
        case_inp, case_out = case
        solution_output = given_problem(problem_name, str(os.path.basename(case_inp)))
        calculated_output = [i.rstrip() for i in solution_output]
        with open(case_out, 'r') as f_output:
            expected_output = [i.rstrip() for i in f_output]
        passed = calculated_output == expected_output

        if passed:
            print(f'Test Case: {str(os.path.basename(case_inp))}', 'passed successfully!')
        else:
            print(f'Test Case: {str(os.path.basename(case_inp))}', 'FAILED!')
            print(f'Output:', str(calculated_output), '\t\t', 'Expected:', expected_output)
    return


def main():
    """
    Ask for an iterable of problems
    and test them all.
    :return: None.
    """
    for p in sys.argv[1:]:
        all_cases_per_problem(p.title())
    return


if __name__ == '__main__':
    main()
