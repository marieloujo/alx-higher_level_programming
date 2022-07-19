#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    results = []
    for i in range(list_length):
        try:
            cal = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            cal = 0
            print("division by 0")
        except (ValueError, TypeError):
            cal = 0
            print("wrong type")
        except IndexError:
            cal = 0
            print("out of range")
            pass
        finally:
            results.append(cal)

    return (results)
