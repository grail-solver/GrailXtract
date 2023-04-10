import os
from core.helper import extract_data

"""
This module is dedicated to test our protocol output using gpt
"""


def run_test():
    test_folder_path = 'case'
    for folder_name in os.listdir(test_folder_path):
        folder_path = os.path.join(test_folder_path, folder_name)
        if os.path.isdir(folder_path):
            # For each problem file
            for file_name in os.listdir(folder_path):
                if file_name.endswith('.txt'):
                    file_path = os.path.join(folder_path, file_name)
                    with open(file_path, 'r') as file:
                        text = file.read()

                    # Extract relevant data from the text
                    result = extract_data(text)

                    # Save text output in file
                    result_file_path = os.path.join(folder_path, 'result.txt')
                    with open(result_file_path, 'w') as result_file:
                        result_file.write(result)


def run_specific_test(folder: str):
    folder_path = os.path.join('case', folder)
    if os.path.isdir(folder_path):
            # For each problem file
            for file_name in os.listdir(folder_path):
                if file_name.endswith('.txt'):
                    file_path = os.path.join(folder_path, file_name)
                    with open(file_path, 'r') as file:
                        text = file.read()

                    # Extract relevant data from the text
                    result = extract_data(text)

                    # Save text output in file
                    result_file_path = os.path.join(folder_path, 'result.txt')
                    with open(result_file_path, 'w') as result_file:
                        result_file.write(result)


if __name__ == '__main__':
    # run_test()
    run_specific_test('case_04_ratheil')
