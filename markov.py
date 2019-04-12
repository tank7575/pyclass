"""
This is a module for creating Markov Chains.
(This is the module docstring)
This is also a multi-line string becasue it has triple quotes.

>>> m = Markov('ab')        
>>> m.predict('a) 'b'      # method

>>>get_table('ab')     # function 
{'a': {'b': 2}}


"""
import argparse
import random
import urllib.request as req
import sys


def fetch_book(url, filename, encoding='utf8'):
    fin = req.urlopen(url)
    fout = open(filename, 'w', encoding=encoding)
    fout.write(fin.read().decode(encoding))
    fout.close()

class Markov:
    joiner = ' '
    def __init__(self, data, size=1):
        #self.table = get_table(data)
        self.tables = []
        for i in range(1, size+1):
            self.tables.append(get_table(data, size=i))
        self.size = size

    def _get_table(self,data_in):
        #print(f"data in: {data_in}")
        table = self.tables[len(data_in) - 1]
        return table

    def predict(self, data_in):
        #options = self.table.get(data_in, {})
        table = self._get_table(data_in)
        options = table.get(data_in, {})
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

    def lorem(self, start, length):
        res = [start]
        for i in range(length):
            seed = self.joiner.join(res[-self.size:])
            out = self.predict(seed)
            res.append(out)
        return self.joiner.join(res)               


class WordMarkov(Markov):
    def __init__(self, data_in, size=1):
        if isinstance(data_in, str):
            data_in = data_in.split()
        super().__init__(data_in,size)
    
    def _get_table(self, data_in):
        for table in self.tables:
            if data_in in table:
                return table              
        


def get_table(line, size=1):
    results = {}
    for i in range(len(line)):
        chars = line[i:i+size]
        try:
            out = line[i+size]
        except IndexError:
            break
        if isinstance(chars, list):
            chars = ' '.join(chars)
        char_dict = results.get(chars, {})
        char_dict.setdefault(out, 0)
        char_dict[out] += 1
        results[chars] = char_dict
    return results

def repl(m):
    while True:
        try:
            txt = input('>')
        except EOFError:
            print("goodbye!")
            break
        try:
            res = m.predict(txt)
        except AttributeError:
            print("Try again")
        else:
            print(res)

def add(x, y):
    return x+y

def main(args):
    ap = argparse.ArgumentParser(description='Markov chain generator')
    ap.add_argument('-f', '--file', help='input file')
    ap.add_argument('-e', '--encoding', help='encoding (default utf8)',
                    default='utf8')
    ap.add_argument('-s', '--size', help='size (default 1)',
                    default=1, type=int)
    ap.add_argument('-w', '--word', help='word mode',
                    action='store_true')
    opts = ap.parse_args(args)
    if opts.file:
        with open(opts.file, encoding=opts.encoding) as fin:
            txt = fin.read()
        Klass = Markov
        if opts.word:
            Klass = WordMarkov
        m = Klass(txt, size=opts.size)
        repl(m)
    

if __name__ == '__main__':
    #pass
    #m = Markov('hello World')
    main(sys.argv[1:])
    #m2 = WordMarkov(
     #  open('totc.txt', encoding='utf8').read(),#.split(),
      #  size=4)
        
