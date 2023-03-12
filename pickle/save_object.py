import pickle

# create a Python object to save
data = {'name': 'John', 'age': 30, 'gender': 'male'}

# open a file to write binary data using 'wb' mode
with open('pickle\\data.pickle', 'wb') as file:
    # use pickle.dump() to serialize the Python object and write it to the file
    pickle.dump(data, file)