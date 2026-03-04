#this reexp is kinda hard but after figuring it out, it was pretty fun and convinient tbhn (this cost me a lot of time to learn btw)
import re
def coursecode(code):
    pattern = r"^[A-Z]{2,3}[0-9]{3}$"

    if re.match(pattern, code):
        return True
    else:
        return False
