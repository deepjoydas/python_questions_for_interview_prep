# Questions

## Question No 1
    write a function solution that given a string S containing of N letters 'a' and/or 'b' returns True when all occurrences of letter 'a' are before all occurrences of letter 'b' and return false otherwise

    - Given S="aabbb", the function should return True
    - Given S="ba" the function should return False
    - Given S="aaa" the function should return True. Note that 'b' does not need to occur in S
    - Given S="b", the function should return True. Note that 'a' does not need to occur in S
    - Given S="abba", the function should return False

### Answer: code1.py

## Question No 2
    We are given a two-dimensional board of size NxM (N rows and M columns). Each filed of  the board can be empty ('.') may contain an obstacle ('X') or may have a character in it. The character might be either an assassin ('A') or a guard. Each guard stands still and looks straight ahead in the direction they are facing. Every guard look sin one of four directions (up, down, left or right on the board) and is represented by one of four symbols. A guard denoted by '<' is looking to the left; by '>', to the right; '^', up; or 'v', down. The guards can see everything in a straight line in the direction in which that are facing as far as the first obstacle ('X' or any other guard) or the edge of the board. The assassin can move from the current field to any other empty field with a shared edge. The assassin cannot move onto fields containing obstacles or enemies. 

    ```python
    Write a function in python:
    
    def solution(B)
    ```

    That given an array B containing of N strings denoting rows of the array, return True if is it possible for the assassin to sneak from their current location to the bottom right cell of the board undetected and false otherwise.

        - 1. Given B=["X.....>","..v..X.",".>..X..","A......"], your function should return False. All available paths lead through a filed observed by a guard

        - 2. Given B=["...Xv","AX..^",".XX.."], your function should return True. The guard in the second row is blocking the other one from watching the bottom right square.

        - 3. Given B=["...",">.A"] your function should return False, as the assassin gets spotted right at the start.

        - 4. Given B=["A.v",..."], your function should return False. Its not possible for the assassin to enter the bottom right cell undetected as the cell is observed

            - Assume N is an integer with range [1..500]
            - all strings in B are of the same length M from range [1..500]
            - there is exactly one assassin on the board
            - there is no guard or wall on B[N-1][M-1]
            - every string in B consists only of the following characters '.','X','<','>','v','^' and/or 'A'

### Answer: code2.py

## Question No 3.
    You are given a data set called biopics.csv containing information on biographical movies. Your task is to perform some data manipulations on the biopics data.

    Data Overview

    The original biopics data are made available by the analytics website FiveThirtyEight. You will be working with a preprocessed version, available for you at biopics.csv. It contains the following columns:

    'title' - the movie's title
    'country' - country of production
    'year_release' - the year the movie was released
    'box_office' - movie's earning at the box office, in US$
    'type_of_subject' - the occupation of the movie's subject or their reason for recognition
    'lead_actor_actress' - the name of the actor or actress who played the subject

    Write a function named ```process_data()``` that takes no arguments. The function should lead the biopics data (this has been implemented for you), perform data manipulations described below and return a pandas data frame with manipulated data.

    Clean up the biopics data:

    Filter our duplicated row
    Rename the variable called box_office to earnings
    Filter out rows for which earnings are missing (i.e. they are NaN)
    Keep only movies relased in the year 1990 or later
    Convert the type of type_of_subject and country to Categorical 
    Create a new variable called lead_actor_actress_known that is False if lead_actor_actress is NaN and True otherwise
    Update earnings which they are expressed in million of dollars instead of dollars 
    Recorder the columns in the data frame such that thet are in the following order: title, year_release, # earnings, country, type_of_subject, lead_actor_actress, lead_actor_actress_known
    Sort the rows in descending order by earnings

    On the top of the python standard library you can make use of any function from the pandas and numpy packages