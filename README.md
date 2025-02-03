# PASSWORD MODULE SOLVER FOR "Keep Talking and Nobody Explodes"

This project provides a Python script to solve the Passwort module in the game Keep Talking and Nobody Explodes (German version). The script helps players quickly determine possible words based on given letters.

### 1. How It Works
1. Word List:
        The script contains a predefined list of possible words in german that can appear in the password module.

2. User Input:
        The player inputs the available letters for the first, second and third columns when prompted.

3. Filtering Words:
        The script checks the word list and filters words that match the given letters in the first two columns.

4. Displaying Solutions:
        The possible solutions are printed.

### 2. Example Usage

**Input:**

```
Input first column: a n b d f
Input second column: n t e r o
Input third column: g e t o r
```

**Output:**

```
Possible solutions: angst, beten, ferse
```

### 3. How to Use
1. Clone the repository
2. Run the script in the terminal:
       ```
       python password_solver.py
       ```
3. Enter the letters for the first, second and third column when prompted.
4. View the possible solutions displayed in the output.

### 4. Improvement
Implement a graphical user interface for easier interaction.    
Add support for more languages.   
Include auto-detection   


### 5. Reference
Keep Talking and Nobody Explodes is developed by Steel Crate Games. This tool is an unofficial helper for the Passwort module in the German version of the game.
