def naive_with_mismatches(p, t, max_mismatches):
    occurrences = []
    for i in range(len(t) - len(p) + 1):
        match = True
        mismatches = 0
        for j in range(len(p)):
            if t[i+j] != p[j]:
                mismatches += 1
                if mismatches > max_mismatches:
                    match = False
                    break
        if match:
            occurrences.append(i)
    return occurrences
