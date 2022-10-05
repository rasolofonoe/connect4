from .game import Grid, Player


class ConsolePlayer(Player):
    """Allow a human to see the grid in its shell, and input a column from the
    keyboard."""

    def play(self, grid: Grid) -> int:
        print(grid)
        col = int(input("Colum:"))
        return col
