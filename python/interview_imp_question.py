#reversing a string without slicing
given_str="hello"
rev_str=""
for x in given_str:
    rev_str=x+rev_str
print(rev_str)    
