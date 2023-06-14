
# Mancala Board Game Implementation in Python - README





## Table of Contents

1)  [Overview](https://github.com/KavyaKolavasi1/Mancala#overview)

2)  [Player Class](https://github.com/KavyaKolavasi1/Mancala#player-class)

3)  [Mancala Class](https://github.com/KavyaKolavasi1/Mancala#mancala-class)

4) [Output](https://github.com/KavyaKolavasi1/Mancala#output)

4) [Reflection](https://github.com/KavyaKolavasi1/Mancala#reflection)


## Overview
This project is the implementation of the board game Mancala in python. Below we will discuss the game objectives followed by brief description of the implementation of the Player and Mancala classes.

### Game Objective
Mancala, the term which stems from the arabic word meaning"to move", has origin's dating back to 1400 B.C.E. and is played today by many worldwide.

#### Overall Objective: The player with the most seeds in their store wins.
#### Game Play: Each player will take a turn to distribute seeds from their pit. Player will choose a pit and place one seed into each pit moving to their right. Player can place seed into their own store but not corresponding players store. Play is then complete and oponents turn continues.
#### Game Complete: The game is complete once a player has all of their pits empty. Obtain total seed counts in store and player with highest seed count wins.
#### Special Rules
#### 1) Capture Oponents Seeds: If player's last seed lands in empty pit, capture all seeds from oponents pit directly across from it.
#### 2) Last Seed Lands in Store: If the last seed lands in the player's store, player gets a second turn.

### Board Set-Up

Pits: Each player contains 6 pits starting off with 4 seeds per pit.

         Player 2 Pits: [6,5,4,3,2,1] Start at position 1 and move to the right
         Player 1 Pits: [1,2,3,4,5,6] Start at position 1 and move to the right


Store (Mancala): Each player has one store that contains their current seed count. Once seeds are placed in store they cannot be removed for any reason. Store will be after respective player's #6 pit.

                

## Player Class
### Description
The player class initializes a new player using name and number and contains information regarding each of the players as well as board information and current statistics.
### Implementation
*  **_ init_(self,name,number):** This method initializes player with name, number, starting store, and starting pit counts. All data members are private and can only be called within the player class directly.
* **get_name(self):** This method will return the player's name
* **get_number(self):** This method will return the player's number
* **print_info(self):** This method will print current board information 
* **is_playing(self):** This method will return if player is finished playing. This is displayed by total pit
* **end_player(self):** This method will end the current player's turn and update all pit seed counts to zero.
* **get_store(self):** This method will return player's seed count in store 
* **update_store(self, seed_count):** This method will update current store count
* **get_pit(self):** This method will return the counts of seeds in each pit in list form
* **empty_pit(self, pit_index):** This method will empty pit to 0 and return seed count of given index 
* **distribute(self, pit_index, seed_count, is_chosen):** This method will distribute count of seeds on the chosen player's side, including store.
    
    __Parameters:__

        pit_index (integer): index of first pit that gets distribution seed

        seed_count (integer): remaining seeds to be distributed

        is_chosen: (True): if distributing on chosen player's side
                   (False): if distributing on opponent's side


    __Returns (status, index, remaining-seeds):__


        status = 1: Last seed ended up in store.

        status = 2: Last seed ended up in empty pit.

        index: index of empty pit when status is 2. Ignored for other cases.

        remaining-seeds: integer: seeds remaining at the end of distribution on the current side
        return 0 otherwise.
        


## Mancala Class
### Description
The mancala class will create a new player by calling the player class, check if the play is still in process or complete and resume game play as neessary.
### Implementation
* **_ init_(self):** This method initializes player 1 and player 2, the current (chosen) player, and the game status (done or stil playing). Data members are private variables used by a running game.
* **is_game_running(self):** This method determines if the game has started, by checking to see if players have been created. It will return True or False.
* **has_game_ended(self):** This method determines checks to see if game has ended for either one or both players (all pits will be at 0 seed count). It will return True or False.
* **create_player(self,name):** This method attempts to create player 1 object if not already one created. If player one already created, attempts to create player 2 object. This will return None if fails to create either player. Method will call Player class to create player objects.
* **print_board(self):** This method will print information about board in the current state. This is done by calling print_info() of each player. If both players are not set-up,then "Game has not started" message will be displayed.
* **return_winner(self):** This method returns information about the winning player if possible and if game has ended. Method may also return "It's a tie" if no winner or "Game has not ended" if game still in play.
* **distribute(self, pit_index):** This method obtains chosen pit_index from player and calls to distribute method from player class to move the seeds appropriately and obtain the current status of the move (see status's from player class above). This method will then do the following.
        
    __Special Cases:__

        a. Status 1: (Last seed ended up in store) - Mancala class distribute method will 
                     notify player to take a second turn.

        b. Status 2: (Last seed ended up in empty pit) - Mancala class distribute method
                     will capture all seeds from pit directly opposite from player and
                     dispense into player's store.

        c. Move into Oponent Pits: If player has remaining seeds after dispensing into
                                    store, then play moves into oponents pits.

    Mancala class distribute method differs from player distribute method in that it does not directly move any seeds, but rather calls to the player class distribute method to do so. It then appropriately updates board or player following the last move.

* **play_game(self, player_number, pit_index):** This method takes the parameters of which player is currently going to play as well as which pit_index they choose to start at. Please note the pit_index here will be 1-6 and chosen by player. The method will return the current seed count and store for both players as a list.

    __Parameters:__

        player_number: integer: player number that is to make the move

        pit_index: chosen pit by player (1-6)
    
    
    __Returns:__

        If game has not started: "Game has not started!"

        If invalid player number: "Invalid player number!"

        If invalid pit index: "Invalid number for pit index!"

        If game is over: "Game has ended!"

        seeds: Current seed count/store of both players as a list.

            [P1,P1,P1,P1,P1,P1,S1,P2,P2,P2,P2,P2,P2,S2]

        
## Output

### A simple example of how the class can be used below:


      game = Mancala()
      player1 = game.create_player("Lily")
      player2 = game.create_player("Lucy")
      print(game.play_game(1, 3))
      game.play_game(1, 1)
      game.play_game(2, 3)
      game.play_game(2, 4)
      game.play_game(1, 2)
      game.play_game(2, 2)
      game.play_game(1, 1)
      game.print_board()
      print(game.return_winner())



### And the output will be:

    player 1 take another turn
    [4, 4, 0, 5, 5, 5, 1, 4, 4, 4, 4, 4, 4, 0]
    player 2 take another turn
    player1:
    store: 10
    [0, 0, 2, 7, 7, 6]
    player2:
    store: 2
    [5, 0, 1, 1, 0, 7]
    Game has not ended


### Another test example could be:

      game = Mancala()
      player1 = game.create_player("Lily")
      player2 = game.create_player("Lucy")
      game.play_game(1, 1)
      game.play_game(1, 2)
      game.play_game(1, 3)
      game.play_game(1, 4)
      game.play_game(1, 5)
      game.play_game(1, 6)
      game.print_board()
      print(game.return_winner())


### And the output will be:

      player 1 take another turn
      [4, 4, 0, 5, 5, 5, 1, 4, 4, 4, 4, 4, 4, 0]
      player 2 take another turn
      player1:
      store: 10
      [0, 0, 2, 7, 7, 6]
      player2:
      store: 2
      [5, 0, 1, 1, 0, 7]
      Game has not ended

### Another test example could be:

      game = Mancala()
      player1 = game.create_player("Lily")
      player2 = game.create_player("Lucy")
      game.play_game(1, 1)
      game.play_game(1, 2)
      game.play_game(1, 3)
      game.play_game(1, 4)
      game.play_game(1, 5)
      game.play_game(1, 6)
      game.print_board()
      print(game.return_winner())

### And the output will be:

      player 1 take another turn
      player1:
      store: 12
      [0, 0, 0, 0, 0, 0]
      player2:
      store: 36
      [0, 0, 0, 0, 0, 0]
      Winner is player 2: Lucy
## Reflection

As a child my brother and I would always play mancala year round and would even have family tournaments. This board game holds a special place in my heart. This implementation using python, introduces the concepts of object oriented programming which focuses on using classes and objects to represent data and create larger programs such as this. This program is a text based version of the game with two players.
