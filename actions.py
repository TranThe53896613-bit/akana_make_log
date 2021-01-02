ADD = 1
CREATE = 2
DELETE = 3
MODIFY = 4
BUY = 5

def get_action_name(code):
    if code == 1:
        return "ADD"
    elif code == 2:
        return "CREATE"
    elif code == 3:
        return "DELETE"
    elif code == 4:
        return "MODIFY"
    elif code == 5:
        return "BUY"
    else:
        raise ValueError(f"code action {code} is invalid")