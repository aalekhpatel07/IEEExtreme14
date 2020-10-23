from pathlib import Path
import os
import sys
from typing import List

TOP = Path('../IEEExtreme14')
DATA = (TOP / 'data')
DATA_INPUT = DATA / 'input'
DATA_OUTPUT = DATA / 'output'
PROBLEM = (TOP / 'solutions')


def given_problem(problem_name: str, input_data: List[str]):
    """
    Given a problem, and some input data,
    produce its output by executing the file_driver
    method in the Problem file.

    :param problem_name: The name of the problem to be tested.
    :param input_data: The contents of the input file as a list of lines.
    :return: The calculated output.
    """

    module = __import__(f'solutions.{problem_name.title()}')
    problem_class = getattr(module, problem_name.title())
    current_problem = getattr(problem_class, problem_name.title())

    problem_instance = current_problem(input_data)

    return problem_instance.output


def all_cases_per_problem(problem_name):
    """
    Given a problem name, dynamically
    test it against the test_cases defined
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
        case_inp = case[0]
        case_out = case[1]
        with open(case_inp, 'r') as f_input:
            content = [i for i in f_input]
            solution = given_problem(problem_name, content)
        with open(case_out, 'r') as f_output:
            all_answer = f_output.readline()
            if str(solution).rstrip() == all_answer.rstrip():
                print(f'Test Case: {str(os.path.basename(case_inp))}', 'passed successfully!')
            else:
                print(f'Test Case: {str(os.path.basename(case_inp))}', 'FAILED!')
                print(f'Output:', str(solution), '\t\t', 'Expected:', all_answer)

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
