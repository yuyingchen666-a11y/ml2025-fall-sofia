# module8_metrics-scikit.py

import numpy as np
from sklearn.metrics import precision_score, recall_score

def main():
    # Read number of points
    N = int(input("Enter N (number of points): "))

    # Initialize arrays using numpy
    X = np.zeros(N, dtype=int)  # ground truth
    Y = np.zeros(N, dtype=int)  # predicted

    # Read (x, y) points
    print("Enter the points (x as ground truth, y as predicted). Values must be 0 or 1.")
    for i in range(N):
        x_val = int(input(f"Point {i+1} - x: "))
        y_val = int(input(f"Point {i+1} - y: "))
        X[i] = x_val
        Y[i] = y_val

    # Compute precision & recall
    precision = precision_score(X, Y, zero_division=0)
    recall = recall_score(X, Y, zero_division=0)

    # Output the results
    print("Precision:", precision)
    print("Recall:", recall)

if __name__ == "__main__":
    main()
