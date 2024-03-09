from aipys_analyse.simulation.runSimulation import runSimulation
import pandas as pd
def main():
    df = runSimulation(targetNum = 10, geneNum = 300, effectSgRNA = 4,getData = True, mu = 10, a = 0.1,low = 1, high = 5,size = 10_000,FalseLimits = (0.01,0.5),ObservationNum = (10,3))
    print(df)
if __name__ == "__main__":
    main()