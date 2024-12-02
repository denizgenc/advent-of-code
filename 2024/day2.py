import itertools

import adventinput

def day2_part1(reports):
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

def day2_part2(reports):
    """
    crap
    """
    numeric = [[int(x) for x in line.split()] for line in reports]

    safe, safe_dampened = 0, 0
    for report in numeric:
        increasing = [a < b for a, b in itertools.pairwise(report)]
        decreasing = [a > b for a, b in itertools.pairwise(report)]
        if all(increasing) or all(decreasing):
            diffs = [abs(a-b) < 4 for a, b in itertools.pairwise(report)]
            safe += all(diffs)
            # If we have a difference that is too large, but we can filter out at most one number
            # that causes this difference (and we know that all of these numbers are increasing or
            # decreasing monotonically), this number must occur at either the start
            # or the beginning of the report
            # Otherwise, that means that for a report [ ... a, b, c, ... ],
            # where abs(a-b) >= 4, abs(a-c) must be > 4, so removing "b" won't change anything
            if diffs.count(False) == 1 and (diffs.index(False) == 0 or diffs.index(False) == len(diffs) - 1):
                #print(f"we're at the first branch with report {report} and diffs {diffs}")
                filtered = report[1:] if diffs.index(False) == 0 else report[:-1]
                safe_dampened += all((abs(a-b) < 4 for a, b in itertools.pairwise(filtered)))
        elif increasing.count(False) == 1 or decreasing.count(False) == 1:
            # pick "strongest direction"
            candidate = increasing if increasing.count(False) == 1 else decreasing
            outlier = candidate.index(False)
            filtered_reports = []
            # I don't know why we need to do this, we just do
            filtered_reports.append(report[:outlier] + report[outlier + 1:])
            filtered_reports.append(report[:outlier+1] + report[outlier + 2:])

            tests = set()
            for r in filtered_reports:
                monotonic = all((a < b for a, b in itertools.pairwise(r))) or all((a > b for a, b in itertools.pairwise(r)))
                gradual = all((abs(a-b) < 4 for a, b in itertools.pairwise(r)))
                tests.add((monotonic, gradual))

            if (True, True) in tests:
                safe_dampened += 1

    safe_dampened += safe
    return safe, safe_dampened

def day2_part2_dumb(reports):
    """
    stupid but at least it makes sense
    """
    safe, safe_dampened = 0, 0
    for report in reports:
        if day2_part1([report]) > 0:
            safe += 1
        else:
            dumb_results = []
            levels = report.split()
            for index, _ in enumerate(levels):
                new_report = " ".join(levels[:index] + levels[index+1:])
                dumb_results.append(day2_part1([new_report]))
            if any(dumb_results):
                safe_dampened += 1

    safe_dampened += safe

    return safe, safe_dampened

if __name__ == "__main__":
    reports = adventinput.get_data(2)
    #res = day2_part2_dumb(reports)
    res = day2_part2(reports)
    print(res)
