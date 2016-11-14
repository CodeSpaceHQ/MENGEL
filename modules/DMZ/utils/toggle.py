def get_axis_toggle(method):
    if method == "column":
        return 0
    elif method == "row":
        return 1
    else:
        print("Please input row or column.")
        return 2
