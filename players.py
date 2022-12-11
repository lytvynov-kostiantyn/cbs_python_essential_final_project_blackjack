from abc import abstractmethod, ABC


class AbstractPlayer(ABC):
    def __init__(self, name, bank):
        self.name = name
        self.bank = bank

    @abstractmethod
    def get_card(self):
        pass


class Player(AbstractPlayer):
    def get_card(self):
        pass


class Bot(AbstractPlayer):
    def get_card(self):
        pass
