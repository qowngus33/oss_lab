def range2(end, start=0, step=1):
    if start > end:
        (start, end) = (end, start)
    return list(range(start, end, step))

print(range2(10, 2, start=1))