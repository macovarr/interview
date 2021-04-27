def flatten(l):
    result = []
    if not l:
        return []
    for entry in l:
        if isinstance(entry, list):
            result.extend(flatten(entry))
        else:
            result.append(entry)
    return result


assert flatten([1, 2, [3, 4], 5, [[6]]]) == [1, 2, 3, 4, 5, 6]
assert flatten([1, 2, [3, [4, 5], 6], 7, [[8, 9]]]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
