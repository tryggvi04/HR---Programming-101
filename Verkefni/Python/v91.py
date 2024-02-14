def is_float(string_to_test: str):
    try:
        float(string_to_test)
        return True
    except:
        return False
