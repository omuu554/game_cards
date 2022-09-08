from Card import Card
from CardGame import CardGame

def ActionsOnRoundWinner(card1:Card, card2:Card,cardGame:CardGame):

    if (card1 > card2):
        cardGame.Player1.Add_Card(card1)
        cardGame.Player1.Add_Card(card2)
        print(f"\n{cardGame.Player1.PlayerName} won in: {card1} vs {card2}\n")
    else:
        cardGame.Player2.Add_Card(card1)
        cardGame.Player2.Add_Card(card2)
        print(f"\n{cardGame.Player2.PlayerName} won in: {card2} vs {card1}\n")

def CardGameManager(cardGame:CardGame):
    print(f"Player: {cardGame.Player1.PlayerName}\nCards: {cardGame.Player1.PlayerCards}\n")
    print(f"Player: {cardGame.Player2.PlayerName}\nCards: {cardGame.Player2.PlayerCards}\n")
    Round = 0
    for Round in range(10):
        p1Card = cardGame.Player1.Get_Card()
        p2Card = cardGame.Player2.Get_Card()
        Round += 1
        print(f"\nRound: {Round}")
        print(f"(Player: {cardGame.Player1.PlayerName} | card: {p1Card})       vs       (Player: {cardGame.Player2.PlayerName} | card: {p2Card})\n")
        ActionsOnRoundWinner(p1Card, p2Card, cardGame)
        # if(p1Card > p2Card ): # THE FUNCTION ABOVE DOES THE SAME THING
        #     cardGame.Player1.Add_Card(p1Card)
        #     cardGame.Player1.Add_Card(p2Card)
        #     print(f"\n{cardGame.Player1.PlayerName} won in: {p1Card} vs {p2Card}\n")
        # else:
        #     cardGame.Player2.Add_Card(p1Card)
        #     cardGame.Player2.Add_Card(p2Card)
        #     print(f"\n{cardGame.Player2.PlayerName} won in: {p1Card} vs {p2Card}\n")

    return cardGame.Get_Winner()


if __name__ == "__main__":
    playerName1 = input("Please enter the name of the first player: ")
    playerName2 = input("Please enter the name of the second player: ")

    playerDeckSize = input("Please enter an integer for the decksize of the first player (10-26): ")

    cardGame = CardGame(playerName1, playerName2, playerDeckSize)
    GameWinner = CardGameManager(cardGame)

    if(GameWinner is not None):
     print(f"\nThe player that won is \n{GameWinner}")
    else:
     print(f"Its a tie no one won")



