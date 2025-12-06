from day6_part1 import ProblemType, solve_problem


def worksheet_to_problems(txt: str):
    lines = txt.splitlines()

    # Get colum sizes based on operator line (last line) spaces
    colums: list[tuple[str, int]] = []  # operator code + colum size
    operator, size = "", 0
    for c in lines[-1]:
        if c != " ":
            if operator != "":
                colums.append((operator, size - 1))  # remove extra space
            operator = c
            size = 0
        size += 1
    colums.append((operator, size))  # save last colum

    # Process colums into problems
    problems: list[ProblemType] = []
    cursor = 0
    for colum in colums:
        operator, size = colum

        # Get digits for current colum
        digits_matrix = [
            [digit for digit in line[cursor : cursor + size]] for line in lines[:-1]
        ]

        # Build numbers by transposing digits matrix
        numbers = [
            int("".join([row[i] for row in digits_matrix]))
            for i in range(len(digits_matrix[0]))
        ]

        problems.append((operator, numbers))
        cursor += size + 1

    return problems


if __name__ == "__main__":

    with open("day6_input.txt", "r") as file:
        txt = file.read()

    problems = worksheet_to_problems(txt)

    total = 0
    for problem in problems:
        total += solve_problem(problem)

    print("The grand total is", total)
