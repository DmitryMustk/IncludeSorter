import sys
import os

def is_c_or_cpp_file(file_path):
    _, file_extension = os.path.splitext(file_path)
    return file_extension.lower() in ['.c', '.cpp', '.h', '.hpp']

def process_file(file_path):
    user_includes = []  
    stdlib_includes = []  
    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        if line.startswith("#include"):
            include_path = line.split()[1].strip('"<>')
            if line.startswith("#include \""):
                user_includes.append(include_path)
            elif line.startswith("#include <"):
                stdlib_includes.append(include_path)

    user_includes.sort()
    stdlib_includes.sort()

    with open(file_path, 'w') as file:
        for include in user_includes:
            file.write(f'#include "{include}"\n')
        file.write('\n')
        for include in stdlib_includes:
            file.write(f'#include <{include}>\n')


def main():
    args = sys.argv
    [process_file(i) for i in args if is_c_or_cpp_file(i)]

if __name__ == "__main__":
    main()