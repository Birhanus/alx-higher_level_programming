#!usr/bin/python3
def element_at(my_list, idx):
    for a in my_list:
        if idx < 0 or idx > len(my_list):
            pass
        else:
            return my_list[idx]
