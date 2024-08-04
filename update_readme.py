import os

counter = 0


def list_files_in_directory(directory='.', indent=''):
    """
    Generates a formatted list of all files and directories within a given directory.
    This function skips hidden files and directories.

    :param directory: The starting directory to scan.
    :param indent: The current indentation level for nested directories.
    :return: A formatted string of files and directories.
    """
    result = ""
    global counter
    # print(os.listdir(directory))
    for item in os.listdir(directory):
        if item.startswith('.'):
            continue  # Skip hidden files and directories
        path = os.path.join(directory, item)
        if os.path.isdir(path):
            result += f"### {indent}**{item}**\n"  # Directory
            result += list_files_in_directory(path, indent + '  ')
        else:
            if item != 'update_readme.py' and item != 'update_readme.sh' and item != 'README.md':
                counter += 1
                result += f"{indent}- {item}\n"  # File
    return result


def update_readme():
    """
    Updates the README.md file with the list of files in the project directory.
    """
    header = "# LeetCode Problem Solutions\n\n"
    file_structure = list_files_in_directory()
    introduction = f"Welcome to my LeetCode problem solutions repository! Here, you'll find my solutions to various LeetCode problems organized by category.\n\n## Introduction\n\n\
    This repository contains my solutions to LeetCode problems. Each problem solution is organized into specific categories such as Dynamic Programming, Strings, Arrays, Heaps, etc. \n\n\
    Feel free to explore the solutions, and I hope you find them helpful in your learning journey! Number of problems solved till now: {counter}\n\n"
    # introduction = "This README file lists all files in the project directory.\n\n"

    with open('README.md', 'w') as readme_file:
        readme_file.write(header)
        readme_file.write(introduction)
        readme_file.write(file_structure)

    print("README.md updated successfully.")


if __name__ == '__main__':
    update_readme()
