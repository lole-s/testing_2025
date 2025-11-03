def is_prime(num):
    if not isinstance(num, int):
        return False
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

