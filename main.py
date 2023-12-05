import sys
import os

def is_c_or_cpp_file(file_path):
    _, file_extension = os.path.splitext(file_path)
    return file_extension.lower() in ['.c', '.cpp', '.h', '.hpp']

def process_file(file_path):
    important_lines = []
    user_includes = []  
    stdlib_includes = []  
    other_code_lines = [] 

    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        if any([line.startswith(i) for i in ["#pragma", "#define", "#ifndef"]]):
            important_lines.append(line)
        elif line.startswith("#include"):
            include_path = line.split()[1].strip('"<>')
            if line.startswith("#include \""):
                user_includes.append(include_path)
            elif line.startswith("#include <"):
                stdlib_includes.append(include_path)
        else:
            other_code_lines.append(line)

    user_includes.sort()
    stdlib_includes.sort()

    with open(file_path, 'w') as file:
        for line in important_lines:
            file.write(line)
        for include in user_includes:
            file.write(f'#include "{include}"\n')
        if user_includes:
            file.write('\n')
        for include in stdlib_includes:
            file.write(f'#include <{include}>\n')
        for line in other_code_lines:
            file.write(line)

def main():
    args = sys.argv
    [process_file(i) for i in args if is_c_or_cpp_file(i)]

if __name__ == "__main__":
    main()