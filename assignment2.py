import random as rnd
import os
import sys

class Grid():
    def __init__(self, row=4, col=4, initial=2):
        self.row = row                              # number of rows in grid
        self.col = col                              # number of columns in grid
        self.initial = initial                      # number of initial cells filled
        self.score = 0

        self.grid = self.createGrid(row, col)       # creates the grid specified above

        self.emptiesSet = []                        # list of empty cells
        self.updateEmptiesSet()

        for _ in range(self.initial):               # assign two random cells
            self.assignRandCell(init=True)


    def createGrid(self, row, col):

        """
        Create the grid here using the arguments row and col
        as the number of rows and columns of the grid to be made.

        The function should return the grid to be used in __init__()
        """
        grid = [ ]                                 # a list used to save list
        tiles = [ ]
        for r in range(row):
            for c in range(col):
                tiles.append(0)                    # init all the tiles 
            grid.append(tiles) 
            tiles = [ ]
        return (grid)
            


    def assignRandCell(self, init=False):

        """
        This function assigns a random empty cell of the grid
        a value of 2 or 4.

        In __init__() it only assigns cells the value of 2.

        The distribution is set so that 75% of the time the random cell is
        assigned a value of 2 and 25% of the time a random cell is assigned
        a value of 4
        """

        if len(self.emptiesSet):
            cell = rnd.sample(self.emptiesSet, 1)[0]
            if init:
                self.grid[cell[0]][cell[1]] = 2
            else:
                cdf = rnd.random()
                if cdf > 0.75:
                    self.grid[cell[0]][cell[1]] = 4
                else:
                    self.grid[cell[0]][cell[1]] = 2
            self.emptiesSet.remove(cell)


    def drawGrid(self):

        """
        This function draws the grid representing the state of the game
        grid
        """

        for row_index in range(self.row):
            line = '\t|'
            for col_index in range(self.col):
                if not self.grid[row_index][col_index]:
                    line += ' '.center(5) + '|'
                else:
                    line += str(self.grid[row_index][col_index]).center(5) + '|'
            print(line)
        print()


    def updateEmptiesSet(self):

        """
        This function should update the list of empty tiles of the grid.
        """
        self.emptiesSet.__init__()                                     # reinitialize the emptiesSet
        for row_index in range(self.row):
            for col_index in range(self.col):
                if self.grid[row_index][col_index] == 0:
                    self.emptiesSet.append([row_index,col_index])
       
    def collapsible(self):

        """
        This function should test if the grid of the game is collapsible
        in any direction (left, right, up or down.)

        It should return True if the grid is collapsible.
        It should return False otherwise.
        """
       
        grid = [ ]                                                     # a copy of self.grid, it will be changed later
        new_tiles = [ ]                                                # a tiles used to store each colum tiles in self.grid
        this_tile_can_merge = True
        isFull = True
        
        
        # compare each tile to the other tiles in the same row, judge if the tile can collapse or not
        # compare each row in self.grid
        for tiles in self.grid:
            for index in range(len(tiles)-1,0,-1):
                if tiles[index] != 0:
                    for index_previous in range(index-1,-1,-1):
                        if tiles[index_previous] == 0:
                            return True
                        if (tiles[index] != tiles[index_previous]) and (tiles[index_previous] != 0):
                            this_tile_can_merge = False
                        if (tiles[index] == tiles[index_previous]) and ( this_tile_can_merge == True):
                            return True
                    this_tile_can_merge = True
               
        # change each colum in self.grid to row, and use grid to keep them
        for col_index in range(self.col): 
            for row_index in range(self.row):
                new_tiles.append(self.grid[row_index][col_index])
            grid.append(new_tiles)
            new_tiles = [ ]
               
        # compare each tile to the other tiles in the same row, judge if the tile can collapse or not 
        # compare each colum in self.grid(now is row)
        for tiles in grid:
            for index in range(len(tiles)-1,0,-1):
                if tiles[index] != 0:
                    for index_previous in range(index-1,-1,-1):
                        if tiles[index_previous] == 0:
                            return True                        
                        if (tiles[index] != tiles[index_previous]) and (tiles[index_previous] != 0):
                            this_tile_can_merge = False
                        if (tiles[index] == tiles[index_previous]) and ( this_tile_can_merge == True):
                            return True
                    this_tile_can_merge = True
        
        # if there have at least one tile equal to 0, the grid is not ful
        for tiles in self.grid:
            for tile in tiles:
                if tile == 0 :
                    isFull = False
        
        # if there still have empty tile, we can collpase in a direction
        if isFull:
            return False                                         # in this case,the grid is fall, and all the tiles cannot be collopsed in any direction
        else:
            return True


    def collapseRow(self, lst):

        """
        This function takes a list lst and collapses it to the LEFT.

        This function should return two values:
        1. the collapsed list and
        2. True if the list is collapsed and False otherwise.
        """
        collapse = False                                                  # judge the row can be collapsed or not
        index = -1                                                        # a variable 

        
        # judege the tiles in a row can be merge or not
        for row_index in range(1,len(lst)):
            whether_merge_or_not = True                                   # judeg whether this tile can merger to another or not
            if lst[row_index] != 0:
                for row_index_previous in range(row_index-1,index,-1):
                    if (lst[row_index] != lst[row_index_previous]) and (lst[row_index_previous] != 0):
                        whether_merge_or_not = False                      # this tile cannot merge to other because there is another tile which has different valuse 
                
        # merge two tiles
                    if (lst[row_index] == lst[row_index_previous]) and (whether_merge_or_not == True):
                        lst[row_index_previous] *= 2
                        lst[row_index] = 0
                        collapse = True
                        self.score +=  lst[row_index_previous]            # score should be added when two tiles merge together
                        index = row_index_previous
                       
                        
        # move the tiles in this row, move is just like change each tile's position in the list                        
        for row_index in range(len(lst)):
            for row_index_previous in range(row_index + 1,len(lst)):
                if lst[row_index] == 0:
                    if lst[row_index_previous] != 0:
                        lst[row_index] = lst[row_index_previous]
                        lst[row_index_previous] = 0
                        collapse = True
                      
        return (lst,collapse)

    def collapseLeft(self):

        """
        This function should use collapseRow() to collapse all the rows
        in the grid to the LEFT.

        This function should return True if any row of the grid is collapsed
        and False otherwise.
        """
        states_for_each_row = [ ]                                       # a list to store all the rows states that the list can be collapse or not
        
        for tiles in self.grid:
            lst,state = self.collapseRow(tiles)
            states_for_each_row.append(state)
        
        for state in states_for_each_row:
            if state == True:
                return True
           
        return False
          
          
    def collapseRight(self):

        """
        This function should use collapseRow() to collapse all the rows
        in the grid to the RIGHT.

        This function should return True if any row of the grid is collapsed
        and False otherwise.
        """
        temp = 0                                                        #  varialbe used to store tile's value
        row_index = 0                                                   #  varialbe used to represent the each row
        states_for_each_row = [ ]                                       # a list to store all the rows states that the list can be collapse or not
        
        # make tiles's sequence in each row opposite, we can use the same way that we did in CollapseLeft
        for tiles in self.grid:
            while(row_index != self.row - row_index) and (row_index < self.row - row_index -1):
                temp = tiles[row_index]
                tiles[row_index] = tiles[self.row - row_index-1]
                tiles[self.row-row_index-1] = temp
                row_index += 1
            row_index = 0                
                

        for tiles in self.grid:
            lst,state = self.collapseRow(tiles)
            states_for_each_row.append(state)
        
        # we need to change the sequence back to the origin
        for tiles in self.grid:
            while(row_index != self.row - row_index) and (row_index < self.row - row_index -1):
                temp = tiles[row_index]
                tiles[row_index] = tiles[self.row - row_index-1]
                tiles[self.row-row_index-1] = temp
                row_index += 1
            row_index = 0   
        
        for state in states_for_each_row:
            if state == True:
                return True

        return False
        

    def collapseUp(self):

        """
        This function should use collapseRow() to collapse all the columns
        in the grid to UPWARD.

        This function should return True if any column of the grid is
        collapsed and False otherwise.
        """
        col_number = 0                                                   #  varialbe used to represent the each colum
        new_tiles = [ ]                                                  #  a list to keep each colum in self.grid
        states_for_each_row = [ ]                                        # a list to store all the rows states that the list can be collapse or not
        
        # change each colum into row
        for col_index in range(self.col):
            for row_index in range(self.row):
                new_tiles.append(self.grid[row_index][col_index])
                
            lst,state = self.collapseRow(new_tiles)                          #  we can use the arrtibute since all the coulms are rows now
            states_for_each_row.append(state)
            
         # store the answer back to the self.grid 
            for row_number in range(self.row):
                self.grid[row_number][col_number] = new_tiles[row_number]
            col_number += 1
            new_tiles = [ ] 
        
        for state in states_for_each_row:
            if state == True:
                return True
        
        return False

    def collapseDown(self):

        """
        This function should use collapseRow() to collapse all the columns
        in the grid to DOWNWARD.

        This function should return True if any column of the grid is
        collapsed and False otherwise.
        """
        col_number = 0                                                  #  varialbe used to represent the each colum
        new_tiles = [ ]                                                 #  a list to keep each colum in self.grid
        temp = 0                                                        #  varialbe used to store tile's value
        row_index = 0                                                   #  varialbe used to represent the each row
        states_for_each_row = [ ]                                       # a list to store all the rows states that the list can be collapse or not
        
        # make tiles's sequence in each colum opposite, we can use the same way that we did in CollapseUP
        for col_index in range(self.col):
            while (row_index != self.row - row_index) and (row_index < self.row - row_index -1):
                temp = self.grid[row_index][col_index]
                self.grid[row_index][col_index] = self.grid[self.row - row_index-1][col_index]
                self.grid[self.row-row_index-1][col_index] = temp
                row_index += 1
            row_index = 0
       
        # change each colum into row
        for col_index in range(self.col):
            for row_index in range(self.row):
                new_tiles.append(self.grid[row_index][col_index])
                
            lst,state = self.collapseRow(new_tiles)                         #  we can use the arrtibute since all the coulms are rows now
            states_for_each_row.append(state)                                
            
        # store the answer back to the self.grid 
            for row_number in range(self.row):
                self.grid[row_number][col_number] = new_tiles[row_number]
            col_number += 1
            new_tiles = [ ] 
        
        # we need to change the sequence back to the origin
        row_index = 0
        for col_index in range(self.col):
            while (row_index != self.row - row_index) and (row_index < self.row - row_index -1):
                temp = self.grid[row_index][col_index]
                self.grid[row_index][col_index] = self.grid[self.row - row_index-1][col_index]
                self.grid[self.row-row_index-1][col_index] = temp
                row_index += 1
            row_index = 0
        for state in states_for_each_row:
            if state == True:
                return True
        
        return False

