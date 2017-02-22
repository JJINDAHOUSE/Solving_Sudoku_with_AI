# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: Apply constraint propagation to solve the naked twins problem allows us to effectively reduce the number of potential answers among their peers. In other words, we have a higher chance to obtain unique number among their peers. Assume the naked twins permit the values of v1 and v2. Thevalues v1 and v2 are locked in for those two boxes. As a result, no other box in their same unit can contain the value v1 or v2. It reduces the possibilities for their peers. Therefore, repeatlly apply naked twins strategy can help us solve the sudoku faster.

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: Diagonal sudoku intorduces a new constraint that 1 to 9 can only appears once on each diagonal. This constraint limit the number of potential answers among each unit. Therefore, applying constraint propagation can effectively reduce the number of potential answers among each unit. In order words, it increase the possibility of unique number in each box and we can solve diagonal sudoku faster by using constraint propagation.

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