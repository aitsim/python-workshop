# filter in  python
#  The filter() method filters the given sequence with the help of a function
#  that tests each element in the sequence to be true or not.
# filter(function, sequence)
# Parameters:
# function: function that tests if each element of a 
# sequence true or not.
# sequence: sequence which needs to be filtered, it can 
# be sets, lists, tuples, or containers of any iterators.
# Returns:
# returns an iterator that is already filtered.
# -----------------------------

def fun(variable): 
    letters = ['a', 'e', 'i', 'o', 'u'] 
    if (variable in letters): 
        return True
    else: 
        return False

# sequence 
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r'] 
filtered = filter(lambda x : x in ['a','e','i','o','i'], sequence)
filtered = filter(fun,sequence)
  
# print('The filtered letters are:') 
# for s in filtered: 
#     print(s) 
print(filtered)



# ---------------

sequence =[1,2,3,4,5,6,7,8]

filtered = filter(lambda x: x % 2,sequence)

filtered = filter(lambda x: x <5,sequence)

def fun(var):
    if var % 2==0:
        return True 
    return False

filtered = filter(fun, sequence)


print(filtered)
