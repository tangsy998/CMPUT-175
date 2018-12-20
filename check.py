import assignment2 as game

def testCollapseRow():
    print("Running tests for collapseRow()")
    grid = game.Grid()

    a = [0, 0, 4, 0]
    b = [2, 2, 4, 0]
    c = [2, 2, 4, 4]
    d = [2, 4, 8, 16]
    e = [0, 0, 0, 0]
    f = [2, 2, 2, 2]
    g = [2, 2, 0, 2, 2]

    a_sol = ([4, 0, 0, 0], True)
    b_sol = ([4, 4, 0, 0], True)
    c_sol = ([4, 8, 0, 0], True)
    d_sol = ([2, 4, 8, 16], False)
    e_sol = ([0, 0, 0, 0], False)
    f_sol = ([4, 4, 0, 0], True)
    g_sol = ([4, 4, 0, 0, 0], True)

    if grid.collapseRow(a) == a_sol:
        print("Test (a) passed.")
    else:
        print("Test (a) failed")

    if grid.collapseRow(b) == b_sol:
        print("Test (b) passed.")
    else:
        print("Test (b) failed")

    if grid.collapseRow(c) == c_sol:
        print("Test (c) passed.")
    else:
        print("Test (c) failed")

    if grid.collapseRow(d) == d_sol:
        print("Test (d) passed.")
    else:
        print("Test (d) failed")

    if grid.collapseRow(e) == e_sol:
        print("Test (e) passed.")
    else:
        print("Test (e) failed")

    if grid.collapseRow(f) == f_sol:
        print("Test (f) passed.")
    else:
        print("Test (f) failed")

    if grid.collapseRow(g) == g_sol:
        print("Test (g) passed.")
    else:
        print("Test (g) failed")


def testCollapseLeft():
    print("Running test for collapseLeft()")
    grid = game.Grid()
    grid.grid = [[0, 0, 0, 0],
                  [2, 2, 0, 4],
                  [2, 0, 2, 16],
                  [4, 4, 4, 2]]

    sol = [[0, 0, 0, 0],
           [4, 4, 0, 0],
           [4, 16, 0, 0],
           [8, 4, 2, 0]]

    grid.collapseLeft()
    test = grid.grid

    if sol == test:
        print("Test (a) passed.")
    else:
        print("Test (a) failed.")

    grid.grid = [[2, 2, 2, 2],
                  [2, 2, 2, 2],
                  [2, 2, 2, 2],
                  [2, 2, 2, 2]]

    sol = [[4, 4, 0, 0],
           [4, 4, 0, 0],
           [4, 4, 0, 0],
           [4, 4, 0, 0]]

    grid.collapseLeft()
    test = grid.grid

    if sol == test:
        print("Test (b) passed.")
    else:
        print("Test (b) failed.")

    grid.grid = [[0, 0, 0, 4],
                  [0, 0, 0, 2],
                  [0, 0, 0, 4],
                  [0, 0, 0, 2]]

    sol = [[4, 0, 0, 0],
           [2, 0, 0, 0],
           [4, 0, 0, 0],
           [2, 0, 0, 0]]

    grid.collapseLeft()
    test = grid.grid

    if sol == test:
        print("Test (c) passed.")
    else:
        print("Test (c)failed.")


def testCollapseRight():
    print("Running test for collapseRight()")
    grid = game.Grid()
    grid.grid = [[0, 0, 0, 0],
                  [2, 2, 0, 4],
                  [2, 0, 2, 16],
                  [4, 4, 4, 2]]

    sol = [[0, 0, 0, 0],
           [0, 0, 4, 4],
           [0, 0, 4, 16],
           [0, 4, 8, 2]]

    grid.collapseRight()
    test = grid.grid

    if sol == test:
        print("Test (a) passed.")
    else:
        print("Test (a) failed.")

    grid.grid = [[2, 2, 2, 2],
                  [2, 2, 2, 2],
                  [2, 2, 2, 2],
                  [2, 2, 2, 2]]

    sol = [[0, 0, 4, 4],
           [0, 0, 4, 4],
           [0, 0, 4, 4],
           [0, 0, 4, 4]]

    grid.collapseRight()
    test = grid.grid

    if sol == test:
        print("Test (b) passed.")
    else:
        print("Test (b) failed.")

    grid.grid = [[0, 0, 0, 4],
                  [2, 0, 0, 0],
                  [0, 4, 0, 0],
                  [0, 0, 0, 2]]

    sol = [[0, 0, 0, 4],
           [0, 0, 0, 2],
           [0, 0, 0, 4],
           [0, 0, 0, 2]]

    grid.collapseRight()
    test = grid.grid

    if sol == test:
        print("Test (c) passed.")
    else:
        print("Test (c) failed.")


