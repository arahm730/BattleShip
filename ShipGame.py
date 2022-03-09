# Author: Athiqur Rahman
# GitHub username: arahm730
# Date: 3/9/2022
# Description: A game of battleship is created using the Ship and ShipGame classes.

class Ship:
    """Ship class to represent a ship that will be used in ShipGame."""
    def __init__(self, player, head, all_coordinates, length):
        """
        Description:
            Constructor for the Ship class. Initializes the required data members.
        Parameters:
            player: str representing who owns the ship
            head: str representing the first coordinate of the ship
            all_coordinates: list of str representing coordinates of the entire ship
            length: str representing length of ship
        """
        self._player = player
        self._head = head
        self._all_coordinates = all_coordinates
        self._length = length
        self._health = length
        self._damaged_squares = []

    def get_player(self):
        """Returns a string representing the player who owns the ship"""
        return self._player

    def get_health(self):
        """Returns an integer representing the current health of the ship"""
        return self._health

    def take_damage(self):
        """Decrements the ship’s overall health."""
        self._health -= 1

    def get_all_coordinates(self):
        """Returns a list of strings representing all the coordinates of the ship."""
        return self._all_coordinates

    def get_damaged_squares(self):
        """Returns a list of strings representing the ship's damaged squares"""
        return self._damaged_squares

    def add_damaged_square(self, square):
        """
        Description:
            Adds a new damaged square to the list of damaged squares
        Parameter:
            square: str representing the coordinate of the damaged square
        """
        self._damaged_squares.append(square)


