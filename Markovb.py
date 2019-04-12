"""
This is a module for creating Markov Chains.
(This is the module docstring)
This is also a multi-line string becasue it has triple quotes.

>>> m = Markov('ab')        
>>> m.predict('a) 'b'      # method

>>>get_table('ab')     # function 
{'a': {'b': 2}}


"""
import random
import urllib.request as req


def fetch_book(url, filename, encoding='utf8'):
    fin = req.urlopen(url)
    fout = open(filename, 'w', encoding=encoding)
    fout.write(fin.read().decode(encoding))
    fout.close()

class Markov:
    def __init__(self, data):
        self.table = get_table(data)

    def predict(self, data_in):
        options = self.table.get(data_in, {})
        if not options:
          #  raise KeyError(f'{data_in} not in training set')
            raise KeyError('{} not in training set'.format(data_in))
        possible = []
        for item in options.items():
            key = item[0]
            value = item[1]
            for i in range(value):
                possible.append(key)
            return random.choice(possible)
        


def get_table(line):
    results = {}
    for i in range(len(line)):
        char = line[i]
        try:
            out = line[i+1]
        except IndexError:
            break
        char_dict = results.get(char, {})
        char_dict.setdefault(out, 0)
        char_dict[out] += 1
        results[char] = char_dict
    return results

def add(x, y):
    return x+y

m = Markov('hello World')
        
