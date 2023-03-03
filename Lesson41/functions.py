def join_lists(list1, list2):
    return sorted(list1 + list2)


def palindrom(s):
    return s == s[::-1]


def is_prime(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return x != 1


print(join_lists([1,2,3,4,5,6,7,8,9], [9,8,7,6,5]))


