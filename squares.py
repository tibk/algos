from math import sqrt, ceil, floor 


def get_squares(a, b):
    # squares between A and B
    s_r_a = ceil(sqrt(a))
    s_r_b = floor(sqrt(b))
    return s_r_b - s_r_a + 1


if __name__ == '__main__':
    print(get_squares(4, 17))
