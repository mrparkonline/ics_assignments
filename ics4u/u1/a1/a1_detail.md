# A1 - Scrabble

This assignment is partly started for you, you are to just finish coding the inner components of the uncompleted function.

The main goal of this assignment is to find the most common occurring scrabble score in the list of names provided to you in line 3.

In this assignment you are to finish the following functions:

**Function 1**

```
scrabble()
```

The **scrabble()** function takes in a string input and it returns the score of the given string.

**The Point System:**

- 1 point: E,A,I,O,N,R,T,L,S,U
- 2 points: D,G
- 3 points: B,C,M,P
- 4 points: F,H,V,W,Y
- 5 points: K
- 8 points: J,X
- 10 points: Q,Z
- Spaces & Special Characters are considered to be Zero

**Function 2**

```
scrabbleMode()
```

The **scrabbleMode()** function takes in a list input and it will output the most common/most occurring scrabble score. If there are more than 1 most occurring score, then the function returns -1

Example:

```
sample_list = ['B', 'C', 'M', 'P', 'AD', 'Q']

Expected Output
3
```

Explanation:

The score of 3 is the most occurring due to 'B', 'C', 'M', 'P', 'AD',
