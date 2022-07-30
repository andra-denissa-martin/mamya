def min(x, y):
    if x < y:
        return x
    else:
        return y
print(min(1, 2))              
       

def max(number1, number2):
    if number1 > number2:
        return number1
    else:
        return number2
print(max(2, 4))            


def len(list):
    list_of_elements = 0
    for i in list:
        list_of_elements = list_of_elements + 1
    return list_of_elements
print(len([1, 4, 9, 3, 7]))        
    


def multiply(x, y):
    return x**y  
print(multiply(2, 2))        



def pow(x, y):
    num1 = x
    num2 = y
    return num1 * num2 
print(pow(2, 2))    


def divmod(x, y):
    num1 = x
    num2 = y
    number_list = num1 / num2
    zero_list = number_list * 0
    return (number_list, zero_list)
print(divmod(4, 2))    
