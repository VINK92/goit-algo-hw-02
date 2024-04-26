def check_delimiters(input_str):
    stack = []

    pairs = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    for char in input_str:
        if char in pairs.keys():
            stack.append(char)
        elif char in pairs.values():
            if not stack or pairs[stack.pop()] != char:
                return "Несиметрично"
    if stack:
        return "Несиметрично"
    return "Симетрично"


print(check_delimiters("( ){[ 1 ]( 1 + 3 )( ){ }}"))  # Симетрично
print(check_delimiters("( 23 ( 2 - 3);"))            # Несиметрично
print(check_delimiters("( 11 }"))                    # Несиметрично
