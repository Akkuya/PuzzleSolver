from Solver import Solver
import random

class RollingTheBullet(Solver):
    name = "Rolling The Bullet"
    difficulty = "Easy"
    description = """Two bullets are loaded into a gun's round barrel consecutively. 
    The barrel has a capacity of 6. The gun is fired once, but no bullet is shot. 
    Does rolling the barrel (shuffling) before next shot increase the probability of firing a bullet?
    """
    source = "https://brainstellar.com/puzzles/easy/1"

    def solve(self):
        return 1/4

    def simulate(self, n=100000):
        dead = 0
        
        for _ in range(n):
        # place 2 consecutive bullets randomly in 6 chambers
            start = random.randint(0, 5)
            chamber = [0] * 6
            chamber[start % 6] = 1
            chamber[(start + 1) % 6] = 1

            # find an empty chamber (simulating first shot was empty)
            empty_positions = [i for i in range(6) if chamber[i] == 0]
            first_shot = random.choice(empty_positions)

            # next chamber is the one right after
            next_shot = (first_shot + 1) % 6
            dead += chamber[next_shot]

        return dead / n


            