def totalofRange(list, start, stop):
    total = 0
    if (stop > len(list)):
        return total
    for i in range(start - 1, stop):
          total += list[i]
    return total
