from registry import BY_NAME, ALL_PROBLEMS

def main():
    for i, problem in enumerate(ALL_PROBLEMS):
        print(f"{i+1}. {problem.name} [{problem.difficulty}]")

    choice = int(input("\npick a problem: ")) - 1
    problem_class = ALL_PROBLEMS[choice]
    instance = problem_class()

    print(f"\n{instance.description}")
    instance.verify()

if __name__ == "__main__":
    main()