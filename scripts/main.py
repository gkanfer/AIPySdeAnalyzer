from aipys_analyse.simulation.runSimulation import runSimulation
import pandas as pd
def main():
    df = runSimulation(targetNum = 3, geneNum = 2000, effectSgRNA = 4,getData = True, mu = 20, a = 1.2,low = 1, high = 3,size = 100_000,FalseLimits = (0.6,0.9),ObservationNum = (3000,300))
    print(df)
if __name__ == "__main__":
    main()