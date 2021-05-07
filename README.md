# Gomoku
 AI for 2021 ESC190 Gomoku Competition (Silver Placement)
 
 The AI plays 8x8 gomoku, implemented in [gomoku.py](gomoku.py) \
 [standard_ai.py](standard_ai.py) and [blitz_ai.py](blitz_ai.py) are very similar, but designed to return moves in 2.0 seconds and 0.2 seconds respectively. 
 Both use iteratively deepening alphabeta minimax with a greedy heuristic to select which positions to explore. Evaluation of positions is accomplished by computing the 
 change in score as a result of each move, facilitated by a lookup tables that stores the scores for each type individual of row/column/diagonal possible on the board.
