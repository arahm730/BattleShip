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
        """Decrements the ship’s health by 1."""
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