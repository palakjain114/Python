def to_lowercase(s):
    result = ''
    for char in s:
        if 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char
    return result

def to_uppercase(s):
    result = ''
    for char in s:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    return result

def toggle_case(s):
    result = ''
    for char in s:
        if 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        elif 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    return result

input_string = input()
print(to_lowercase(input_string))
print(to_uppercase(input_string))
print(toggle_case(input_string))
    
    
