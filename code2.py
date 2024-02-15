from collections import deque

def solution(B):
    N = len(B)
    M = len(B[0])

    # Directions for guards
    directions = {'<': (0, -1), '>': (0, 1), '^': (-1, 0), 'v': (1, 0)}

    # Function to check if a position is within the board
    def is_valid(row, col):
        return 0 <= row < N and 0 <= col < M

    # Function to perform BFS from the assassin's position
    def bfs(start_row, start_col):
        queue = deque([(start_row, start_col)])
        visited = set()
        visited.add((start_row, start_col))

        while queue:
            row, col = queue.popleft()

            # If we reach the bottom-right cell, return True
            if row == N - 1 and col == M - 1:
                return True

            # Explore all adjacent cells
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_row, new_col = row + dr, col + dc

                # Check if the new position is valid and not visited
                if is_valid(new_row, new_col) and (new_row, new_col) not in visited:
                    visited.add((new_row, new_col))

                    # If the new position is empty, add it to the queue
                    if B[new_row][new_col] == '.':
                        queue.append((new_row, new_col))
                    # If the new position is a guard, mark all positions in its line of sight as observed
                    elif B[new_row][new_col] in directions:
                        dr, dc = directions[B[new_row][new_col]]
                        r, c = new_row + dr, new_col + dc
                        while is_valid(r, c) and B[r][c] != 'X':
                            if B[r][c] == 'A':
                                return False  # Assassin spotted
                            visited.add((r, c))
                            r += dr
                            c += dc

        return False

    # Start BFS from the assassin's initial position
    return bfs(0, 0)

# Test cases
print(solution(["X.....>", "..v..X.", ".>..X..", "A......"]))  # Output: False
print(solution(["...Xv", "AX..^", ".XX.."]))  # Output: True
print(solution(["...", ">.A"]))  # Output: False
print(solution(["A.v", "..."]))  # Output: False