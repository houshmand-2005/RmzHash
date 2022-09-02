import random as random
randnum = random.randint(12, 100)
dic_all_alfa = {
    # you can generate keys by randomazer_hash.py in repository
    # "your key":your value must *int* and lenght of values must be *11*. like ==> 'a' : 12345678910,
    '\n': 'ADD KEY HERE IN NUM',  # like '\n': 23617535821
    '+': 'ADD KEY HERE IN NUM',
    "'": 'ADD KEY HERE IN NUM',
    ':': 'ADD KEY HERE IN NUM',
    '/': 'ADD KEY HERE IN NUM',
    ',': 'ADD KEY HERE IN NUM',
    '?': 'ADD KEY HERE IN NUM',
    '!': 'ADD KEY HERE IN NUM',
    ')': 'ADD KEY HERE IN NUM',
    '(': 'ADD KEY HERE IN NUM',
    '.': 'ADD KEY HERE IN NUM',
    'a': 'ADD KEY HERE IN NUM',
    'b': 'ADD KEY HERE IN NUM',
    'c': 'ADD KEY HERE IN NUM',
    'd': 'ADD KEY HERE IN NUM',
    'e': 'ADD KEY HERE IN NUM',
    'f': 'ADD KEY HERE IN NUM',
    'g': 'ADD KEY HERE IN NUM',
    'h': 'ADD KEY HERE IN NUM',
    'i': 'ADD KEY HERE IN NUM',
    'j': 'ADD KEY HERE IN NUM',
    'k': 'ADD KEY HERE IN NUM',
    'l': 'ADD KEY HERE IN NUM',
    'm': 'ADD KEY HERE IN NUM',
    'n': 'ADD KEY HERE IN NUM',
    'o': 'ADD KEY HERE IN NUM',
    'p': 'ADD KEY HERE IN NUM',
    'q': 'ADD KEY HERE IN NUM',
    'r': 'ADD KEY HERE IN NUM',
    's': 'ADD KEY HERE IN NUM',
    't': 'ADD KEY HERE IN NUM',
    'u': 'ADD KEY HERE IN NUM',
    'v': 'ADD KEY HERE IN NUM',
    'w': 'ADD KEY HERE IN NUM',
    'x': 'ADD KEY HERE IN NUM',
    'y': 'ADD KEY HERE IN NUM',
    'z': 'ADD KEY HERE IN NUM',
    'A': 'ADD KEY HERE IN NUM',
    'B': 'ADD KEY HERE IN NUM',
    'C': 'ADD KEY HERE IN NUM',
    'D': 'ADD KEY HERE IN NUM',
    'E': 'ADD KEY HERE IN NUM',
    'F': 'ADD KEY HERE IN NUM',
    'G': 'ADD KEY HERE IN NUM',
    'H': 'ADD KEY HERE IN NUM',
    'I': 'ADD KEY HERE IN NUM',
    'J': 'ADD KEY HERE IN NUM',
    'K': 'ADD KEY HERE IN NUM',
    'L': 'ADD KEY HERE IN NUM',
    'M': 'ADD KEY HERE IN NUM',
    'N': 'ADD KEY HERE IN NUM',
    'O': 'ADD KEY HERE IN NUM',
    'P': 'ADD KEY HERE IN NUM',
    'Q': 'ADD KEY HERE IN NUM',
    'R': 'ADD KEY HERE IN NUM',
    'S': 'ADD KEY HERE IN NUM',
    'T': 'ADD KEY HERE IN NUM',
    'U': 'ADD KEY HERE IN NUM',
    'V': 'ADD KEY HERE IN NUM',
    'W': 'ADD KEY HERE IN NUM',
    'X': 'ADD KEY HERE IN NUM',
    'Y': 'ADD KEY HERE IN NUM',
    'Z': 'ADD KEY HERE IN NUM',
    ' ': 'ADD KEY HERE IN NUM',
    '1': 'ADD KEY HERE IN NUM',
    '2': 'ADD KEY HERE IN NUM',
    '3': 'ADD KEY HERE IN NUM',
    '4': 'ADD KEY HERE IN NUM',
    '5': 'ADD KEY HERE IN NUM',
    '6': 'ADD KEY HERE IN NUM',
    '7': 'ADD KEY HERE IN NUM',
    '8': 'ADD KEY HERE IN NUM',
    '9': 'ADD KEY HERE IN NUM',
    '0': 'ADD KEY HERE IN NUM'
}


class manager:
    def runtest(self, listtotest):
        """
        test keys has a duplicates
        """
        return len(listtotest) != len(set(listtotest.values()))

    def giveAprammter(self, prammter):
        """
        give you the key of the alfa you Enter
        """
        dic_all_alfa_rand = dic_all_alfa
        code_of_alfa = dic_all_alfa_rand[prammter]
        return code_of_alfa

    def needAll(self):
        """ give the list of alfa and with keys"""
        return dic_all_alfa

    def has_duplicates_rand(self, randnum, bnnum):
        """ 
        This func can find out if our keys are use before tell you True or False
        """
        keys_nn = {}
        n = 0
        for alfa in mang_command.needAll():
            keys_nn[n] = mang_command.giveAprammter(alfa) + bnnum + randnum
            n = n + 1
        # print(keys_nn)
        HasDup = len(keys_nn) != len(set(keys_nn.values()))
        return HasDup


mang_command = manager()
