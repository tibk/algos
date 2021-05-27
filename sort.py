def sort(t, start, stop):                
    if stop <= start:
        return
    pivot_loc = start
    pivot_val = t[start]
    for i in range(start + 1, stop + 1):
        if t[i] < pivot_val:
            t[pivot_loc] = t[i]
            t[i] = t[pivot_loc + 1]
            t[pivot_loc + 1] = pivot_val
            pivot_loc += 1
    print(t, pivot_val)
    sort(t, start, pivot_loc - 1)
    sort(t, pivot_loc + 1, stop)


if __name__ == '__main__':
    t = [0, 1, 10, 5, 30, -5]
    print(f't: {t}')
    sort(t, 0, len(t)-1)
    print(f't: {t}')
