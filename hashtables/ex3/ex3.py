def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    d = {}
    r = []
    for i in range(len(arrays)):

        for j in range(len(arrays[i])):
            if arrays[i][j] not in d:
                d[j] = 1
            else:
                d[j] += 1
                if d[j] >= len(arrays):
                    r.append(j)

    return r


# if __name__ == "__main__":
    # arrays = []

    # arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    # arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    # arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    # print(intersection(arrays))


l = [
    [1, 2, 3, 4, 5],
    [12, 7, 2, 9, 1],
    [99, 2, 7, 1, ]
]

print("A: ", intersection(l))
