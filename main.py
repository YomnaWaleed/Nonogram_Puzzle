from Nongoram2 import Nonogram
"""
create object from class
generate puzzle
print unsolved puzzle
solve puzzle 
print solved puzzle 
"""
test = Nonogram()
test.generate_puzzle()
# test.visualize_nonogram(test.puzzle, test.rows, test.cols)
test.solve()
test.visualize_nonogram(test.puzzle, test.rows, test.cols)
