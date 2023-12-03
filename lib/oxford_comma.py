def oxford_comma(items):
    if len(items) == 0:
        return ""
    elif len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return "{} and {}".format(items[0], items[1])
    else:
        comma_separated = ", ".join(items[:-1])
        return "{}, and {}".format(comma_separated, items[-1])
