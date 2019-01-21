# Function that multiplies all the items in a list, we don't know the size of the list initially
def mass_multiply(n):
    # We can know the size of the list when we use len()
    length_of_list = len(n)

    # Because we are going to use a rolling product, we need to start with an initial number.
    # We start with 1 because 1 x anything is that same number.
    running_product = 1

    # Loop through every item in that list and multiply it by the previous
    # value of running_product and set it to running_product
    for i in range(0,length_of_list):
        running_product = running_product * n[i]
    return running_product


some_list = [10,20,7,5,6]
results = mass_multiply(some_list)
print('Multiplying the items in list',some_list,'produces the result:',results)
results = mass_multiply([1,2,3,4,5])
print('Multiplying the items in list',[1,2,3,4,5],'produces the result:',results)
