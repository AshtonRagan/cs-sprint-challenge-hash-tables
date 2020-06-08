def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    d = {}
    r = []
    for i in a:
        if i not in d:
            d[i] = 1
            d[-i] = 1
        else:
            if i < 0:
                r.append(-i)
            else:
                r.append(i)
    return r


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
