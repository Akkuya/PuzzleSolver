# PuzzleSolver

A growing library of quant finance probability puzzles — each with an analytical solution, a Monte Carlo simulation, and a verifier that checks they agree.

Built as interview prep for quant roles. The point isn't to memorize solutions — it's to understand them deeply enough to implement them from scratch.

## Structure

```bash
PuzzleSolver/
    cli.py              # entry point — run this
    Solver.py           # base class all problems inherit from
    registry.py         # auto-discovers all problems via __subclasses__()
    problems/
        __init__.py     # imports all problem files
        expectation.py  # probability / expectation problems
```

## How it works

Every problem is a class that inherits from `Solver` and implements three methods:

- `solve()` — returns the exact analytical answer
- `simulate(n)` — runs `n` Monte Carlo trials and returns the empirical answer
- `verify()` — calls both and checks they agree within tolerance

```python
class RollingTheBullet(Solver):
    name = "Rolling The Bullet"
    difficulty = "Easy"
    techniques = ["conditional_probability"]
    source = "https://brainstellar.com/puzzles/easy/1"

    def solve(self):
        return 1/4

    def simulate(self, n=100000):
        ...
```

The simulation is written independently from the math — it's a dumb brute-force version of the problem. If `verify()` passes, the derivation is correct. If it fails, there's a bug in the math.

## Running

```bash
python cli.py
```

Pick a problem from the list, see the description, and watch it verify.

## Adding a problem

1. Add a new class to the relevant file in `problems/` (or create a new file)
2. Inherit from `Solver`, fill in the class attributes, implement `solve()` and `simulate()`
3. If you created a new file, add one line to `problems/__init__.py`:
  
   ```python
   from .yourfile import *
   ```

4. Done — `registry.py` picks it up automatically via `Solver.__subclasses__()`

## Problem metadata

Every problem class carries:

| Attribute | Description |
| --- | --- |
| `name` | Display name |
| `difficulty` | Easy / Medium / Hard |
| `techniques` | List of techniques used e.g. `["markov_chain", "recurrence"]` |
| `source` | Link to original problem |
| `description` | Full problem statement |
| `intuition` | Key insight that unlocks the solution |

## Techniques

Problems are tagged by the technique needed to solve them:

- `conditional_probability` — Bayes, conditioning on known information
- `markov_chain` — state-based recurrence, hitting times, steady state
- `recurrence` — linear recurrences, characteristic equation
- `expectation` — linearity of expectation, indicator variables
- `first_step_analysis` — write E[T] in terms of itself, solve
- `symmetry` — collapse cases using structural symmetry
- `generating_functions` — heavier machinery for distributions and counting

## Resources

- *A Practical Guide to Quantitative Finance Interviews* — Xinfeng Zhou (the green book)
- *A First Course in Probability* — Sheldon Ross (prerequisite theory)
- [Brainstellar](https://brainstellar.com) — problem source
- [Jane Street Puzzles](https://www.janestreet.com/puzzles/) — harder targets
