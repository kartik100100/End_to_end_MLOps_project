import pandas as pd


def test_dataset_exists():
    df = pd.read_csv('notebook/data/student.csv')

    assert df is not None
    assert len(df) > 0


def test_dataset_has_columns():
    df = pd.read_csv('artifacts/test.csv')

    assert len(df.columns) > 0