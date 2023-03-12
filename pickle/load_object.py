import pickle

# open the file containing the serialized Python object using 'rb' mode
with open('pickle\\data.pickle', 'rb') as file:
    # use pickle.load() to deserialize the Python object from the file
    data = pickle.load(file)
    # print the deserialized object
    print(data)