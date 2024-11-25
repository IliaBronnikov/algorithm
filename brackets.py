"""
Необходимо определить является ли строка правильным математическим выражение в плане скобок, т.е. каждой открытой скобки соотвествует закрытая.

Пример
() - True
) - False
((()))()) - False
"""

# Решение 1 - через стек
def check_bracket(bracket_str: str) -> bool:
    if len(bracket_str) == 0:
        return True

    stack = []

    for bracket in bracket_str:
        if bracket == "(":
            stack.append(bracket) 
        else:
            if stack:
                stack.pop()
            else:
                return False
    if stack:
        return False
    
    return True
    
  

# Решение 2 - через счетчик
def check_bracket(bracket_str: str) -> bool:
    bracket_mapping = {"(": 1, ")": -1}
    counter = 0
    
    for bracket in bracket_str:
        counter += bracket_mapping[bracket]
        if counter < 0:
            return False
    
    if not counter:
        return True
    
    return False
  
