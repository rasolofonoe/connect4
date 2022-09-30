from .game import Grid, Player,Cell


class DumbIA(Player):
    def play(self, grid: Grid) -> int:
        i = 0
        j = 0
        etat = 0
        while etat != 1:
            if grid.grid[i][j] == Cell.EMPTY:
                etat = 1
                return j
            else:
                j = j+1
                if grid.grid[i][j] == Cell.EMPTY:
                    etat = 1
                    return j
                else:
                    if j == 6:
                        i = i +1
                        j = 1





    #def play(self, player: Player, cell: Cell) -> bool:
    #        column = player.play(self.grid)
    #        line = self.grid.place(column, cell)
    #        return self.grid.win(line, column)

    #ret = ""
    #for line in range(self.lines - 1, -1, -1):
    #    ret += "|"
    #    for column in range(self.columns):
    #        ret += self.grid[line][column].value
    #    ret += "|\n"
    #ret += "+" + "-" * self.columns + "+\n"
    #ret += " " + "".join(str(i) for i in range(self.columns)) + "\n"

