assignments = []

rows = "ABCDEFGHI"
cols = "123456789"

def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [letter + num for letter in A for num in B]

boxes = cross(rows, cols)
row_units = [cross(r, cols) for r in rows]
col_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')]
diagonal_left = [[a[0] + a[1] for a in zip(rows, cols)]]
diagonal_right = [[a[0] + a[1] for a in zip(rows, cols[::-1])]]
unitlist = row_units + col_units + square_units + diagonal_left + diagonal_right
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)


def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """

    # Find all instances of naked twins
    visited = set()
    ntlist = []
    for box, peer in peers.items():
        if len(values[box]) == 2:
            target = values[box]
            for p in peer:
                if values[p] == target:
                    if (box, p) not in visited and (p, box) not in visited:
                        ntlist.append((box, p))
                        visited.add((box, p))
                        visited.add((p, box))
    # Eliminate the naked twins as possibilities for their peers
    if not ntlist:  # No naked twins
    	return values
    else:  # Naked twins exit
    	for nt in ntlist:
    		v = values[nt[0]]
    		for peer in peers[nt[0]]:
    			if peer in peers[nt[1]] and v[0] in values[peer]:
    				new_value = values[peer].replace(v[0], '')
    				values = assign_value(values, peer, new_value)
    			if peer in peers[nt[1]] and v[1] in values[peer]:
    				new_value = values[peer].replace(v[1], '')
    				values = assign_value(values, peer, new_value)
    	return values

def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    chars = []
    digits = '123456789'
    for c in grid:
        if c in digits:
            chars.append(c)
        if c == ".":
            chars.append(digits)
    assert len(chars) == 81
    return dict(zip(boxes, chars))

def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    print

def eliminate(values):
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    for box in solved_values:
        digit = values[box]
        for peer in peers[box]:
        	new_value = values[peer].replace(digit,'')
        	values = assign_value(values, peer, new_value)
    return values

def only_choice(values):
    for unit in unitlist:
        for digit in '123456789':
            digit_count = [box for box in unit if digit in values[box]]
            if len(digit_count) == 1:
                values = assign_value(values, digit_count[0], digit)
    return values

def reduce_puzzle(values):
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    stalled = False
    while not stalled:
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        values = eliminate(values)
        values = only_choice(values)
        values = naked_twins(values)  # Add naked twins as a part of the strategy
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        stalled = solved_values_before == solved_values_after
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

def search(values):
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)
    if values is False:
        return False
    # Need this base case to return the solved value of sudoku
    if all(len(values[box]) == 1 for box in boxes):
        return values
    # Choose one of the unfilled squares with the fewest possibilities
    min_l, min_index = min((len(values[box]), box) for box in boxes if len(values[box]) > 1)
    # Now use recursion to solve each one of the resulting sudokus, and if one returns a value (not False), return that answer!
    for value in values[min_index]:
        new_sudoku = values.copy()
        new_sudoku = assign_value(new_sudoku, min_indx, value)
        attempt = search(new_sudoku)
        if attempt:
            return attempt

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    values = grid_values(grid)
    return search(values)

if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
