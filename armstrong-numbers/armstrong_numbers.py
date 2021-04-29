def is_armstrong_number(number):
    number_list = [int(digit) for digit in str(number)]
    digit_sum = 0
    
    for digit in number_list:
        digit_sum += digit ** len(number_list)
        
    return digit_sum == number