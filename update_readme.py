import os

def generate_file_list(directory='.', indent=0):
    """
    Recursively generate a list of files in each folder.

    :param directory: Directory to start from
    :param indent: Indentation level for nested folders
    :return: Formatted string with file listing
    """
    file_list = ""
    for root, dirs, files in os.walk(directory):
        # Skip hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        # Add directory to the file list
        relative_path = os.path.relpath(root, start=directory)
        if relative_path == ".":
            relative_path = "Root Directory"
        file_list += f"{'  ' * indent}- **{os.path.basename(relative_path)}/**\n"

        # List files in the current directory
        for file in sorted(files):
            if not file.startswith('.'):
                file_list += f"{'  ' * (indent + 1)}- {file}\n"

        # Recursively list subdirectories
        for d in sorted(dirs):
            file_list += generate_file_list(os.path.join(root, d), indent + 1)
        break  # Prevent deeper recursion since we manually traverse
    return file_list


def update_readme():
    """
    Update the README.md file with the current list of files in each folder.
    """
    # Define the content for the README file
    header = "# LeetCode Problem Solutions\n\nWelcome to my LeetCode problem solutions repository! Here, you'll find my solutions to various LeetCode problems organized by category.\n\n## Introduction\n\n\
    This repository contains my solutions to LeetCode problems. Each problem solution is organized into specific categories such as Dynamic Programming, Strings, Arrays, Heaps, etc. \n\n\
    Feel free to explore the solutions, and I hope you find them helpful in your learning journey! "
    introduction = ""
    # (
    #       "This README file is automatically updated with a list of all files in the project directory "
    #       "every time there is a push to the main branch.\n\n"
    #   )

    # Generate the file list
    file_structure = generate_file_list()

    # Write the content to the README file
    with open('README.md', 'w') as f:
        f.write(header)
        f.write(introduction)
        f.write(file_structure)

    print("README.md updated successfully.")


if __name__ == '__main__':
    update_readme()
