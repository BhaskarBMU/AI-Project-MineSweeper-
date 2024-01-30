# AI-Project-MineSweeper-

The objective of this project is to develop an intelligent AI agent capable of playing Minesweeper, a classic puzzle game, with high efficiency and accuracy. The game involves a grid of cells, some of which contain hidden mines. The player's task is to uncover all cells without mines based on numerical clues given by uncovered cells, which indicate the number of adjacent mines.

To achieve this, the AI agent will be designed using Constraint Satisfaction Problem (CSP) methodologies. CSP is a paradigm for solving combinatorial problems that involve making decisions under constraints. In the context of Minesweeper, the constraints are derived from the rules of the game, such as the number of adjacent mines to a cell and the total number of mines on the board. Simultaneously, a Table Driven approach will be utilized, where a predefined table maps specific game states (percepts) to corresponding actions. This table will encapsulate various scenarios the AI might encounter, allowing for rapid and efficient decision-making.

**** Methodology

**In our Game we have created two ways of playing the Minesweeper.First Involves the table driven approach and second through CSP(Constraint Satisfaction Problem).
**Table Driven Approach
**This approach is a method in artificial intelligence that uses a table to look up actions based on percepts (sensory inputs).

**1.1.1 Percepts
**
In the context of this Minesweeper AI, percepts are the information that the AI receives about the game state. This includes:

State: The state of each cell (whether it's a mine, safe, or unknown).
Number of mines: The number of mines surrounding a particular cell.
Cells Visited: Which cells have already been clicked.

****1.1.2  Actions (Possible Moves)
****
Actions are the responses or moves that the AI can make based on its percepts. In Minesweeper, these actions include:

Mine: Marking a cell as a mine.
Safe: Marking a cell as safe.
Reveal: Choosing a cell to reveal next.         

**1.1.3 Percept to Action Mapping Table
**

![image](https://github.com/BhaskarBMU/AI-Project-MineSweeper-/assets/114286743/cfae8acd-1df3-4525-a9fd-598dcc986153)





