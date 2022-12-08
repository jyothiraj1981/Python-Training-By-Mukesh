def decorator_list(func):
    def inner(*list_of_tuples):
        return[func(val[0],val[1]) for val in list_of_tuples]
    return inner

@decorator_list
def sub_together(a,b):
    return a-b
print(sub_together([5,4],[10,3],[15,10],[12,6]))