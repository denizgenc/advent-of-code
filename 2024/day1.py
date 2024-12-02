import adventinput

def day1(locations):
    ids = [x for s in locations for x in map(int, s.split())]
    group_1, group_2 = ids[0::2], ids[1::2]
    differences = [abs(a - b) for a, b in zip(sorted(group_1), sorted(group_2))]
    total = sum(differences)

    #return total

    new_total = 0
    for n in set(group_1):
        new_total += n * group_1.count(n) * group_2.count(n)

    return total, new_total

if __name__ == "__main__":
    lines = adventinput.get_data(1)
    res = day1(lines)
    print(res)
