#input: nhập tuple
#output: phần tử đầu tiên và cuối cùng

def truy_cap_pt(tuple_data):
    first_element = tuple_data[0]
    last_element = tuple_data[-1]
    return first_element,last_element

input_tuple = eval(input("nhập tuple, vì du (1, 2, 3): "))
first, last = truy_cap_pt(input_tuple)

print("phần tử đầu tiên:",first)
print("phần tử cuối cùng:",last)