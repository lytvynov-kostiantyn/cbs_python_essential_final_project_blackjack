# Final project for Python Essential
## Blackjack on Python

---
### Description:

---
### Rules:
* The game uses one card deck, which updates after each deal.
* Five players can participate in the game (the user sets the parameter at the start).
* The minimum size of a player's bank is 5$
* Minimal bet is 1$
* Maximum bet equal to player bank.
* Cards points:
    * Ace is 11 points if a player or dealer gets more than 21, values are changed by 1 point.
    * King, Queen, Jack is 10 points.
    * Cards from 10 to 2 get points according to their face value.
* On the first hand, each player receives 2 cards, the dealer receives 1 card.
* If the player gets 21 on the first two cards, then he has blackjack, and:
    * If the dealer has less than 10 points on the first card. The player receives his bet back and additionally the amount of his bet with a coefficient of 1.5.
    * If the dealer has 10 or 11 points on the first card. The player has a choice. He can return his bet and get a win equal to his stake, or wait until the end of the hand and get a win equal to the amount of his bet with a coefficient of 1.5.
* If the player, after receiving additional cards, gets more than 21, he immediately loses his bet and leaves the game.
* The dealer must take cards until his points are greater than or equal to 17.


---
### Under the hood:
`main.py` - the file that launches the game process with user-defined parameters.

`const.py` - small game database with constant values and frequently used functions.

`cards.py` - the file describes the class of a card and the class of a deck of cards.

`players.py` - the file describes the classes of player, bot, and dealer.

`game.py` - the file contains the class that describes the game process.