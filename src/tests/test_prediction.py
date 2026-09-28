import numpy as np
from sklearn.linear_model import LogisticRegression


def test_prediction_output():

    X = np.array([
        [1, 2],
        [2, 3],
        [3, 4],
        [4, 5]
    ])

    y = [0, 0, 1, 1]

    model = LogisticRegression()
    model.fit(X, y)

    prediction = model.predict([[5, 6]])

    assert prediction.shape == (1,)
    assert prediction[0] in [0, 1]