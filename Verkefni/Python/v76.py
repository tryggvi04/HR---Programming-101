def decimal_to_binary(decimal):
    res_str = ""
    current_int = decimal
    while current_int > 0:
        remainder = current_int % 2
        res_str = str(remainder) + res_str
        current_int = current_int // 2
    if decimal == 0:
        return "0"
    return(res_str)

