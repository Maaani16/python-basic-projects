import random
import string
from abc import ABC, abstractmethod

import nltk

nltk.download("words")


class PasswordGenerator(ABC):
    @abstractmethod
    def generate(self):
        pass


class PinCode(PasswordGenerator):
    def __init__(self, length: int = 8):
        self.length = (
            input("please enter the length of your pin code (default(enter): 8) :") or 8
        )
        self.length = int(self.length)
        self.character = string.digits

    def generate(self) -> str:
        return "".join(random.choice(self.character) for _ in range(self.length))


class RandomPassword(PasswordGenerator):
    def __init__(self):
        self.length = (
            input(
                "please enter the length of your random password : (default(enter): 8) :"
            )
            or 8
        )
        self.length = int(self.length)
        self.character = string.ascii_letters
        self.has_digits = (
            input(
                "Do you want your password to contain numbers? (y/(default(enter): n) )"
            ).lower()
            == "y"
        )
        if self.has_digits:
            self.character += string.digits
        self.has_symbol = (
            input(
                "Do you want your password to contain symbols? (y/(default(enter): n) )"
            ).lower()
            == "y"
        )
        if self.has_symbol:
            self.character += string.punctuation

    def generate(self) -> str:
        return "".join(random.choice(self.character) for _ in range(self.length))


class MemorablePassword(PasswordGenerator):
    def __init__(self):
        self.length = (
            input(
                "please enter the length of your memorable password : (default(enter): 4) :"
            )
            or 4
        )
        self.length = int(self.length)
        self.separator = (
            input(
                "please enter the separator of your memorable password : (default(enter): -) :"
            )
            or "-"
        )
        self.character = nltk.corpus.words.words()

    def generate(self) -> str:
        return "".join(
            (random.choice(self.character) + self.separator) for _ in range(self.length)
        )


if __name__ == "__main__":
    p_code = PinCode()
    print(p_code.generate())
    random_p = RandomPassword()
    print(random_p.generate())
    memorable_p = MemorablePassword()
    print(memorable_p.generate())
