from collections import deque

def is_palindrome(input_str):
    input_str = input_str.replace(" ", "").lower()
    
    char_queue = deque()
    
    for char in input_str:
        char_queue.append(char)

    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False
    
    return True

print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("racecar"))                     # True
print(is_palindrome("hello"))                       # False
