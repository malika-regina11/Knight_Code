import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

board = np.tile([1, 0], [8, 4])

for i in range(board.shape[0]):
    board [i] = np.roll(board[i], i%2)

cmap = ListedColormap(['#769656', '#eeeed2'])
plt.figure(figsize=(6, 6))
plt.matshow(board, cmap=cmap, fignum=1)

pieces = [
    ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"],  # Black major pieces
    ["♟"] * 8,                                  # Black pawns
    [""] * 8,
    [""] * 8,
    [""] * 8,
    [""] * 8,
    ["♙"] * 8,                                  # White pawns
    ["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"],  # White major pieces
]

for i in range(8):
    for j in range(8):
        piece = pieces[i][j]
        if piece != "":
            plt.text(j, i, piece, ha='center', va='center', fontsize=30)
            
cols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
rows = ['8', '7', '6', '5', '4', '3', '2', '1']
plt.xticks(range(8), cols) 
plt.yticks(range(8), rows)
plt.grid(False)
plt.title('chessboard', fontsize = 14, pad = 10)
plt.show()


