def create_log(**kwargs):
    if 'file' not in kwargs.keys():
        raise ValueError("You must specify where save the log")
    elif 'action' not in kwargs.keys():
        raise ValueError("You must specify action of the log")
    elif 'obj' not in kwargs.keys():
        raise ValueError("You must specify what action")
