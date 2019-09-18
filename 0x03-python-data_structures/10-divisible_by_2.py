#!/ust/bin/python3
def divisible_by_2(my_list=[]):
    copylis = my_list[:]
    for x in range(len(my_list)):
        if (copylis[x] % 2 == 0):
            copylis[x] = True
        else:
            copylis[x] = False
    return(copylis)
