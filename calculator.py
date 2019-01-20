def calculate(input_str):
    """
    First call this function
    :param input_str: a calculable expression for example: (1 + 2 / 7 * 6 - 1)
    :return: final evaluation of parameter
    """
    if is_valid(input_str):
        if has_operator(input_str):
            operand, sub1, sub2 = find_operator(input_str)
            sub_res1 = calculate(sub1)
            sub_res2 = calculate(sub2)
            result = base_calculate(operand, sub_res1, sub_res2)
            return result
        else:
            return float(input_str)
    else:
        print("not valid input")
        return None


def is_valid(input_str):
    return True


def find_operator(input_str):
    operators = {}
    operators_indexes = []
    if input_str.find("+") != -1:
        operators["plus"] = input_str.find("+")
    if input_str.find("-") != -1:
        operators["minus"] = input_str.find("-")
    if input_str.find("*") != -1:
        operators["mul"] = input_str.find("*")
    if input_str.find("/") != -1:
        operators["div"] = input_str.find("/")

    for each in operators.values():
        operators_indexes.append(each)
    for key, value in operators.items():
        if key == "plus":
            return "+", input_str[:value], input_str[value+1:]
        if key == "minus":
            return "-", input_str[:value], input_str[value + 1:]
    for key, value in operators.items():
        if key == "mul":
            return "*", input_str[:value], input_str[value+1:]
        if key == "div":
            return "/", input_str[:value], input_str[value+1:]


def base_calculate(operand, sub_res1, sub_res2):
    if operand == '*':
        return sub_res1 * sub_res2
    if operand == "-":
        return sub_res1 - sub_res2
    if operand == "/":
        return sub_res1 / sub_res2
    if operand == "+":
        return sub_res1 + sub_res2


def has_operator(input_str):
    import re
    input_str_list = input_str[::-1]
    if re.search('[+\-*/]', str(input_str_list)):
        return True
    return False
