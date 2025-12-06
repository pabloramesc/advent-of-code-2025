from math import prod

ProblemType = tuple[str, list[int]]  # operator code + list of numbers


def worksheet_to_problems(txt: str):
    lines = [line.split() for line in txt.splitlines()]

    nprobs = len(lines[0])
    for line in lines:
        if len(line) != nprobs:
            raise ValueError("All lines must have same number of elements.")

    problems: list[ProblemType] = []
    for k in range(nprobs):
        numbers = [int(line[k]) for line in lines[:-1]]
        operator = lines[-1][k]
        problem = (operator, numbers)
        problems.append(problem)

    return problems


def solve_problem(problem: ProblemType):
    operator, numbers = problem
    if operator == "+":
        return sum(numbers)
    elif operator == "*":
        return prod(numbers)
    else:
        raise ValueError(f"Not valid operator '{operator}'.")


if __name__ == "__main__":

    with open("day6_input.txt", "r") as file:
        txt = file.read()

    problems = worksheet_to_problems(txt)

    total = 0
    for problem in problems:
        total += solve_problem(problem)

    print("The grand total is", total)
