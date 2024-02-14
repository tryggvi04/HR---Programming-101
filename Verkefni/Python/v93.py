def divide_safe(num1_str,num2_str):
    try:
        res = float(num1_str)/float(num2_str)
        return round(res, 5)
    except:
        return None
    

print(divide_safe(input(), input()))