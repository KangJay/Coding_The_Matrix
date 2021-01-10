
"""
0.5.1: Simple Expressions 
Tasks 0.5.1 to 0.5.3
Arithmetic and Numbers
"""
def SimpleExpressions():
    #Task 0.5.1: Use Python to find the number of minutes in a week 
    minsInHour, hoursInDay, daysInWeek = 60, 24, 7 
    minsInWeek = daysInWeek * hoursInDay * minsInHour 
    print("There are %d minutes in a week." % minsInWeek)
    #Task 0.5.2: Use Python to find the remainder of 2304811 divided by 47 without using modulo
    num, divider = 2304811, 47 
    whole_answer = num // divider 
    print("The remainder is %d." % (num - (whole_answer * divider)))
    #Task 0.5.3: Enter a Boolean Expression to test whether the sum of 673 and 909 is divisible by 3 
    if (673 + 909) % 3 == 0:
        print("The sum of the numbers are divisible by 3.")
    else: 
        print("The sum of the numbers are not divisible by 3.")

"""
0.5.2: Assignment Statements
Task 0.5.4
"""
def AssignmentStatements():
    """
    Task 0.5.4: Assign the value -9 to x and 1/2 to y. Predict the value of the following
    expression, then enter it to check your prediction:
        2**(y+1/2) if x+10<0 else 2**(y-1/2)
    """
    x, y = -9, 1/2
    # Prediction: Will equal 1.0 since x + 10 is not < 0 
    print(2**(y+1/2) if x+10<0 else 2**(y-1/2))

"""
Sets
Tasks 0.5.5 to 0.5.9
"""
def Sets(): 
    # Task 0.5.5: Write a comprehension over {1, 2, 3, 4, 5} whose value is the set consisting of the squares of the first five positive integers.
    test_set = {1, 2, 3, 4, 5}
    resulting_set = {x ** 2 for x in test_set if x > 0}
    print("Resulting set:", resulting_set)
    #Task 0.5.6: Write a comprehension over {0, 1, 2, 3, 4} whose value is the set consisting of the first five powers of two. 
    test_set = {x - 1 for x in test_set} #Makes the previous set decrement by 1 for each value  
    resulting_set = {2 ** x for x in test_set}
    print("Resulting set:", resulting_set)
    #Task 0.5.7 The value of the previous comprehension, {x * y for x in {1, 2, 3} for y in {2, 3, 4}}
    #is a seven-element set. Replace {1, 2, 3} and {2, 3, 4} with two other three-element sets so that the value becomes a nine-element set. 
    set1, set2 = {1, 2, 3}, {4, 5, 7}
    resulting_set = {x * y for x in set1 for y in set2}
    print("Resulting set:", resulting_set)
    #Task 0.5.8: Replace {1, 2, 3} and {2, 3, 4} in the previous comprehension with two dis-joint (Non-overlapping) three element sets so the value
    #becomes a five-element set 
    set1, set2 = {0, 1, 2}, {4, 8, 16}
    resulting_set = {x * y for x in set1 for y in set2}
    print("Resulting set:", resulting_set)
    #Task 0.5.9: Assume S and T are assigned sets. Without using the intersection operator &, write a comprehension over S whose value is the 
    #intersection of S and T. Hint: Use a membership tet in a filter at the end of the comprehension. 
    #Try out your comprehension with S = {1, 2, 3, 4} and T = {3, 4, 5, 6}
    S, T = {1, 2, 3, 4}, {3, 4, 5, 6}
    resulting_set = {x for x in S if x in T}
    print("Overlapping elements:", resulting_set)


"""
Lists
Task 0.5.10 to 0.5.12
"""
def Lists():
    #Task 0.5.10: Write an expression whose value is the average of the elements of the list [20, 10, 15, 75]
    elements = [20, 10, 15, 75]
    average = sum(elements) / len(elements) 
    print("Average is: {}".format(average))
    #Task 0.5.11: Write a double list comprehension over the lists ['A','B','C'] and [1,2,3] whose value is the 
    #list of all possible two-element lists [letter, number]. That is, the value is
    #[['A', 1], ['A', 2], ['A', 3], ['B', 1], ['B', 2],['B', 3], ['C', 1], ['C', 2], ['C', 3]]
    alphas, nums = ['A','B','C'], [1,2,3]
    result = [[x, y] for x in alphas for y in nums]
    print("Resulting list:", result)
    #Task 0.5.12: Suppose LofL has been assigned a list whose elements are themselves lists 
    # of numbers. Write an expression that evaluates to the sum of all the numbers in all the lists.
    LofL = [[.25, .75, .1], [-1, 0], [4, 4, 4, 4]]
    sumOfLists = sum([sum(x) for x in LofL])
    print("Sum of lists:", sumOfLists)

