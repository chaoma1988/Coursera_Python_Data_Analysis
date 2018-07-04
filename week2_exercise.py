"""
Solution - Create a list nested_list consisting of five empty lists
"""

# Add code here
nested_list = [[], [], [], [], []]

# Tests
print(nested_list)

# Output
#???


"""
Template - Create a list nested_list of length 5 whose items 
are themselves lists consisting of 3 zeros
"""

# Add code here
nested_list = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

# Tests
print(nested_list)

# Output
#???


"""
Template- Create a list zero_list consisting of 3 zeroes using a list comprehension
https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions

As a challenge, redo the previous problem using a nested list comprehension
https://docs.python.org/3/tutorial/datastructures.html#nested-list-comprehensions
"""

# Add code here for a list comprehension
zero_list = [0 for x in range(3)]

# Add code here for nested list comprehension
nested_list = [zero_list for x in range(3)]


# Tests
print(zero_list)
print(nested_list)

# Output
#[0, 0, 0]
#[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]



"""
Template - Select a specific item in a nested list
"""

print()
print('*'*40)
print('prob 4')
# Define a nested list of lists
nested_list = [[col + 3 * row for col in range(3)] for row in range(5)]
print(nested_list)

# Add code to print out the item in this nested list with value 7

print(nested_list[2][1])
# Output
#[[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 13, 14]]
#7

"""
Template - Create a list list_dicts of 5 empty dictionaries
"""

# Add code here
list_dicts=[{},{},{},{},{}]

# Tests
print(list_dicts)


# Output
#???


"""
Solution - Write a function dict_copies(my_dict, num_copies) that 
returns a list consisting of num_copies copies of my_dict
"""


# Add code here
def dict_copies(my_dict, num_copies):
    """
    Given a dictionary my_dict and an integer num_copies, 
    returns a list consisting of num_copies copies of my_dict.
    """
    answer = []
    for idx in range(num_copies):
        answer.append(dict(my_dict))
    return answer


# Tests
print(dict_copies({}, 0))
print(dict_copies({}, 1))
print(dict_copies({}, 2))

test_dict = dict_copies({'a' : 1, 'b' : 2}, 2)
print(test_dict)

# Check for reference problem
test_dict[1]["a"] = 3
print(test_dict)



# Output
#[]
#[{}]
#[{}, {}]
#[{'a': 1, 'b': 2}, {'b': 2, 'a': 1}]
#[{'b': 2, 'a': 1}, {'b': 2, 'a': 3}]

# Note that you have a reference issue if the last line of output is
#[{'a': 3, 'b': 2}, {'b': 2, 'a': 3}]


"""
Solution - Write a function make_dict_lists(length) that returns a dictionary whose keys are in range(length) and whose
corresponding values are lists of zeros with length matching the key
"""


# Add code here
def make_dict_lists(length):
    """
    Given an integer length, return a dictionary whose keys
    lie in range(length) and whose corresponding values are 
    lists of zeros with length matching the key
    """
    return_dict = {}
    for keys in range(length):
        return_dict[keys] = [0 for x in range(keys)]
    return return_dict



# Tests
print(make_dict_lists(0))
print(make_dict_lists(1))
print(make_dict_lists(5))


# Output
#{}
#{0: []}
#{3: [0, 0, 0], 0: [], 4: [0, 0, 0, 0], 1: [0], 2: [0, 0]}


"""
Template - Create a dictionary grade_table whose keys are provided
student names and values are associated list of grades
"""


# Add code here

grade_table = {'Joe':[100,98,100],
               'Scott':[75,59,89],
               'John':[86,84,91],
              }
# Tests
print(grade_table["Joe"])
print(grade_table["Scott"])
print(grade_table["John"])


# Output
#[100, 98, 100, 13]
#[75, 59, 89, 77]
#[86, 84, 91, 78]


"""
Template - Create a function make_grade_table(name_list, grades_list) 
whose keys are the names in names and whose values are the
lists of grades in grades
"""


# Add code here

def make_grade_table(name_list, grades_list):
    """
    Given a list of name_list (as strings) and a list of grades
    for each name, return a dictionary whose keys are
    the names and whose associated values are the lists of grades
    """
    return_dict={}
    idx = 0
    for keys in name_list: # the solution provided by the instructor using zip() function to zip the name_list and grades_list
        return_dict[keys] = grades_list[idx]
        idx = idx + 1
        
    return return_dict
        

# Tests
print(make_grade_table([], []))

name_list = ["Joe", "Scott", "John"]
grades_list = [100, 98, 100, 13], [75, 59, 89, 77],[86, 84, 91, 78] 
print(make_grade_table(name_list, grades_list))


# Output
#{}
#{'Scott': [75, 59, 89, 77], 'John': [86, 84, 91, 78], 'Joe': [100, 98, 100, 13]}


