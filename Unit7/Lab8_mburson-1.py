def Find_UPC(upc_string):
    odd_sum = 0
    even_sum = 0

    for i in range(11):
        digit = int(upc_string[i])
        if (i + 1) % 2 != 0:
            odd_sum += digit
        else:
            even_sum += digit

    total_sum = (odd_sum * 3) + even_sum
    check_digit = (10 - (total_sum % 10)) % 10

    return check_digit

def is_valid_upc(upc_code):

    calculated_check = Find_UPC(upc_code[:-1])
    actual_check = int(upc_code[-1])

    return calculated_check == actual_check

while True:
    user_upc = input("Enter the 12-digit UPC code: ")
    if user_upc.lower() == "q":
        break

    if is_valid_upc(user_upc):
        print("The UPC code is valid.")
    else:
        print("The UPC code is invalid.")