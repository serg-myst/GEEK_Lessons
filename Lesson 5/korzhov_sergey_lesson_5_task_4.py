
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
gen = (src[num] for num in range(len(src)) if src[num] > src[num-1] and num != 0)
print(*gen)