def testCollapseDown():
    print("Running test for collapseDown()")
    grid = game.Grid()
    grid.grid = [[2, 8, 2, 4],
                  [8, 4, 8, 2],
                  [2, 4, 2, 4],
                  [4, 2, 4, 2]]

    sol = [[2, 0, 2, 4],
           [8, 8, 8, 2],
           [2, 8, 2, 4],
           [4, 2, 4, 2]]

    grid.collapseDown()
    test = grid.grid

    if sol == test:
        print("Down (a) passed.")
    else:
        print("Test (a) failed.")

    grid = game.Grid(row=5, col=5)
    grid.grid = [[2, 8, 2, 4, 0],
                  [8, 4, 8, 2, 0],
                  [2, 4, 2, 4, 0],
                  [4, 2, 4, 2, 0],
                  [4, 4, 8, 0, 2]]

    sol = [[0, 0, 2, 0, 0],
           [2, 8, 8, 4, 0],
           [8, 8, 2, 2, 0],
           [2, 2, 4, 4, 0],
           [8, 4, 8, 2, 2]]

    grid.collapseDown()
    test = grid.grid

    if sol == test:
        print("Down (b) passed.")
    else:
        print("Test (b) failed.")


def testCollapseUp():
    print("Running test for collapseUp()")
    grid = game.Grid()
    grid.grid = [[2, 8, 2, 4],
                  [8, 4, 8, 2],
                  [2, 4, 2, 4],
                  [4, 2, 4, 2]]

    sol = [[2, 8, 2, 4],
           [8, 8, 8, 2],
           [2, 2, 2, 4],
           [4, 0, 4, 2]]

    grid.collapseUp()
    test = grid.grid

    if sol == test:
        print("Down (a) passed.")
    else:
        print("Test (a) failed.")

    grid = game.Grid(row=5, col=5)
    grid.grid = [[2, 8, 2, 4, 0],
                  [8, 4, 8, 2, 0],
                  [2, 4, 2, 4, 0],
                  [4, 2, 4, 2, 0],
                  [4, 4, 8, 0, 2]]

    sol = [[2, 8, 2, 4, 2],
           [8, 8, 8, 2, 0],
           [2, 2, 2, 4, 0],
           [8, 4, 4, 2, 0],
           [0, 0, 8, 0, 0]]

    grid.collapseUp()
    test = grid.grid

    if sol == test:
        print("Down (b) passed.")
    else:
        print("Test (b) failed.")


def testCollapsible():
    print("Running test for collapsible()")
    grid = game.Grid()

    grid.emptiesSet = [0, 1, 2, 3, 4, 5, 6, 8]
    grid.grid = [[0, 0, 0, 0],
                  [0, 0, 0, 4],
                  [2, 0, 2, 16],
                  [2, 4, 4, 2]]

    if grid.collapsible():
        print('Test (a) passed.')
    else:
        print('Test (a) failed.')

    grid.emptiesSet = []
    grid.grid = [[2, 8, 2, 4],
                  [4, 2, 8, 2],
                  [16, 8, 2, 4],
                  [2, 4, 8, 2]]

    if not grid.collapsible():
        print('Test (b) passed.')
    else:
        print('Test (b) failed.')

    grid.emptiesSet = []
    grid.grid = [[2, 8, 2, 4],
                   [8, 4, 8, 2],
                   [2, 4, 2, 4],
                   [4, 2, 4, 2]]

    if grid.collapsible():
        print('Test (c) passed.')
    else:
        print('Test (c) failed.')

    grid.emptiesSet = []
    grid.grid = [[2, 4, 2, 4],
                   [4, 2, 4, 2],
                   [2, 4, 2, 4],
                   [4, 2, 4, 2]]

    if not grid.collapsible():
        print('Test (d) passed.')
    else:
        print('Test (d) failed.')

def emptiesEquality(lst_1, lst_2, row, col):
    empty_1 = []
    empty_2 = []


    for tile in lst_1:
        empty_1.append((row * tile[0]) + (tile[1]))

    for tile in lst_2:
        empty_2.append((row * tile[0]) + (tile[1]))

    return empty_1 == empty_2

def testEmpties():
    print("Running test for updateEmptiesSet()")
    grid = game.Grid()
    grid.grid = [[0, 0, 0, 0],
                  [0, 0, 0, 4],
                  [2, 0, 2, 16],
                  [2, 4, 4, 0]]
    grid.updateEmptiesSet()
    truth = [[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [1, 2], [2, 1], [3, 3]]
    if emptiesEquality(grid.emptiesSet, truth, 4, 4):
        print('Test (a) passed.')
    else:
        print('Test (a) failed.')

    grid.grid = [[0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0]]
    grid.updateEmptiesSet()
    truth = [[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [1, 2], [1, 3], [2, 0], [2, 1], [2, 2], [2, 3], [3, 0], [3, 1], [3, 2], [3, 3]]
    if emptiesEquality(grid.emptiesSet, truth, 4, 4):
        print('Test (b) passed.')
    else:
        print('Test (b) failed.')

    grid = game.Grid(row=5, col=5)
    grid.grid = [[0, 0, 0, 0, 0],
                  [0, 0, 0, 4, 4],
                  [2, 0, 2, 16, 0],
                  [2, 4, 4, 2, 0],
                  [0, 4, 4, 0, 2]]
    grid.updateEmptiesSet()
    truth = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 1], [1, 2], [2, 1], [2, 4], [3, 4], [4, 0], [4, 3]]
    if emptiesEquality(grid.emptiesSet, truth, 5, 5):
        print('Test (c) passed.')
    else:
        print('Test (c) failed.')



# Uncomment the tests for the function you want to check

testCollapseRow()
testCollapseLeft()
testCollapseRight()
testCollapsible()
testEmpties()
testCollapseDown()
testCollapseUp()
