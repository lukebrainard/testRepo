def mean(input):
    sum  = 0
    for a in input:
        sum += a
    return sum/len(input)

test = [1, 2, 3, 4,6, 8, 2, 4]
print(mean(test))