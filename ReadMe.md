# Question

## 1. write a function solution that given a string S containing of N letters 'a' and/or 'b' returns True when all occurrences of letter 'a' are before all occurrences of letter 'b' and return false otherwise

    - Given S="aabbb", the function should return True
    - Given S="ba" the function should return False
    - Given S="aaa" the function should return True. Note that 'b' does not need to occur in S
    - Given S="b", the function should return True. Note that 'a' does not need to occur in S
    - Given S="abba", the function should return False

### Answer: code1.py

## 2. We are given a two-dimensional board of size NxM (N rows and M columns). Each filed of  the board can be empty ('.') may contain an obstacle ('X') or may have a character in it. The character might be either an assassin ('A') or a guard. Each guard stands still and looks straight ahead in the direction they are facing. Every guard look sin one of four directions (up, down, left or right on the board) and is represented by one of four symbols. A guard denoted by '<' is looking to the left; by '>', to the right; '^', up; or 'v', down. The guards can see everything in a straight line in the direction in which that are facing as far as the first obstacle ('X' or any other guard) or the edge of the board. The assassin can move from the current field to any other empty field with a shared edge. The assassin cannot move onto fields containing obstacles or enemies. 

    - Write a function in python:

    - def solution(B)

    - That given an array B containing of N strings denoting rows of the array, return True if is it possible for the assassin to sneak from their current location to the bottom right cell of the board undetected and false otherwise.

        - 1. Given B=["X.....>","..v..X.",".>..X..","A......"], your function should return False. All available paths lead through a filed observed by a guard

        - 2. Given B=["...Xv","AX..^",".XX.."], your function should return True. The guard in the second row is blocking the other one from watching the bottom right square.

        - 3. Given B=["...",">.A"] your function should return False, as the assassin gets spotted right at the start.

        - 4. Given B=["A.v",..."], your function should return False. Its not possible for the assassin to enter the bottom right cell undetected as the cell is observed

            - Assume N is an integer with range [1..500]
            - all strings in B are of the same length M from range [1..500]
            - there is exactly one assassin on the board
            - there is no guard or wall on B[N-1][M-1]
            - every string in B consists only of the following characters '.','X','<','>','v','^' and/or 'A'
