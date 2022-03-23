A game of Battleships is created where two players control a 10x10 grid. Each player is allowed to place as many
ships possible on their grid.

Example: Player 'first' places a ship on G9 as a column:

place_ship('first', 4, 'G9', 'C')
```
  1 2 3 4 5 6 7 8 9 10
A
B
C
D
E
F
G                 x
H                 x
I                 x
J                 x
```

Player 'first' is the first person allowed to fire a torpedo, after which they alternate firing torpedoes. 
A ship is sunk once all of its squares have been hit. When a player sinks their opponent's final ship they win.
