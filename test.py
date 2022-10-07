def f(start_number, start_base, end_base):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    number = sum([digits.find(digit)*start_base**i for i, digit in enumerate(start_number[::-1])])
    end_number = '' if number > 0 else '0'
    while number > 0:
        end_number = digits[number % end_base] + end_number
        number //= end_base
    return end_number


print(f('0', 2, 16))
