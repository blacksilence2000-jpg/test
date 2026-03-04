import re
def hexcode(code):
    pattern = r"^#[0-9A-Fa-f]{6}$"

    if re.match(pattern, code):
        return True
    else:
        return False