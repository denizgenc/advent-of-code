import itertools

import adventinput

def day2(reports):
    numeric = [[int(x) for x in line.split()] for line in reports]

    safe = 0
    for report in numeric:
        monotonic = (
                all((a < b for a, b in itertools.pairwise(report)))
                or all((a > b for a, b in itertools.pairwise(report)))
        )
        if monotonic:
            gradual = all((abs(a-b) < 4 for a, b in itertools.pairwise(report)))
            safe += gradual

    return safe


if __name__ == "__main__":
    reports = adventinput.get_data(2)
    res = day2(reports)
    print(res)
