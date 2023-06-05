numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]
def check_list(number_list):
    print(number_list)
    
    first_number= number_list[0]
    last_number= number_list[-1]
    if first_number==last_number:
        return True
    else:
        return False
print(check_list(numbers_x))
print(check_list(numbers_y))
