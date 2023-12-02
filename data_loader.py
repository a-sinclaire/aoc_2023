import __main__
import os


def get_data():
    directory_name = os.path.dirname(__file__)
    base_name = os.path.basename(__main__.__file__).strip('.py')
    file_path = os.path.join(directory_name, f'data/{base_name}.data')
    print(f'Loading data from {file_path}...')
    with open(file_path) as f:
        data = f.readlines()
    return data
