
"""
empty sudoku
predefined sudoku
FIDP Seite 266-271
"""

from csp import CSP



def filter_values_by_key(dictionary, condition):
    return [v for k,v in dictionary.items() if condition(k)]


def sudoku_constraints(assignment):
    # Check lines and columns
    for k in (0,1):
        for ix in range(9):
            values = filter_values_by_key(assignment,
                                          lambda key: key[k] == ix)
            if len(values) != len(set(values)):
                return False
    # Check 3x3 blocks
    for i in range(3):
        for j in range(3):
            values = filter_values_by_key(assignment,
                     lambda key: (key[0] // 3, key[1] // 3) == (i,j))
            if len(values) != len(set(values)):
                return False
    # All constraints are satisfied
    return True
            

def print_sudoku(assignment):
    print()
    for i in range(9):
        print(("+-" * 10)[:-1])
        print('|', end='')
        for j in range(9):
            print(assignment.get((i,j), ' '), '|', sep='', end='')
        print()
    print(("+-" * 10)[:-1])



# Define variables and domains
variables = [(i,j) for i in range(9) for j in range(9)]
domains = {t: list(range(1, 10)) for t in variables}



# Demo
if __name__ == '__main__':
    # Predefined sudoku
    s = """\
...15....
5.8..4.1.
1.4.8...3
..7..654.
8...2.9.7
....3...2
.8.5...9.
916.438..
.....7...
"""
    
    s = s.strip().replace('\n', '')
    assert len(s) == 9*9, "bad number"
    
    domains = dict()
    pre_assignment = dict()
    
    for ix,char in enumerate(s):
        i,j = divmod(ix, 9)
        if 49 <= ord(char) <= 57:
            domains[(i,j)] = [int(char)]
            pre_assignment[(i,j)] = int(char)
        else:
            domains[(i,j)] = list(range(1,10))
    
    # Solve sudoku
    csp = CSP(variables, domains, sudoku_constraints)
    assignment = csp.solve(pre_assignment)
    print_sudoku(assignment)
    

