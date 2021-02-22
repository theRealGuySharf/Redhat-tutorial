import re
import argparse
import sys


class Colors:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    END = '\33[0m'


def get_params():
    """parse CLI arguments
     Raises ArgumentError if user asks for both color and machine or a non-supported color"""
    args = parser.parse_args()
    if args.color and args.machine:
        error = "--color and --machine are mutually exclusive, please choose only one.\n"
        sys.stderr.write(f"ArgumentError: {error}")
        exit(2)
    if args.color:
        try:
            getattr(Colors, args.color.upper())
        except AttributeError:
            error = f"Unsupported color: {args.color}"
            sys.stderr.write(f"AttributeError: {error}")
            exit(3)
    return args


def find_pattern(pattern, file_name, lines):
    """Find the specified pattern and send to printout."""
    p = re.compile(pattern)
    for index, line in enumerate(lines):
        matches = p.finditer(line)
        for match in matches:
            print_result(file_name, index, match.start(), match.group(0))


def print_result(file_name, line_no, start_pos, match):
    """print results based on user preference (human vs machine)"""
    if params.machine:
        print_machine(file_name, line_no, start_pos, match)
    else:
        if params.color:
            print_with_color(match, file_name, line_no)
        else:
            print_human(match, file_name, line_no)


def print_machine(file_name, line_no, start_pos, match):
    sys.stdout.write(f"{file_name}:{line_no}:{start_pos}:{match}\n")


def print_human(match, file_name, line_no):
    sys.stdout.write(f"Found match {match} in file {file_name}, line no {line_no}")


def print_with_color(match, file_name, line_no):
    sys.stdout.write(f"{getattr(Colors, params.color.upper())}")
    print_human(match, file_name, line_no)
    sys.stdout.write(f"{Colors.END}\n")


parser = argparse.ArgumentParser(description="Find a specified pattern in a list of given files.")
parser.add_argument("-p", "--pattern", action="store", help="Pattern to look for.")
parser.add_argument("-f", "--files", nargs="+", help="path(s) to file(s) to find pattern in.")
parser.add_argument("-c", "--color", action="store", help="Colored output (Black,Red,Green,Yellow,Blue,Magenta,Cyan)")
parser.add_argument("-m", "--machine", action="store_true", default=False,
                    help="prints in machine-readable format: file_name:no_line:start_pos:matched_text")


def main():
    global params
    params = get_params()
    files_lines = []
    for file in params.files:
        with open(file, "r") as f:
            files_lines.append({"file_name": file, "lines": f.readlines()})

    for file in files_lines:
        find_pattern(params.pattern, file["file_name"], file["lines"])


if __name__ == '__main__':
    main()
