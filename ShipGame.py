# Author: Athiqur Rahman
# GitHub username: arahm730
# Date: 3/5/2022
# Description: A game of battleship is created using the Ship and ShipGame classes.

class Ship:
    """Ship class to represent a ship that will be used in ShipGame."""
    def __init__(self, player, head, all_coordinates, length):
        """Constructor for the Ship class.Takes three parameters. Initializes the required data members.
        player - represents the player who owns the specific ship
        head - represents the head of the ship (closest to A1)
        length - represents the length of the ship
        The private data member health represents health of the ship and initially equals the length of the ship
        """
        self._player = player
        self._head = head
        self._all_coordinates = all_coordinates
        self._length = length
        self._health = length

    def get_player(self):
        """Getter method to return the player who owns the ship and is used by the ShipGame class."""
        return self._player

    def get_health(self):
        """Getter method to return the current health of the ship and is used by the ShipGame class."""
        return self._health

    def take_damage(self):
        """Purpose: The purpose of this method is to decrement the ship’s overall health. """
        self._health -= 1

    def get_all_coordinates(self):
        return self._all_coordinates


class ShipGame:
    """ShipGame class to represent a game of Battleship, played by two players."""
    def __init__(self):
        """Constructor for ShipGame class. Takes no parameters. Initializes the required data members."""
        self._player_first_board = []
        self._player_first_ships = []
        self._player_second_board = []
        self._player_second_ships = []

        self._current_state = None
        self._turn = "first"
        self._winner = None

        self.create_board(self._player_first_board)
        self.create_board(self._player_second_board)

    def create_board(self, player_board):
        for index in range(10):
            rows = []
            for column in range(10):
                rows.append(0)
            player_board.append(rows)

    def display_board(self, player):
        if player == "first":
            for lst in game._player_first_board:
                print(lst)
            print("\n")

        if player == "second":
            for lst in game._player_first_board:
                print(lst)
            print("\n")

    def switch_turn(self, player_number):
        """Takes one parameter:
        player_number – represents which player’s turn it is (first or second)
        Purpose: The purpose of this method is to switch turns. It updates the turn to the other player.
        Returns:
        False - if turn is invalid
        True - after checking if turn is finished and valid"""
        if self._turn == "first":
            self._turn = "second"
        else:
            self._turn = "second"

    def place_ship(self, player, ship_length, coordinates, orientation):
        """Takes four parameters:
        player – represents which player is making the move (first or second)
        ship_length – represents length of ship
        coordinates – represents square the ship will occupy closest to A1
        orientation – represents ship’s orientation (R if squares in same row, C if in same column)
        Purpose: The purpose of this method is for each player to place ships on their game board. It will
        incorporate the Ship class to create a ship object. It will also place an “X” on that specific square
        on the board to represent a ship’s square.
        Returns:
        False – if ship does not fit on player’s grid, or if it would overlap with other placed ships on
        player’s grid or if length of ship is less than 2"""

        if player == "first":
            if self.check_ship_fits(self._player_first_board, ship_length, coordinates, orientation):
                # Puts 1 on the grid
                if orientation == "R":
                    ship_cords = self.place_horizontal(self._player_first_board, ship_length, coordinates)

                    # There is space to put ship
                    player_first_ship = Ship("first", coordinates, ship_cords, ship_length)
                    self._player_first_ships.append(player_first_ship)

                return True

        elif player == "second":
            self.check_ship_fits(self._player_second_board, ship_length, coordinates, orientation)

        return False

    def place_horizontal(self, player_board, ship_length, coordinates):
        """Replaces horizontal squares with 1 and returns the coordinates of each replaced square"""
        row = coordinates[0]
        column = int(coordinates[1]) - 1
        letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        board_row = letters.index(row)  # E3 will be the 5th row

        ship_cords = []
        starting_index = column
        for i in range(ship_length):
            player_board[board_row][starting_index] = 1
            starting_index += 1
            ship_cords.append(row + str(starting_index))
        return ship_cords

    def check_ship_fits(self, player_board, ship_length, coordinates, orientation):
        """Takes four parameters:
        player_board – represents a board from a player
        ship_length – represents length of ship
        coordinates – represents square the ship will occupy closest to A1
        orientation – represents ship’s orientation (R if squares in same row, C if in same column)
        Purpose: The purpose of this method is to check if a ship can fit a specified row or column
        Returns:
        False – if ship does not fit on player’s grid, or if it would overlap with other placed ships on
        player’s grid or if length of ship is less than 2
        True – if there is room in the player board’s row or column"""
        row = coordinates[0]
        column = int(coordinates[1]) - 1
        if orientation == "C":
            if self.check_column(player_board, ship_length, coordinates):
                return True
        elif orientation == "R":
            if self.check_row(player_board, ship_length, coordinates):
                return True

    def check_column(self, player_board, ship_length, coordinates):
        """Takes three parameters:
        player_board – represents a board from a player
        ship_length – represents length of ship
        coordinates – represents square the ship will occupy closest to A1
        Purpose: The purpose of this method is to check if a ship can fit a specific column
        Returns:
        False – if ship does not fit on the specific column, or if it would overlap with other placed ships
        on that column
        True – if there is room in the player board’s specified column"""
        row = coordinates[0]
        column = int(coordinates[1])
        pass

    def check_row(self, player_board, ship_length, coordinates):
        """Takes three parameters:
        player_board – represents a board from a player
        ship_length – represents length of ship
        coordinates – represents square the ship will occupy closest to A1
        Purpose: The purpose of this method is to check if a ship can fit a specific row
        Returns:
        False – if ship does not fit on the specific row, or if it would overlap with other placed ships on
        that row
        True – if there is room in the player board’s specified row"""
        row = coordinates[0]
        column = int(coordinates[1]) - 1

        letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        board_row = letters.index(row)  # E3 will be the 5th row

        valid_placement = True
        total_available_space = 0
        current_available_space = 0
        searchable_space = player_board[board_row][column:]

        if len(searchable_space) < ship_length:
            return False

        # Checks rest of row starting at column number. E3 means starting at 3rd element in list up to last element
        for i in searchable_space[:ship_length]:
            if i == 0:
                current_available_space += 1
                total_available_space = max(total_available_space, current_available_space)
            if i != 0:
                current_available_space = 0
                valid_placement = False

        if total_available_space >= ship_length and valid_placement:
            return True

        return False



    def get_current_state(self):
        """Gets the current state of the game"""
        return self._current_state

    def fire_torpedo(self, player, target_coordinates):
        """Takes two parameters:
        player – represents which player is making the move (first or second)
        target_coordinates – represents coordinates of target square
        Purpose: The purpose of this method is for the player to fire a torpedo at the coordinates on
        their opponent’s grid
        Returns:
        False – If it is not the player’s turn or if the game has already been won
        True – returns True otherwise after recording the move, updating whose turn it is, and updating
        current state"""
        pass

    def hit_ship(self, player, target_coordinates):
        """”Takes two parameters:
        player – represents which player is making the move (first or second)
        target_coordinates – represents coordinates of target square
        Purpose: The purpose of this method is to hit a ship on the gameboard. This will also use the
        take_damage method from the Ship class, in order to decrement the ship’s health depending on
        whether a square on the ship has already been hit.
        Returns:
        False – If it is not the player’s turn or if the game has already been won
        True – if a ship is successfully hit"""

    def sink_ship(self, player, coordinates):
        """”Takes two parameters:
        player – represents the player whose ship has been recently sunk
        coordinates – represents coordinates of ship
        Purpose: The purpose of this method is to sink a player’s ship. It will decrement the player’s ship
        count by 1.
        Return:
        False – If it is not the player’s turn or if the game has already been won
        True – returns True after decrementing the player’s ship count
        """

    def get_nums_ships_remaining(self, player):
        """Takes one parameter:
        player – represents the specified player (first or second)
        Purpose: The purpose of this method is to return how many ships the specified player has left
        Return:
        Integer specifying ships remaining for the specified player"""
        pass

game = ShipGame()
print("Test")
print(game.place_ship('first', 5, 'A3', 'R'))
print(game.place_ship('first', 5, 'A6', 'R'))
print(game._player_first_ships[0]._all_coordinates)



game.display_board("first")

