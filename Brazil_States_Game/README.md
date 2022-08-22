### Guess the Brazil States game

A python game with a basic GUI. The player tries to write correctly the name of all the brazilian states.  
For each right guess, the name of the state is writen inside (or near) it and the counter is upgraded.


### Why I used this project ?

To start working with CSV Data and the `pandas` library.


### What I did different

It is possible to edit this game to play with any country, continent, etc. Here is how:  
1. Use the GIF image you want and edit its name in main.py;  
2. Edit the NUMBER_OF_STATES to the number of states the player will try to guess;  
3. Prepare the states.txt with the names of the states, one per line.  
4. Run the buildcsv_coor.py script and click inside each of the states in the same order they are in the states.txt.  
Teses steps will add the coordinates to each state and create a CSV file from this data, ready to play.

### How to use?

To play, you can run the main.py script from the command-line.


### Setup

This script was created using `python 3.10`.

The project depends on the `pandas` and `turtle` libraries, install them with pip:  
`pip install pandas`  
`pip install turtle`


### Possible improvements

- A timer coulb be implemented. Adding time for right guesses and subtracting for wrong ones.
- The guessed states coulb be painted.


### Contributing

You are welcome to contribute sending feedbacks about the code. For that, reach me at [LinkedIn](https://www.linkedin.com/in/tuliobegena).

You are also welcome to contribute to the code via pull requests, of course.

### Vindications
The writer_turtle.py I used just to test the import.
