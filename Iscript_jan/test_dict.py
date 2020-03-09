# x = {7: 49}
squares = {'b' : 4, 'a' : 4, 'c' :64 , 'd' : 9, 'e' : 16, 'f': 25}
#squares[6] = 36
#for key in x:
#    if key not in squares:
#        squares[key] = x[key]

#for key in squares:
#    print("squares is {} {}".format(key, squares[key]))
list_squares = []
for key in squares:
    list_squares.append((key,squares[key]))

print ("list of squares is {}".format(list_squares))

list_squares.sort()
list_squares.sort(key=lambda x: x[1])
print ("list of squares sorted is {}".format(list_squares))
