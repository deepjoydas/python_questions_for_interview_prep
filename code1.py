def solution(S):
    seen_b = False
    
    for char in S:
        if char == 'b':
            seen_b = True
        elif seen_b:
            return False
    
    return True

# Test cases
print(solution("aabbb"))  # Output: True
print(solution("ba"))     # Output: False
print(solution("aaa"))    # Output: True
print(solution("b"))      # Output: True
print(solution("abba"))   # Output: False