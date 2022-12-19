# Final project for Python Essential
## Blackjack(lite) on Python

---
### Description:
This application implements a simpler version of the well-known game "Blackjack". At the beginning of the game, the player is asked to enter his name and the amount which he is willing to risk in this game. After that, the player determines the number of additional players (bots) at the table.
The players place their bets and the game begins. On the first deal, each player receives two cards, the dealer receives one card. If the player gets an ace, he is asked to choose the value of the points of this card (1 or 11). If the player hits blackjack (21 points on two cards) he can prefer to continue playing or pick up the win depending on the dealer's first card. Further, each player can take additional cards at will, if the player scores more than 21 points, he immediately loses his bet. Further, additional cards are taken by the dealer, who is obliged to take cards until he scores 17 or more points.
The final winner is determined according to the rules below.
After the game, the current state of the account of each player is displayed on the screen, bots with a zero balance leave the game.
If the player loses all means the game ends.
If the player has a positive balance, the player is offered to play another game with a new deck of cards.

---
### Rules:
* The game uses one card deck, which updates after each deal.
* Five players can participate in the game (the user sets the parameter at the start).
* The minimum size of a player's bank is 5$
* Minimal bet is 1$
* Maximum bet equal to player bank.
* Cards points:
    * Ace is 11 or 1 point(s) (by player's choice).
    * King, Queen, Jack is 10 points.
    * Cards from 10 to 2 get points according to their face value.
* On the first hand, each player receives 2 cards, the dealer receives 1 card.
* If the player gets 21 on the first two cards, then he has blackjack, and:
    * If the dealer has less than 10 points on the first card. The player receives his bet back and additionally the amount of his bet with a coefficient of 1.5.
    * If the dealer has 10 or 11 points on the first card. The player has a choice. He can return his bet and get a win equal to his stake, or wait until the end of the hand and get a win equal to the amount of his bet with a coefficient of 1.5.
* If the player, after receiving additional cards, gets more than 21, he immediately loses his bet and leaves the game.
* The dealer must take cards until his points are greater than or equal to 17.
* Final results:
    * If the dealer has blackjack, all players who do not have blackjack lose, players with blackjack get their bet back.
    * If the dealer has more than 21, all who are still in the game win 1xbet, players with blackjack win 1.5xbet.
    * If the dealer has 21 or less:
        * If the dealer and player have equal points, it's a draw and the player gets his bet back.
        * If the dealer has more points than the player, the player loses his bet.
        * If the dealer has fewer points than the player, the player wins 1xbet, and players with blackjack win 1.5xbet.
        * If the dealer has 21 points and the player has a blackjack, the player will receive a win equal to 1.5xbet.

---
### Under the hood:
`main.py` - the file that launches the game process.

`const.py` - small game database with constant values.

`cards.py` - the file describes the class of a card and the class of a deck of cards.

`players.py` - the file describes the classes of player, bot, and dealer.

`game.py` - the file contains the class with the game process.