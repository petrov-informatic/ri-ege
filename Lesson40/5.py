def print_digit_sum1(n):
    print(sum(map(int, str(n))))


def print_digit_sum2(n):
    print(sum([int(i) for i in str(n)]))


def print_digit_sum3(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    print(s)



print_digit_sum1(12345)
print_digit_sum2(12345)
print_digit_sum3(12345)