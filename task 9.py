### Dictionary Task 9 ###
from Tools.scripts.make_ctype import values

number= [1,2,3,4,5,6,7,8,9,10]
print("Original List:",number,'\n')
print("Extracted First Five Elements:")
print(number[:5])
b = []
for i in range(0,5):
    b.append(number[i])
    i=i+1
a_reversed = b[::-1]
print("Reverse extracted elements: ", a_reversed)