class Game():
    def __init__(self, row=4, col=4, initial=2):
        self.game = Grid(row, col, initial)
        self.play()


    def printPrompt(self):
        if sys.platform == 'win32':
            os.system("cls")
        else:
            os.system("clear")
        print('Press "w", "a", "s", or "d" to move Up, Left, Down or Right respectively.')
        print('Enter "p" to quit.\n')
        self.game.drawGrid()
        print('\nScore: ' + str(self.game.score))


    def play(self):

        moves = {'w' : 'Up',
                 'a' : 'Left',
                 's' : 'Down',
                 'd' : 'Right'}

        stop = False
        collapsible = True

        while not stop and collapsible:
            self.printPrompt()
            key = input('\nEnter a move: ')

            while not key in list(moves.keys()) + ['p']:
                self.printPrompt()
                key = input('\nEnter a move: ')

            if key == 'p':
                stop = True
            else:
                move = getattr(self.game, 'collapse' + moves[key])
                collapsed = move()

                if collapsed:
                    self.game.updateEmptiesSet()
                    self.game.assignRandCell()

                collapsible = self.game.collapsible()

        if not collapsible:
            if sys.platform == 'win32':
                os.system("cls")
            else:
                os.system("clear")
            print()
            self.game.drawGrid()
            print('\nScore: ' + str(self.game.score))
            print('No more legal moves.')


# -----------------------------------------------------------------------------
# Main Function ---------------------------------------------------------------
# -----------------------------------------------------------------------------
def main():
    game = Game()
main()


# This condition ensures that the game isn't run if the file is loaded as
# a module. Will only run if the file is executed.

if __name__ == '__main__':
    game = Game()
