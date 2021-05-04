def classify(number):
    if number < 1:
        raise ValueError("Number not valid.")
    aliquot_sum = sum(i for i in range(1, number // 2 + 1) if number % i == 0)
    if aliquot_sum == number:
        return "perfect"
    if aliquot_sum > number:
        return "abundant"
    return "deficient"
