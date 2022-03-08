# Author: Athiqur Rahman
# GitHub username: arahm730
# Date: 3/7/2022
# Description: A game of battleship is created using the Ship and ShipGame classes.

class Ship:
    """Ship class to represent a ship that will be used in ShipGame."""
    def __init__(self, player, head, all_coordinates, length):
        """Constructor for the Ship class.Takes three parameters. Initializes the required data members."""
        self._player = player
        self._head = head
        self._all_coordinates = all_coordinates
        self._length = length
        self._health = length
        self._damaged_squares = []

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

    def get_damaged_squares(self):
        return self._damaged_squares

    def add_damaged_square(self, square):
        self._damaged_squares.append(square)


class ShipGame:
    """ShipGame class to represent a game of Battleship, played by two players."""
    def __init__(self):
        """Constructor for ShipGame class. Takes no parameters. Initializes the required data members."""
        self._player_first_board = []
        self._player_first_ships = []
        self._player_second_board = []
        self._player_second_ships = []

        self._current_state = "UNFINISHED"
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
            for lst in self._player_first_board:
                print(lst)
            print("\n")

        if player == "second":
            for lst in self._player_second_board:
                print(lst)
            print("\n")

    def switch_turn(self):
        """The purpose of this method is to switch turns. It updates the turn to the other player."""
        if self._turn == "first":
            self._turn = "second"
        else:
            self._turn = "second"

    def place_ship(self, player, ship_length, coordinates, orientation):
        """Purpose: The purpose of this method is for each player to place ships on their game board. It will
        incorporate the Ship class to create a ship object. It will also place an “X” on that specific square
        on the board to represent a ship’s square."""

        if player == "first" and ship_length >= 2:
            if self.check_ship_fits(self._player_first_board, ship_length, coordinates, orientation):
                # Puts 1 on the grid
                if orientation == "R":
                    ship_cords = self.place_horizontal(self._player_first_board, ship_length, coordinates)
                    # There is space to put ship
                    player_first_ship = Ship("first", coordinates, ship_cords, ship_length)
                    self._player_first_ships.append(player_first_ship)
                elif orientation == "C":
                    ship_cords = self.place_vertical(self._player_first_board, ship_length, coordinates)
                    # There is space to put ship
                    player_first_ship = Ship("first", coordinates, ship_cords, ship_length)
                    self._player_first_ships.append(player_first_ship)
                return True

        elif player == "second" and ship_length >= 2:
            if self.check_ship_fits(self._player_second_board, ship_length, coordinates, orientation):
                # Puts 1 on the grid
                if orientation == "R":
                    ship_cords = self.place_horizontal(self._player_second_board, ship_length, coordinates)
                    # There is space to put ship
                    player_second_ship = Ship("second", coordinates, ship_cords, ship_length)
                    self._player_second_ships.append(player_second_ship)

                elif orientation == "C":
                    ship_cords = self.place_vertical(self._player_second_board, ship_length, coordinates)
                    # There is space to put ship
                    player_second_ship = Ship("first", coordinates, ship_cords, ship_length)
                    self._player_second_ships.append(player_second_ship)
                return True

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
            ship_cords.append(row + str(starting_index))
            starting_index += 1
        return ship_cords

    def place_vertical(self, player_board, ship_length, coordinates):
        """Replaces vertical squares with 1 and returns the coordinates of each replaced square"""
        row = coordinates[0]
        column = int(coordinates[1]) - 1
        letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        board_row = letters.index(row)  # E3 will be the 5th row
        ship_cords = []
        for i in range(ship_length):
            player_board[board_row][column] = 1
            ship_cords.append(letters[board_row] + str(column+1))
            board_row += 1
        return ship_cords

    def check_ship_fits(self, player_board, ship_length, coordinates, orientation):
        """Check if a ship can fit a specified row or column"""
        if orientation == "C":
            if self.check_column(player_board, ship_length, coordinates):
                return True
        elif orientation == "R":
            if self.check_row(player_board, ship_length, coordinates):
                return True
        return False

    def check_column(self, player_board, ship_length, coordinates):
        """Check if a ship can fit a specific column"""
        row = coordinates[0]
        column = int(coordinates[1]) - 1

        letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        board_row = letters.index(row)

        searchable_column = []
        for i in range(ship_length):
            searchable_column.append(player_board[board_row:][i][column])

        valid_placement = True
        total_available_space = 0
        current_available_space = 0

        if len(searchable_column) < ship_length:
            return False

        # Checks rest of column starting at column number.
        for i in searchable_column:
            if i == 0:
                current_available_space += 1
                total_available_space = max(total_available_space, current_available_space)
            if i != 0:
                current_available_space = 0
                valid_placement = False

        if total_available_space >= ship_length and valid_placement:
            return True

        return False

    def check_row(self, player_board, ship_length, coordinates):    #CHECK BUGS
        """Check if a ship can fit a specific row"""
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
        """Fire a torpedo at the coordinates on their opponent’s grid"""
        if self._turn == player and self._current_state == "UNFINISHED":
            targeted_ships = None
            if player == "first":
                targeted_ships = self._player_second_ships
            elif player == "second":
                targeted_ships = self._player_first_ships

            for ship in targeted_ships:
                if target_coordinates in ship.get_all_coordinates():
                    self.hit_ship(player, target_coordinates)
            self.switch_turn()
            return True
        else:
            return False

    def hit_ship(self, player, target_coordinates):
        """”Hit a ship on the game board. This will also use the take_damage method from the Ship class,
        in order to decrement the ship’s health depending on whether a square on the ship has already been hit."""
        targeted_ships = None
        if player == "first":
            targeted_ships = self._player_second_ships
        elif player == "second":
            targeted_ships = self._player_first_ships

        for ship in targeted_ships:
            if target_coordinates in ship.get_all_coordinates():
                damaged_squares = ship.get_damaged_squares()
                if target_coordinates not in damaged_squares:
                    ship.add_damaged_square(target_coordinates)
                    ship.take_damage()

                    if ship.get_health() == 0:
                        self.sink_ship(self, player, ship)

    def sink_ship(self, player, sunk_ship):
        """”Sink a player’s ship. It will decrement the player’s ship count by 1."""
        if player == "first":
            self._player_first_ships.remove(sunk_ship)
            if len(self._player_first_ships) == 0:
                self._current_state = "SECOND_WON"
        elif player == "second":
            self._player_second_ships.remove(sunk_ship)
            if len(self._player_second_ships) == 0:
                self._current_state = "FIRST_WON"

    def get_nums_ships_remaining(self, player):
        """Integer specifying ships remaining for the specified player"""
        if player == "first":
            return len(self._player_first_ships)
        elif player == "second":
            return len(self._player_second_ships)
