Code Structure:
The program has been organised within 2 files; maxconnect4.py and MaxConnect4Game.py

maxconnect4.py has all the functions and it accepts the user inputs initially, sets up the board and calls the subsequent AI algorithms.

MaxConnect4Game.py has the function implementation of the AI algorithms and the evaluation function.


Syntax:
Interactive Mode Syntax :
(Make sure the input.txt file is on the same path of the python script)

Sample command to be run on command line.
python maxconnect4.py interactive input_file computer-next/human-next depth 

One-move Mode Syntax :

python maxconnect4.py one-move input_file output_file depth
