
class Player:
    """A class to represent a player with name and position being played. Used by Mancala class"""
    def __init__(self, name, number):
        """
        Creates a new player using name and number.
        Caller must not create an already existing player.
        Saves name and number in private variables
        Additionally,
        - parameters:
          name: string - name of the new player
          number: integer - 1 or 2
        - member data:
          _store: integer - initialized to 0. During game, it contains seed count in store
          _pits: list of 6 integers: contains seeds belonging to player. Initialized to 4 in each pit.
         _turn: True means it is this player's turn to play
        """

        # Create starting data members for constructor class
        self._name = name
        self._number = number
        self._store = 0
        self._pits = [4, 4, 4, 4, 4, 4]

    def __str__(self):
        return f'Player: {self._name}, Pits: {self._pits}'

    def __repr__(self):
        return f'Player(\'{self._name}\', {self._pits})'

    def get_name(self):
        """ Function returns player name """

        return self._name

    def get_number(self):
        """ Function will return player number """

        return self._number

    def print_info(self):
        """Function will print board information with player and current store"""

       # Return player number, store, with current pit count
        print('player' + str(self._number))
        print('store: ' + str(self._store))
        print(str(self._pits))

    def is_playing(self):
        """Function returns if player is finished playing. This is displayed by total pit count."""

        # If any of the pits still contain seeds, play still active
        for index, seed_count in enumerate(self._pits):
            if seed_count != 0:
                return True
        return False

    def end_player(self):
        """Function will end the current player turn"""

        # Iterate through all pits, and move remaining seeds into store
        # Update all pits to zero
        for index, seed_count in enumerate(self._pits):
            self.update_store(seed_count)
            self._pits[index] = 0

    def get_store(self):
        """Function returns player's seed count in store"""

        # Obtains current store seed count
        return self._store

    def update_store(self, seed_count):
        """Function updates store count"""

        # Update the store once seeds deposited
        self._store += seed_count

    def get_pit(self):
        """ Function will return pit list """

        # Obtain the current pit seed count for player
        return self._pits

    def empty_pit(self, pit_index):
        """Function will set empty pit to 0 and return seed count"""

        # Obtain the seed count in current pit
        seed_count = self._pits[pit_index]

        # Update all pits to 0
        self._pits[pit_index] = 0

        # Obtain the current seed count
        return seed_count

    def distribute(self, pit_index, seed_count, is_chosen):
        """
        Distribute count of seeds on the chosen player's side, including store.
        parameters:
        pit_index: integer: index of first pit that gets distribution seed
        seed_count: integer: remaining seeds to be distributed
        is_chosen: True: if distributing on chosen player's side
                   False: if distributing on opponent's side
        Returns (status, index, remaining-seeds)
        status = 1: Last seed ended up in store.
        status = 2: Last seed ended up in empty pit.
        index: index of empty pit when status is 2. Ignored for other cases.
        remaining-seeds: integer: seeds remaining at the end of distribution on the current side
        return 0 otherwise.
        """


        index = pit_index
        count = seed_count

        # Distribute seeds into pits
        while index < 6 and count > 0:
            # If distributing into chosen player's pits, look for empty pit
            if is_chosen:
                # Check if last seed and pit empty
                if count == 1:
                    # Last seed.
                    if self._pits[index] == 0:
                        # Last seed going into empty pit.
                        # Return proper status, index of empty pit and count to caller
                        return (2, index, 0)

            # None of the cases above. Place seed in pit and continue.
            self._pits[index] += 1
            count -= 1
            index += 1

        # Exited while loop. Is the last seed going into store?
        if is_chosen and count > 0:
            # Add seed to store.
            if index == 6:
                self.update_store(1)
                count -= 1
                # Set index back to 0 so that player starts at first pit
                index = 0
                if count == 0:
                    return (1, index, 0)

        # Return leftover seeds with status 0
        # Continue on next player side
        return (0, index, count)

