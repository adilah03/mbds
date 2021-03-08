### Question 3 ###

# needed to load input files as data table
import pandas as pd
train_data = pd.read_table('./train_data.txt', delimiter='\t')
train_truth = pd.read_table('./train_truth.txt', delimiter='\t')
train_truth = train_truth.values.ravel()
test_data = pd.read_table('./test_data.txt')

# import function for MLP and cross-validation
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import GridSearchCV

# create mlp with 4x4 hidden layers
mlp = MLPRegressor(hidden_layer_sizes=[4,4])
# run cross-validation (with 10 folds) to find the best parameters for our model
param_grid = {
    'activation': ['tanh', 'relu'],
    'solver': ['sgd', 'adam'],
    'alpha': [0.0001, 0.0005, 0.01, 0.05, 0.1, 0.5, 1, 5],
    'learning_rate': ['constant', 'adaptive'],
 }
kcv = GridSearchCV(mlp, param_grid, cv=10)

# fit the best model found, i.e., select parameters with the lowest cv errors
kcv.fit(train_data, train_truth)
# use this model to predict y values for the given x values
test_predicted = kcv.predict(test_data)
print('y')
for y in test_predicted:
    print(y)