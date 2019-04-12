#from markov import markov
import markov
import unittest


class TestMarkov(unittest.TestCase):
    def test_markov(self):
        m = markov.Markov('ab')
        res = m.predict('a')
        self.assertEqual(res, 'b')

    def test_markov2(self):
        m = markov.Markov('abc', size=2)
        res = m.predict('ab')
        self.assertEqual(res, 'c')

    def test_word_makov(self):
        m = markov.WordMarkov(['Hello', 'World'])
        res = m.predict('Hello')
        self.assertEqual(res, 'World')

    def test_get_table(self):
        res = markov.get_table('ab')
        self.assertEqual(res, {'a': {'b':1}})

    def test_get_table2(self):
        res = markov.get_table('abc', size=2)
        self.assertEqual(res, {'ab': {'c':1}})

    def test_get_table_word(self):
        #import pdb; pdb.set_trace()
        res = markov.get_table(['Hello', 'World'])
        self.assertEqual(res, {'Hello': {'World':1}})



if __name__ == '__main__':
    unittest.main()
