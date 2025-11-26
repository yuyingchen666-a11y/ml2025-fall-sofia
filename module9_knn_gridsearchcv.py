import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score

N = int(input())

X_train = []
y_train = []

for _ in range(N):
    x = float(input())
    y = int(input())
    X_train.append([x])
    y_train.append(y)

X_train = np.array(X_train)
y_train = np.array(y_train)

M = int(input())

X_test = []
y_test = []

for _ in range(M):
    x = float(input())
    y = int(input())
    X_test.append([x])
    y_test.append(y)

X_test = np.array(X_test)
y_test = np.array(y_test)

param_grid = {'n_neighbors': list(range(1, 11))}
knn = KNeighborsClassifier()
grid_search = GridSearchCV(knn, param_grid, cv=3)
grid_search.fit(X_train, y_train)

best_k = grid_search.best_params_['n_neighbors']
best_model = grid_search.best_estimator_

y_pred = best_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(best_k)
print(accuracy)
