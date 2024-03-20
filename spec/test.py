import pandas as pd
from aipys_analyse.simulation.runSimulation import runSimulation

def test_high_moi(capfd):  # Use pytest's `capfd` fixture for output capturing
    """Tests the scenario with a high MOI (Multiplicity of Infection)."""

    df = runSimulation(
        targetNum=3,
        geneNum=300,
        effectSgRNA=4,
        getData=True,
        mu=20,
        a=1.2,
        low=1,
        high=1,  # High MOI
        size=10_000,
        FalseLimits=(0.6, 0.9),
        ObservationNum=(10, 3),
    )

    # Assert expected behavior or properties of `df` here
    # (Example: assert df.shape[0] > 0, "Dataframe should not be empty")

    captured = capfd.readouterrs()
    assert "High MOI test completed successfully" in captured.out, "Expected success message"

def test_other_edge_case(capfd):  # Add more test functions for other edge cases
    """Tests another edge case scenario."""
    captured = capfd.readouterrs()
    assert "Other edge case test completed successfully" in captured.out, "Expected success message"

if __name__ == "__main__":
    import pytest  # Assuming you're using pytest
    pytest.main()  # Run tests using pytest