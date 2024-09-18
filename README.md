# cosc550final
Overview
This project is an implementation of the Saboteur board game, where players take on roles as either Gold-Diggers or Saboteurs. The goal of the game for Gold-Diggers is to build a path to reach the hidden gold, while Saboteurs attempt to block them. The game includes both human players and AI-controlled agents, with the AI using Monte Carlo Tree Search (MCTS) to make intelligent decisions based on future simulations of the game state.

**Features**
Interactive Game Board: Dynamically updated board with paths and action cards that represent the game’s progress.
AI Agents with MCTS: AI players use Monte Carlo Tree Search to evaluate possible future states and select optimal actions.
Hidden Information: Players are assigned secret roles (Gold-Digger or Saboteur) and the game involves unrevealed goal cards, adding layers of strategy.
Human vs. AI or AI-only: Supports human players interacting with AI agents or AI-only games.
Endgame Summary: Display the winning team and provide a summary of key moves in the game.
Project Structure
The project is broken into several Python files that handle different parts of the game's logic:

agent_program.py: Defines the agent structure, including sensors and actuators used by players to interact with the game environment.
card.py: Handles the structure and rules for cards (path cards and action cards).
deck.py: Manages the deck of cards, including shuffling and drawing cards.
game_board.py: Contains the logic for the game board, where players place path cards to reach the hidden goal.
mcts_agent.py: Implements the Monte Carlo Tree Search (MCTS) algorithm for AI agents.
mcts_functions.py: Provides helper functions for running MCTS simulations, backpropagation, and decision-making.
saboteur_app.py: The main application file that runs the game loop, handles player actions, and manages game progression.
saboteur_base_environment.py: Defines the game environment, handling state transitions, legal actions, and checking for terminal states.
saboteur_player.py: Defines the player class, handling the player's hand of cards and their interactions with the game board.
AI Techniques Used
This project implements Monte Carlo Tree Search (MCTS) as the core decision-making technique for AI agents:

**Monte Carlo Tree Search (MCTS): **The AI performs simulations of possible future game states, balancing exploration (trying new moves) and exploitation (focusing on known good moves). This technique is particularly effective in games with hidden information and randomness, like Saboteur.
Random Playouts: During the simulation phase, the AI performs random playouts to estimate the value of each action.
Backpropagation: The results of the simulations are used to update the decision tree, guiding future decisions for the AI.
Why MCTS?
MCTS was chosen for this project due to its ability to handle uncertainty (hidden goals and player roles) and randomness (card draws) effectively. It provides a balance between exploring new strategies and exploiting known successful ones, making it a versatile tool for both Gold-Digger and Saboteur roles.

**How to Play**
Player Roles: At the beginning of the game, each player is assigned a secret role: Gold-Digger (trying to reach the goal) or Saboteur (trying to block others).

Taking Actions: Players take turns performing one of the following actions:

Placing a path card to extend the tunnel toward the goal.
Playing an action card to affect other players (e.g., breaking their tools or revealing goals).
Passing the turn if no legal actions are available.
Winning Conditions:

Gold-Diggers Win: If a path is successfully built to the hidden gold.
Saboteurs Win: If the path is blocked, or if the deck runs out and the goal is not reached.
