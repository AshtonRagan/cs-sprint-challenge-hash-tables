def get_indices_of_item_weights(weights, length, limit):
    # Your code here
    d = {}
    ind = 0
    for i in weights:
        ind += 1
        v = limit - i
        if i not in d:
            d[v] = i, ind - 1
        else:
            print("D: ", d)
            if d[i][1] > ind - 1:
                return [d[i][1], ind - 1]
            return [ind - 1, d[i][1]]
    return None


# w = [4, 6, 10, 15, 16]
w = [12, 6, 7, 14, 19, 3, 0, 25, 40]
l = 9
limit = 7

print("Answere: ", get_indices_of_item_weights(w, l, limit))
