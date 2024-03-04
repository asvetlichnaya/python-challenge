# Assignment2, task1

# Write a program that as input accepts a string typed on keyboard and as output
# it will print this string reversed

def reverse_string(i_str: str):
    o_str = ''
    length = len(i_str)
    for i in range(length):
        o_str = o_str + i_str[length-i-1]
    return o_str


input_string = input('Input: ').strip()

print('Output : ' + reverse_string(input_string))