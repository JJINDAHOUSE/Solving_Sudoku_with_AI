# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: Assume the naked twins permit the values of v1 and v2. The values v1 and v2 are locked in for
   those two boxes. As a result, no other box in theri same unit can contain the value v1 or v2. It reduces the possibilities for their peers. After the reduction, we might have another pairs of naked twins and we can repeatlly apply naked twins strategy to obtain smaller size of new sudoku and finally solve it.

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: By adding diagonals as a part of the units, we only allow value 1 to 9 appears in the same
   column, row, 3 by 3 square, and diagonal once. We first select a box with unique value and apply the elimination strategy to reduce the possibilities, which will result a more complete sudoku. Then, we apply naked twins strategy and agian it will lead to a more complete sudoku. And then only choice strategy. We repeatlly apply these strategies to the sudoku until we solve it or it cannot be solved. 

### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solutions.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

### Data

The data consists of a text file of diagonal sudokus for you to solve.