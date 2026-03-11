def check(n):
    if n is not None:
        if n > 0:
            if n < 100:
                return True
    return False

print(check(50))
