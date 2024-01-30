# AI-Project-MineSweeper-

The objective of this project is to develop an intelligent AI agent capable of playing Minesweeper, a classic puzzle game, with high efficiency and accuracy. The game involves a grid of cells, some of which contain hidden mines. The player's task is to uncover all cells without mines based on numerical clues given by uncovered cells, which indicate the number of adjacent mines.

To achieve this, the AI agent will be designed using Constraint Satisfaction Problem (CSP) methodologies. CSP is a paradigm for solving combinatorial problems that involve making decisions under constraints. In the context of Minesweeper, the constraints are derived from the rules of the game, such as the number of adjacent mines to a cell and the total number of mines on the board. Simultaneously, a Table Driven approach will be utilized, where a predefined table maps specific game states (percepts) to corresponding actions. This table will encapsulate various scenarios the AI might encounter, allowing for rapid and efficient decision-making.

**Methodology**

**In our Game we have created two ways of playing the Minesweeper.First Involves the table driven approach and second through CSP(Constraint Satisfaction Problem).

**Table Driven Approach**

**This approach is a method in artificial intelligence that uses a table to look up actions based on percepts (sensory inputs).

**1.1.1 Percepts**

In the context of this Minesweeper AI, percepts are the information that the AI receives about the game state. This includes:

State: The state of each cell (whether it's a mine, safe, or unknown).
Number of mines: The number of mines surrounding a particular cell.
Cells Visited: Which cells have already been clicked.

**1.1.2  Actions (Possible Moves)**

Actions are the responses or moves that the AI can make based on its percepts. In Minesweeper, these actions include:

Mine: Marking a cell as a mine.
Safe: Marking a cell as safe.
Reveal: Choosing a cell to reveal next.         

**1.1.3 Percept to Action Mapping Table**

![image](https://github.com/BhaskarBMU/AI-Project-MineSweeper-/assets/114286743/cfae8acd-1df3-4525-a9fd-598dcc986153)


**Intelligent Agent**

**Introduction**

The Minesweeper AI is intricately crafted, relying on the potent framework of Constraint Satisfaction Problem (CSP) to overcome the complexities posed by the Minesweeper game. Unlike conventional algorithms like alpha-beta pruning or Minimax, the Minesweeper AI strategically employs CSP as its core methodology. The CSP approach systematically dissects Minesweeper, translating the challenge into variables, domains, and constraints. This allows the AI to deduce safe cell locations and strategically pinpoint potential mine placements.

**Key Components:**

CSP Foundation: The Minesweeper AI relies on CSP, unraveling the game's constraints to deduce safe moves and identify potential mine locations systematically.
Heuristic Evaluation: Intelligently integrating heuristic evaluation techniques enhances decision-making. These heuristics encapsulate strategic nuances, empowering the AI to make informed choices without exhaustive exploration.
Logical Exploration: The CSP-based strategy enables methodical exploration of possible mine configurations while adhering to game constraints.

This dual application of CSP and heuristic evaluation equips the Minesweeper AI with a sophisticated toolset. It navigates the Minesweeper puzzle adeptly, uncovering safe cells and deducing mine locations through a judicious blend of logic and strategic reasoning.

**Constraint Satisfaction Problems (CSP):**

Constraint Satisfaction Problem (CSP) forms the cornerstone of the Minesweeper AI's intelligence, providing a robust framework for systematic problem-solving. In the context of Minesweeper, CSP involves breaking down the game into variables, domains, and constraints, transforming the challenge into a set of solvable equations.

Key Aspects of CSP in Minesweeper AI:

Variable Definition: Mines, safe cells, and their interrelations become variables within the CSP framework.
Domain Specification: The possible values a variable can take on, such as the presence of a mine or a safe cell, constitute the domain.
Constraints Formulation: CSP translates Minesweeper's rules into constraints, defining the logical relationships between variables. For instance, the constraint might express that the number of neighboring mines should match the revealed number on a cell.

CSP empowers the Minesweeper AI to methodically explore configurations, deduce safe moves, and strategically identify potential mine locations through logical deduction.
 
**Heuristic Evaluation:**

**Mine Density Heuristic:**

Description: The agent dynamically adjusts its exploration strategy based on the mine density in the current area. Higher mine densities prompt the AI to be more cautious, while lower densities encourage more aggressive exploration. This adaptive approach ensures the AI's responsiveness to varying game conditions.
Formula: 
Mine Density = (Number of Mines in the Neighborhood) / (Total Number of Cells in the Neighborhood)

**Performance-based Heuristic:**

Description: The AI assesses its performance by computing the average success rate across multiple trials at different mine densities. This information guides the agent in refining its strategies, prioritizing actions that historically lead to better outcomes. It adapts its approach based on past experiences to enhance overall performance.
Formula: 
Performance = (Number of Successful Trials) / (Total Number of Trials)

**Cell Selection Heuristic:**

Description: The AI strategically selects cells for exploration by considering the potential impact on uncovering mines. It prioritizes cells with higher probabilities of containing mines, incorporating information from neighboring clues. This heuristic optimizes the AI's decision-making process, directing it towards areas where mines are more likely to be located.

**Formula:**

Probability = (Number of Hidden Mines Adjacent to the Cell) / (Total Number of Hidden Cells Adjacent to the Cell)



**Depth-limited Search Heuristic:**

Description: To manage computational complexity, the AI employs a depth-limited search. This heuristic ensures that the AI anticipates the consequences of its actions up to a certain depth, balancing computational efficiency with strategic decision-making. The depth-limited search prevents exhaustive exploration, focusing on relevant portions of the game space.
Formula:
Depth-limited Search Depth = d (specified depth for the search)



