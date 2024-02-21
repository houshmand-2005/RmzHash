import random

UseRandomKey = True  # if you want to Use the random key on keep it True
alfa_dic = {
    # normally if UseRandomKey variable is True the values generate randomly
    # "your_key": your value must *int*,
    "\n": "ADD KEY HERE IN NUM",  # like '\n': 23617535821
    "\r": "ADD KEY HERE IN NUM",
    "-": "ADD KEY HERE IN NUM",
    "_": "ADD KEY HERE IN NUM",
    '"': "ADD KEY HERE IN NUM",
    "~": "ADD KEY HERE IN NUM",
    "`": "ADD KEY HERE IN NUM",
    "+": "ADD KEY HERE IN NUM",
    "'": "ADD KEY HERE IN NUM",
    ":": "ADD KEY HERE IN NUM",
    "\\": "ADD KEY HERE IN NUM",
    "/": "ADD KEY HERE IN NUM",
    ",": "ADD KEY HERE IN NUM",
    "?": "ADD KEY HERE IN NUM",
    "!": "ADD KEY HERE IN NUM",
    ")": "ADD KEY HERE IN NUM",
    "(": "ADD KEY HERE IN NUM",
    ".": "ADD KEY HERE IN NUM",
    "a": "ADD KEY HERE IN NUM",
    "b": "ADD KEY HERE IN NUM",
    "c": "ADD KEY HERE IN NUM",
    "d": "ADD KEY HERE IN NUM",
    "e": "ADD KEY HERE IN NUM",
    "f": "ADD KEY HERE IN NUM",
    "g": "ADD KEY HERE IN NUM",
    "h": "ADD KEY HERE IN NUM",
    "i": "ADD KEY HERE IN NUM",
    "j": "ADD KEY HERE IN NUM",
    "k": "ADD KEY HERE IN NUM",
    "l": "ADD KEY HERE IN NUM",
    "m": "ADD KEY HERE IN NUM",
    "n": "ADD KEY HERE IN NUM",
    "o": "ADD KEY HERE IN NUM",
    "p": "ADD KEY HERE IN NUM",
    "q": "ADD KEY HERE IN NUM",
    "r": "ADD KEY HERE IN NUM",
    "s": "ADD KEY HERE IN NUM",
    "t": "ADD KEY HERE IN NUM",
    "u": "ADD KEY HERE IN NUM",
    "v": "ADD KEY HERE IN NUM",
    "w": "ADD KEY HERE IN NUM",
    "x": "ADD KEY HERE IN NUM",
    "y": "ADD KEY HERE IN NUM",
    "z": "ADD KEY HERE IN NUM",
    "A": "ADD KEY HERE IN NUM",
    "B": "ADD KEY HERE IN NUM",
    "C": "ADD KEY HERE IN NUM",
    "D": "ADD KEY HERE IN NUM",
    "E": "ADD KEY HERE IN NUM",
    "F": "ADD KEY HERE IN NUM",
    "G": "ADD KEY HERE IN NUM",
    "H": "ADD KEY HERE IN NUM",
    "I": "ADD KEY HERE IN NUM",
    "J": "ADD KEY HERE IN NUM",
    "K": "ADD KEY HERE IN NUM",
    "L": "ADD KEY HERE IN NUM",
    "M": "ADD KEY HERE IN NUM",
    "N": "ADD KEY HERE IN NUM",
    "O": "ADD KEY HERE IN NUM",
    "P": "ADD KEY HERE IN NUM",
    "Q": "ADD KEY HERE IN NUM",
    "R": "ADD KEY HERE IN NUM",
    "S": "ADD KEY HERE IN NUM",
    "T": "ADD KEY HERE IN NUM",
    "U": "ADD KEY HERE IN NUM",
    "V": "ADD KEY HERE IN NUM",
    "W": "ADD KEY HERE IN NUM",
    "X": "ADD KEY HERE IN NUM",
    "Y": "ADD KEY HERE IN NUM",
    "Z": "ADD KEY HERE IN NUM",
    " ": "ADD KEY HERE IN NUM",
    "1": "ADD KEY HERE IN NUM",
    "2": "ADD KEY HERE IN NUM",
    "3": "ADD KEY HERE IN NUM",
    "4": "ADD KEY HERE IN NUM",
    "5": "ADD KEY HERE IN NUM",
    "6": "ADD KEY HERE IN NUM",
    "7": "ADD KEY HERE IN NUM",
    "8": "ADD KEY HERE IN NUM",
    "9": "ADD KEY HERE IN NUM",
    "0": "ADD KEY HERE IN NUM",
}
START_NUM = 10000000001
END_NUM = 99578000011


class Manager:
    """create random keys and check the duplicate test!"""

    # with this the keys changed for each user
    def set_seed(self, seed_number: int) -> dict | None:
        """create random keys for values
        Input:
            - seed_number : int
        Output:
            - random_dic_all_alfa : dict | None
        """

        if UseRandomKey:
            random.seed(int(seed_number))
            random_dic_all_alfa = {
                alfa: random.randint(START_NUM, END_NUM) for alfa in alfa_dic
            }
            dup = self.duplicate_test(random_dic_all_alfa)
            return random_dic_all_alfa if dup else None
        return None

    def duplicate_test(self, alfa_dic_test: dict) -> bool:
        """Test keys has a duplicates or not!
        Input:
            - alfa_dic_test : dict
        Output:
            - bool
        """
        return len(alfa_dic_test) == len(set(alfa_dic_test.values()))
