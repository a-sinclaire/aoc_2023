import __main__
import os


def get_data():
    directory_name = os.path.dirname(__file__)
    base_name = os.path.basename(__main__.__file__).strip('.py')
    file_path = os.path.join(directory_name, f'data/{base_name}.data')
    try:
        with open(file_path) as f:
            data = f.readlines()
        print(f'Loading data from {file_path}...')
    except FileNotFoundError:
        print(f'Could not find puzzle input at {file_path}')
        data = None

    test1_file_path = os.path.join(directory_name, f'data/{base_name}.test1')
    try:
        with open(test1_file_path) as f:
            test1 = f.readlines()
        print(f'Loading test1 data from {test1_file_path}...')
    except FileNotFoundError:
        print(f'Could not find test1 data at {test1_file_path}')
        test1 = None

    test2_file_path = os.path.join(directory_name, f'data/{base_name}.test2')
    try:
        with open(test2_file_path) as f:
            test2 = f.readlines()
        print(f'Loading test2 data from {test2_file_path}...')
    except FileNotFoundError:
        print(f'Could not find test2 data at {test2_file_path}')
        test2 = None

    return data, test1, test2
