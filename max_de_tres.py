def max_of_three(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    else:
        return "a dos numeros o tres que son iguales"

    return n3


print(max_of_three(40, 55, 5))
