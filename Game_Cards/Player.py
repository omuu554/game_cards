from DeckOfCards import DeckOfCards
from Card import Card
import random
class Player:

    def __init__(self,PlayerName:str = "GuestPlayer", PlayerDeckStartSize:int = 26):
        PlayerDeckSize = self.__PlayerDeckSizeNotInteger(PlayerDeckStartSize)
        PlayerDeckSize = self.__PlayerDeckSizeBad(PlayerDeckSize)

        self.PlayerName = str(PlayerName)
        self.DeckSize = PlayerDeckSize
        self.PlayerCards = []

    def __RaiseErrorIfNotDeckOfCards(self, Deck:DeckOfCards):
        if(type(Deck) != DeckOfCards):
            raise TypeError("The Deck you have entered is not of type DeckOfCards")
    def __RaiseErrorIfNotCard(self,card:Card):
        if(type(card) != Card):
            raise TypeError("The card you have entered is not of type Card")
    def __ActionAddCard(self,Card:Card):
        self.PlayerCards.append(Card)

    def __PlayerDeckSizeNotInteger(self, DeckSize:int):
        if(not str(DeckSize).isdigit() or type(DeckSize) != int):
            DeckSize = 26

        return DeckSize

    def __PlayerDeckSizeBad(self, DeckSize:int):
        if(DeckSize < 10 or DeckSize > 26):
            DeckSize = 26

        return DeckSize

    def IsPlayerDeckNotEmpty(self):
        return self.PlayerCards


    def Set_Hand(self, CardsDeck:DeckOfCards):
        self.__RaiseErrorIfNotDeckOfCards(CardsDeck)

        for i in range(self.DeckSize):
            card = CardsDeck.Deal_One()
            if(card is not None):
             self.Add_Card(card)


    def Get_Card(self):
       if(self.IsPlayerDeckNotEmpty()):
        card = random.choice(self.PlayerCards)
        self.PlayerCards.remove(card)
        return card

       return None

    def Add_Card(self, card:Card):
        self.__RaiseErrorIfNotCard(card)
        self.__ActionAddCard(card)




