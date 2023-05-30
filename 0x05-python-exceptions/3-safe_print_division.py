#!usr/bin/python3

def safe_print_list_integers(numbers_list, x=0):
    count = 0

    for i in range(min(x, len(numbers_list))):
        try:
            print("{:d}".format(numbers_list[i]), end='')
            count += 1
        except (TypeError, ValueError):
            pass

    print()
    return count

