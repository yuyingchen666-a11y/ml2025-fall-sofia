# module7_knn-regr-scikit.py

import numpy as np
from sklearn.neighbors import KNeighborsRegressor

# --- Step 1: Read N (number of points) ---
N = int(input("Enter N (number of training points): "))

# --- Step 2: Read k ---
k = int(input("Enter k (for k-NN Regression): "))

# Error if k > N
if k > N:
    print("Error: k cannot be greater than N.")
    exit()

# --- Step 3: Read the N training points ---
print(f"Enter {N} points (x and y values):")

X_train = np.zeros((N, 1))   # N rows, 1 column for x
y_train = np.zeros(N)        # N labels for y

for i in range(N):
    x_val = float(input(f"Point {i+1} - x: "))
    y_val = float(input(f"Point {i+1} - y: "))

    X_train[i] = x_val
    y_train[i] = y_val

# --- Step 4: Ask user for X to predict ---
X_test_val = float(input("Enter X value to predict Y: "))
X_test = np.array([[X_test_val]])

# --- Step 5: Variance of labels ---
label_variance = np.var(y_train)
print(f"Variance of labels (y): {label_variance}")

# --- Step 6: Build and run k-NN Regression ---
model = KNeighborsRegressor(n_neighbors=k, metric='euclidean')
model.fit(X_train, y_train)

prediction = model.predict(X_test)

# --- Step 7: Output result ---
print(f"k-NN Regression prediction for X = {X_test_val}: {prediction[0]}")