class Mancala:
    """A class to represent Mancala game with board information in current state and player information"""
    def __init__(self):
        """
        Manages data in private variables used by a running game
        _player1: reference to player object for player 1
        _player2: reference to player object for player 1
        _chosen_player_number: integer: default player is 1
        """

        self._player1 = None
        self._player2 = None
        self._chosen_player_number = 1
        self._game_ended = False

    def is_game_running(self):
        """Determines if the game has started by checking to see if players have been created"""
        if not self._player1 or not self._player2:
            return False
        return True

    def has_game_ended(self):
        """Checks to see if game has ended for either player or both (pits at 0)"""

        chosen_player = self._player1 if self._chosen_player_number == 1 else self._player2
        opponent = self._player2 if self._chosen_player_number == 1 else self._player1
        if not chosen_player.is_playing():
            opponent.end_player()
            return True

        return False

    def create_player(self, name):
        """
        Attempts to create player 1 if not already one created.
        If player 1 is already created, attempts to create player 2.
        returns None if fails to create either player.
        Returns the reference to newly created player object otherwise.
        """

        if not self._player1:
            # If no player 1 exists. Create one.
            self._player1 = Player(name, 1)
            return self._player1

        # Try creating player 2
        if self._player2:
            print("Player list full. No new players can be created")
            return None
        # Else create player 2
        self._player2 = Player(name, 2)
        return self._player2

    def print_board(self):
        """
        Print information about game board in the current state.
        This is done by calling print_info() of each player.
        If both players are not set-up, message, "Game has not started"
        is printed.
        """

        if not self.is_game_running():
            print("Game has not started")
        else:
            self._player1.print_info()
            self._player2.print_info()

    def return_winner(self):
        """
        Returns information about winning player, if game ended and there is a winner.
        Returns "It's a tie", if no winner.
        Returns "Game has not ended" otherwise.
        """

        if not self.is_game_running():
            return "Game has not started"

        # Check if both players finished
        if self._game_ended:
            # Check who got more seeds
            seeds1 = self._player1.get_store()
            seeds2 = self._player2.get_store()
            if seeds1 > seeds2:
                # Player1 won.
                return "Winner is player 1: " + self._player1.get_name()
            elif seeds1 < seeds2:
                # Player2 won.
                return "Winner is player 2: " + self._player2.get_name()
            else:
                return "It's a tie"
        else:
            return "Game has not ended"

    def distribute(self, pit_index):
        """
        Distributes seeds in pit at pit_index into pits to right.
        Follows rules.
        Returns 1 if game ended and 0 otherwise.
        """

        # Pick right player object based on number
        player = self._player1 if self._chosen_player_number == 1 else self._player2
        opponent = self._player2 if self._chosen_player_number == 1 else self._player1

        # Empty player's pit into seed_count
        opponent_index = 0
        seed_count = player.empty_pit(pit_index)
        chosen_index = pit_index + 1

        # Keep distributing into player's and opponents pits until done
        while True:
            if seed_count <= 0:
                # Return status 1 if game ended
                if self.has_game_ended():
                    return 1
                return 0

            # Distribute on player's side
            (status, chosen_index, seed_count) = player.distribute(chosen_index, seed_count, True)

            # If all seeds are distributed, find where last seed ended up.
            if seed_count <= 0:
                if status == 1:
                    # Seed ended up in store.
                    print("Player " + str(self._chosen_player_number) + " take another turn")
                    continue

                if status == 2:
                    # Seed ended up in empty pit on player's side
                    count = opponent.empty_pit(5 - chosen_index)
                    player.update_store(count + 1)

                    # Check end game condition and do so if needed
                    continue

            # We have leftover seeds. Distribute into opponents pits.
            (status, opponent_index, seed_count) = opponent.distribute(opponent_index, seed_count, False)

    def play_game(self, player_number, pit_index):
        """
        Return if game not running or player_number is neither 1 nor 2.
        Return with message if pit_number out of range.
        player_number: integer: player number that is to make the move
        pit_index: index of pit on player's side
        """

        index = pit_index

        # Error if game not started
        if not self.is_game_running():
            return "Game has not started!"

        # Is the player valid
        if player_number != 1 and player_number != 2:
            return 'Invalid player number!'

        # Is the pit valid
        if index <= 0 or index > 6:
            return 'Invalid number for pit index!'

        # If the game has already ended, then return string indicating the same.
        if self._game_ended:
            return "Game has ended!"

        # Remember new chosen player number
        self._chosen_player_number = player_number

        # Convert pit_index from position to index
        index -= 1
        status = self.distribute(index)
        if status == 1:
            self._game_ended = True

        seeds = []
        seeds.extend(self._player1.get_pit())
        seeds.append(self._player1.get_store())

        seeds.extend(self._player2.get_pit())
        seeds.append(self._player2.get_store())
        return seeds

if __name__ == "__main__":

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
    game.return_winner()


