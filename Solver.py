class Solver:
    name = ""
    difficulty = ""
    techniques = []
    source = ""
    description = ""
    
    def solve(self):
        raise NotImplementedError
    
    def simulate(self, n=100000):
        raise NotImplementedError

    def verify(self, n=100000, tolerance = 0.1):
        analytical = self.solve();
        simulated = self.simulate();
        error = abs(analytical - simulated)
        passed = error < tolerance
        print(f"{'PASSED' if passed else 'FAILED'}")
        print(f"Expected value: \t{analytical}")
        print(f"Simulated value: \t{simulated}")
        print(f"Error: \t{error}")
        return passed
