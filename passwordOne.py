# == INSTRUCTIONS ==
#
# Purpose: Validate a password
# Parameters: one, a string
# Rules:
#   - It must be longer than 7 characters (8 is fine)
#   - It must contain at least one of the following special characters: `!`, `@`,
#     `$`, `%` or `&`
# Returns: a boolean (True if valid, False otherwise)
# Example:
#   Call:    is_valid("1234567")
#   Returns: False
#   Call:    is_valid("12345678")
#   Returns: False
#   Call:    is_valid("12345!78")
#   Returns: True


# def is_valid(password):
#   if len(password) <=7:
#     return False
#   elif "!" in password:
#     return True
#   elif "@" in password:
#     return True
#   elif "$" in password:
#     return True
#   elif "%" in password:
#     return True
#   elif "&" in password:
#     return True
#   else:
#     return False


def is_valid(password):
    if len(password) <= 7:
        return False
    if any(char in password for char in '!@$%&'):
        return True
    else: 
        return False
    
