import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

board = np.tile([1, 0], [8, 4])

for i in range(board.shape[0]):
    board [i] = np.roll(board[i], i%2)

cmap = ListedColormap(['black', 'white'])
plt.matshow(board, cmap=cmap)

cols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
rows = ['8', '7', '6', '5', '4', '3', '2', '1']
plt.xticks(range(8), cols) 
plt.yticks(range(8), rows)
plt.grid(False)
plt.title('chessboard', fontsize = 14, pad = 10)
plt.show()