"""
Tuples
Tasks 0.5.13 to 0.5.16
"""
def Tuples():
    #Task 0.5.14: Suppose S is a set of integers, e.g. {-4, -2, 1, 2, 5, 0}. Write a triple comprehension whose value
    #is a list of all three-element tuples (i, j, k) such that i, j, k are elements of S whose sum is zero
    #Task 0.5.15: Modify the previous task so the resulting list does not include 0, 0, 0. Done also
    S = {-4, -2, 1, 2, 5, 0}
    result = [(i, j, k) for i in S for j in S for k in S if i != j and i != k and j != k and (i, j, k) != (0, 0, 0) and i + j + k == 0]
    print("Resulting tuples:", result)
    #Task 0.5.16 Further modify the expression so that its value is not the list of all such tuples but is the 
    #first such tuple. 
    result = [(i, j, k) for i in S for j in S for k in S if i != j and i != k and j != k and (i, j, k) != (0, 0, 0) and (i + j + k) == 0][0] #first element 
    print("Result:", result)
"""
Iterating over other things! 
Tasks 0.5.17 to 0.5.20
"""
def Iterating(): 
    #Task 0.5.17: Find an example of a list L such that len(L) and len(list(set(L))) are different 
    L = [1, 1, 1, 2, 3] 
    set_len = len(list(set(L))) 
    list_len = len(L)
    print("Length of set: ", set_len, ", length of list: ", list_len, ".", sep="")
    #Task 0.5.18: Write a comprehension over a range of the form range(n) such that the 
    #value of the comprehension is the set of odd numbers from 1 to 99. 
    odd_nums = {x for x in range(100)[1::2]} #start at index 1, get every 2nd number. 1 - 3 - 5 - 7 and on. 
    print("Odd numbers:", odd_nums)
    #Task 0.5.19: Task 0.5.19: Assign to L the list consisting of the first five letters ['A','B','C','D','E'].
    #Next, use L in an expression whose value is [(0, ’A’), (1, ’B’), (2, ’C’), (3, ’D’), (4, ’E’)]
    #Your expression should use a range and a zip, but should not use a comprehension.
    L = ['A','B','C','D','E']
    result = list(zip(range(5), L))
    print("Resulting list:", result)
    #Task 0.5.20: Starting from the lists [10, 25, 40] and [1, 15, 20], write a comprehension whose value 
    # is the three-element list in which the first element is the sum of 10 and 1, the second is the 
    # sum of 25 and 15, and the third is the sum of 40 and 20. Your expression should use zip but not list.
    l1, l2 = [10, 25, 40], [1, 15, 20]
    result = [sum(x) for x in (zip(l1, l2))]
    print("Resulting list:", result)

def Dictionaries(): 
    #Task 0.5.21: Suppose dlist is a list of dictionaries and k is a key that appears in all the 
    # dictionaries in dlist. Write a comprehension that evaluates to the list whose ith element
    # is the value corresponding to key k in the ith dictionary in dlist.
    # Test your comprehension with some data. Here are some example data.
    # dlist = [{'James':'Sean', 'director':'Terence'}, {'James':'Roger', 'director':'Lewis'}, {'James':'Pierce', 'director':'Roger'}] 
    # k = 'James'
    dlist = [{'James':'Sean', 'director':'Terence'}, {'James':'Roger', 'director':'Lewis'}, {'James':'Pierce', 'director':'Roger'}]
    k = 'James'
    result = [x[k] for x in dlist if k in x.keys()]
    print("Resulting List:", result)
    # Task 0.5.22: Modify the comprehension in Task 0.5.21 to handle the case in which k 
    # might not appear in all the dictionaries. The comprehension evaluates to the list whose ith 
    # element is the value corresponding to key k in the ith dictionary in dlist if that dictionary 
    # contains that key, and 'NOT PRESENT' otherwise.
    # Test your comprehension with k = 'Bilbo' and k = 'Frodo' and with the following
    # list of dictionaries:  dlist = [{'Bilbo':'Ian','Frodo':'Elijah'}, {'Bilbo':'Martin','Thorin':'Richard'}]
    dlist = [{'Bilbo':'Ian','Frodo':'Elijah'}, {'Bilbo':'Martin','Thorin':'Richard'}]
    k = 'Bilbo' and k = 'Frodo'
    
def main(): 
    SimpleExpressions() #0.5.1 - 0.5.3
    AssignmentStatements() # 0.5.4 
    Sets()  # 0.5.5 - 0.5.9
    Lists() # 0.5.10 - 0.5.12 
    Tuples()    # 0.5.13 - 0.5.16
    Iterating() # 0.5.17 - 0.5.20
    Dictionaries() # 0.5.21 - 0.5.2

if __name__ == "__main__":
    main()