class ShipGame:
    """ShipGame class to represent a game of Battleship played by two players."""
    def __init__(self):
        """Constructor for ShipGame class. Takes no parameters. Initializes the required data members."""
        self._current_state = "UNFINISHED"
        self._turn = "first"
        self._player_first_ships = []
        self._player_second_ships = []
        self._player_first_board = self.create_board()
        self._player_second_board = self.create_board()

    def create_board(self, player_board=None):
        """Returns a 10x10 board of 100 empty '_' squares"""
        if player_board is None:
            player_board = []
        for index in range(10):
            rows = []
            for column in range(10):
                rows.append('_')
            player_board.append(rows)
        return player_board

    def display_board(self, player):
        """
        Description:
            Displays the 10x10 board belonging to the given user
        Parameter:
            player: str representing the player from the game
        """
        if player == "first":
            for lst in self._player_first_board:
                print(lst)
            print("\n")

        if player == "second":
            for lst in self._player_second_board:
                print(lst)
            print("\n")

    def switch_turn(self):
        """Updates the turn to the other player"""
        if self._turn == "first":
            self._turn = "second"
        else:
            self._turn = "first"

    def place_ship(self, player, ship_length, coordinates, orientation):
        """
        Description:
            Allows each player to place ships on their game board. It will incorporate the Ship class to create
            a ship object. It will also place an “X” on that specific square on the board to represent a ship’s square.
        Parameters:
            player: str representing the player who will be placing the ship (first or second)
            ship_length: int representing the length of the ship
            coordinates: str representing the coordinates of the square closest to A1 where the ship will occupy
            orientation: str representing the orientation of the ship (either C for column or R for row)
        Returns:
            False: if the ship would not fit entirely on that player's grid, or if it would overlap other previously
                   placed ships on that player's grid, or if the length of the ship is less than 2
            True:  otherwise, after adding the ship successfully
        """
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
        """
        Description:
            Replaces the chosen horizontal squares with X and returns the coordinates of each replaced square
        Parameters:
            player_board: str representing the board belonging to the player
            ship_length: int representing the length of the ship
            coordinates: str representing the coordinates of the square closest to A1 where the ship will occupy
        Returns:
            ship_cords: list of strings representing all the coordinates belonging to the ship
        """
        row = coordinates[0]
        column = int(coordinates[1]) - 1
        letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        board_row = letters.index(row)
        ship_cords = []
        starting_index = column

        for i in range(ship_length):
            player_board[board_row][starting_index] = 'X'
            ship_cords.append(row + str(starting_index))
            starting_index += 1
        return ship_cords

    def place_vertical(self, player_board, ship_length, coordinates):
        """
        Description:
            Replaces the chosen vertical squares with X and returns the coordinates of each replaced square
        Parameters:
            player_board: str representing the board belonging to the player
            ship_length: int representing the length of the ship
            coordinates: str representing the coordinates of the square closest to A1 where the ship will occupy
        Returns:
            ship_cords: list of strings representing all the coordinates belonging to the ship
        """
        row = coordinates[0]
        column = int(coordinates[1]) - 1
        letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        board_row = letters.index(row)  # E3 will be the 5th row
        ship_cords = []

        for i in range(ship_length):
            player_board[board_row][column] = 'X'
            ship_cords.append(letters[board_row] + str(column+1))
            board_row += 1
        return ship_cords

    def check_ship_fits(self, player_board, ship_length, coordinates, orientation):
        """
        Description:
            Check if a ship can fit a specified row or column
        Parameters:
            player_board: str representing the board belonging to the player
            ship_length: int representing the length of the ship
            coordinates: str representing the coordinates of the square closest to A1 where the ship will occupy
        Returns:
            True: if ships fits either the column or the row
            False: otherwise
        """
        if orientation == "C":
            if self.check_column(player_board, ship_length, coordinates):
                return True
        elif orientation == "R":
            if self.check_row(player_board, ship_length, coordinates):
                return True
        return False

    def check_column(self, player_board, ship_length, coordinates):
        """
        Description:
            Check if a ship can fit a specified column
        Parameters:
            player_board: str representing the board belonging to the player
            ship_length: int representing the length of the ship
            coordinates: str representing the coordinates of the square closest to A1 where the ship will occupy
        Returns:
            False: if the ship would not fit entirely on the specific column or if it would overlap other previously
                   placed ships on that player's grid
            True:  otherwise
        """
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
            if i == '_':
                current_available_space += 1
                total_available_space = max(total_available_space, current_available_space)
            if i != '_':
                current_available_space = 0
                valid_placement = False

        if total_available_space >= ship_length and valid_placement:
            return True

        return False

    def check_row(self, player_board, ship_length, coordinates):
        """
        Description:
            Check if a ship can fit a specified row
        Parameters:
            player_board: str representing the board belonging to the player
            ship_length: int representing the length of the ship
            coordinates: str representing the coordinates of the square closest to A1 where the ship will occupy
        Returns:
            False: if the ship would not fit entirely on the specific row or if it would overlap other previously
                   placed ships on that player's grid
            True:  otherwise
        """
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
            if i == '_':
                current_available_space += 1
                total_available_space = max(total_available_space, current_available_space)
            if i != '_':
                current_available_space = 0
                valid_placement = False

        if total_available_space >= ship_length and valid_placement:
            return True

        return False

    def get_current_state(self):
        """Returns the current state of the game"""
        return self._current_state

    def fire_torpedo(self, player, target_coordinates):
        """
        Description:
            Fire a torpedo at the coordinates on their opponent’s grid
        Parameters:
            player: str representing the player whose torpedo has hit the opponent's ship
            target_coordinates: str representing the coordinates where the torpedo was fired
        Returns:
            False: if it's not the player's turn or if the game has already been won
            True: otherwise, and records the move, updates the turn, and updates current state
        """
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
        """
        Description:
            Hits a ship on the game board. This will use the take_damage method from the Ship class,
            in order to decrement the ship’s health if the square has not yet been hit.
        Parameters:
            player: str representing the player whose torpedo has hit the opponent's ship
            target_coordinates: str representing the coordinates where the torpedo was fired
        """
        targeted_ships = None

        if player == "first":
            targeted_ships = self._player_second_ships
        elif player == "second":
            targeted_ships = self._player_first_ships

        # Loops through each Ship object in the opponent's list of Ship objects
        for ship in targeted_ships:
            if target_coordinates in ship.get_all_coordinates():
                damaged_squares = ship.get_damaged_squares()
                # Ensures that the coordinate has not been previously attacked
                if target_coordinates not in damaged_squares:
                    ship.add_damaged_square(target_coordinates)
                    ship.take_damage()
                    if ship.get_health() == 0:
                        # All the squares of a ship have been hit
                        self.sink_ship(player, ship)

    def sink_ship(self, player, sunk_ship):
        """
        Description:
            Sinks the opponent's ship and removes the Ship object from the opponent's list of ship objects.
        Parameters:
            player: str representing the player whose hit has sunk the opponents ship
            sunk_ship: str representing the Ship object that has been sunk
        """
        if player == "first":           # Player first sinks player second's ship
            self._player_second_ships.remove(sunk_ship)
            if len(self._player_second_ships) == 0:
                self._current_state = "FIRST_WON"
        elif player == "second":        # Player second sinks player first's ship
            self._player_first_ships.remove(sunk_ship)
            if len(self._player_first_ships) == 0:
                self._current_state = "SECOND_WON"

    def get_nums_ships_remaining(self, player):
        """
        Description:
            Returns the number of ships remaining for the specified player
        Parameters:
            player: str representing a player from the game
        Returns:
            integer of the number of remaining ships in the player's list of ships
        """
        if player == "first":
            return len(self._player_first_ships)
        elif player == "second":
            return len(self._player_second_ships)

