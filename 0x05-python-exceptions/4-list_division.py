#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    for i in range(list_length):
        try:
            dividend = my_list_1[i] if i < len(my_list_1) else 0
            divisor = my_list_2[i] if i < len(my_list_2) else 1  # Avoid division by zero

            if not isinstance(dividend, (int, float)) or not isinstance(divisor, (int, float)):
                raise TypeError("wrong type")
            elif divisor == 0:
                raise ZeroDivisionError("division by 0")

            result_list.append(dividend / divisor)

        except TypeError as e:
            print(e)
            result_list.append(0)

        except ZeroDivisionError as e:
            print(e)
            result_list.append(0)

        except IndexError:
            print("out of range")
            result_list.append(0)

    return result_list

