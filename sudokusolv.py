# Import PuLP modeler functions
from pulp import *
import main



# The Vals, Rows and Cols sequences all follow this form
Vals = Rows = Cols = range(1,10)

# The boxes list is created, with the row and column index of each square in each box
Boxes = [
    [(3 * i + k + 1, 3 * j + l + 1) for k in range(3) for l in range(3)]
    for i in range(3)
    for j in range(3)
]
# The prob variable is created to contain the problem data
prob = LpProblem("Sudoku Problem", LpMinimize)

# The problem variables are created
choices = LpVariable.dicts("Choice", (Vals, Rows, Cols), cat="Binary")

# The arbitrary objective function is added
prob += 0, "Arbitrary Objective Function"

# Constraint ensuring that only one value can be in each square is created
for r in Rows:
    for c in Cols:
        prob += lpSum([choices[v][r][c] for v in Vals]) == 1, ""

# The row, column and box constraints are added for each value
for v in Vals:
    for r in Rows:
        prob += lpSum([choices[v][r][c] for c in Cols]) == 1, ""

    for c in Cols:
        prob += lpSum([choices[v][r][c] for r in Rows]) == 1, ""

    for b in Boxes:
        prob += lpSum([choices[v][r][c] for (r, c) in b]) == 1, ""

# The starting numbers are entered as constraints
vecs=test1.tvect.copy()


for (v,r,c) in test1.tvect:
    if v > 0:
        prob += choices[v][r][c] == 1,""

# The problem data is written to an .lp file
prob.writeLP("Sudoku.lp")

# The problem is solved using PuLP's choice of Solver
prob.solve()

# The status of the solution is printed to the screen
print("Status:", LpStatus[prob.status])

# A file called sudokuout.txt is created/overwritten for writing to
sudokuout = open('sudokuout.txt', 'w')

# The solution is written to the sudokuout.txt file
for r in Rows:
    if r == 1 or r == 4 or r == 7:
        sudokuout.write("+-------+-------+-------+\n")
    for c in Cols:
        for v in Vals:
            if value(choices[v][r][c]) == 1:

                if c == 1 or c == 4 or c == 7:
                    sudokuout.write("| ")

                sudokuout.write(str(v) + " ")

                if c == 9:
                    sudokuout.write("|\n")
sudokuout.write("+-------+-------+-------+")
sudokuout.close()


# The location of the solution is give to the user
print("Solution Written to sudokuout.txt")
