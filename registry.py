import problems
from Solver import Solver

ALL_PROBLEMS = Solver.__subclasses__()

BY_NAME = {p.name: p for p in ALL_PROBLEMS}

BY_TECHNIQUE = {}
for p in ALL_PROBLEMS:
    for t in p.techniques:
        BY_TECHNIQUE.setdefault(t, []).append(p)