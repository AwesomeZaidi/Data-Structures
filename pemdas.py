from linkedlist import LinkedList

"""
    PEMDAS Problem by Ikey, Jake and Asim.

    "((34*2)-3)"

    Step 1: Convert string to list:
        ['(', '(', '34', '*', '2', ')', '-', '3', ')']
    
    Step 2: 

"""

math_problem = "((34*2)-3)"

    # def __repr__(self):
    #     return self.math_list

def convertStringToList(math_problem):
    new_list = LinkedList()
    symbols = set(['(' , ')', '+', '-', '*', '^'])

    for c in math_problem:
        if c in symbols:
            new_list.append(c)
        if c.isdigit():
            if new_list.length() > 0 and type(new_list.tail.data) == int:
                new_list.tail.data = int(str(new_list.tail.data) + c) 
            else:
                new_list.append(int(c))
        
    return new_list

def eval_string()


if __name__ == '__main__':
    math_problem = "((34*2)-3)"
    math_problem_1 = "10 + 10"

    print('math_problem:', math_problem)
    print(convertStringToList(math_problem))