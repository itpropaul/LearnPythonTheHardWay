import pickle

a = {'hello': 'world'}

with open('dictionary.pickle', 'wb') as handle:
  pickle.dump(a, handle)

print a

with open('dictionary.pickle', 'rb') as handle:
  b = pickle.load(handle)

print b

print a == b
