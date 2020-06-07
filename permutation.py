def permutation(word):
    # base condition
    if len(word) == 1:
        return [word]
    sublist = permutation(word[1:])

    char = word[0]
    result = []
    for element in sublist:
        for j in range(0, len(sublist)+1):
            result.append(element[:j] + char + element[j:])
    return result


print(permutation("abc"))
