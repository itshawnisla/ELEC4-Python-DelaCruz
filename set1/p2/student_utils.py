


def calculate_average(grades):
    return sum(grades) / len(grades)


def get_status(grades):
    if calculate_average(grades) >= 75:
        return "PASSED"
    else:
        return "FAILED"


def get_highest(grades):
    return max(grades)


def get_lowest(grades):
    return min(grades)
