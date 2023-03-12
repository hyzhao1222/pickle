import pickle
from sklearn.linear_model import LinearRegression

# create a LinearRegression model and fit it to some data
model = LinearRegression()
X = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
y = [10, 20, 30]
model.fit(X, y)

# save the trained model to a file using 'wb' mode
with open('pickle\\model.pickle', 'wb') as file:
    pickle.dump(model, file)

# load the saved model from the file using 'rb' mode
with open('pickle\\model.pickle', 'rb') as file:
    loaded_model = pickle.load(file)

# use the loaded model to make predictions
X_new = [[1, 2, 3], [4, 5, 6]]
y_pred = loaded_model.predict(X_new)
print(y_pred)