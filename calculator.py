from string import ascii_letters, digits
from collections import deque

stack = deque()
main_postfix = deque()
dic = {}


def is_of_letters_only(string):
    """returns True if the input string consists only of ascii_letters"""
    for char in string:
        if char not in ascii_letters:
            return False
    return True


def is_of_digits_only(string):
    """returns True if the input string consists only of digits"""
    for char in string:
        if char not in digits:
            return False
    return True


def is_of_digits_and_one_plusminus(string):
    """returns True if string consists od digits and one operator plus or minus"""
    for char in string:
        if char in digits or char in ('+', '-'):
            continue
        else:
            return False
    if string.count('+') == 1 and string.startswith('+'):
        return True
    elif string.count('-') == 1 and string.startswith('-'):
        return True
    else:
        return False


def is_digits_or_letters_only(string):
    """returns True if the strin input consists only of digits or only of ascii_letters"""
    if is_of_letters_only(string) and not is_of_digits_only(string):
        return True
    elif not is_of_letters_only(string) and is_of_digits_only(string):
        return True
    return False


def find_var_in_dict(dic, key):
    """returns value from dictionary if key exits, if not returns False"""
    try:
        return dic[key]
    except KeyError:
        return False


def peek_at_top(stack):
    """returns top value of stack, but doesn't change the stack"""
    try:
        top = stack.pop()
    except IndexError:
        return False
    stack.append(top)
    return top


def stack_operator_is_lower(new_operator, stack_operator):
    """returns True if stack operator has lower precendence"""
    if stack_operator in {'+', '-'} and new_operator in {'/', '*'}:
        return True
    else:
        return False


def change_between_stack_postfix(stack, postfix, exp):
    """subpart of conversion from infix to postfix notation when stack operator has higher or even precendence"""
    postfix.append(stack.pop())
    while True:
        if not stack or peek_at_top(stack) == '(':
            stack.append(exp)
            break
        top = stack.pop()
        if stack_operator_is_lower(exp, top):
            stack.append(top)
            stack.append(exp)
            break
        else:
            postfix.append(top)


def from_string_to_list(string):
    """Converts the expression given by user from string into list.
       Takes into consideration number or variable of multiple elements e.g number(896), variable('distance')"""
    number = ''
    variable = ''
    lis = []
    for char in string:
        if char in ('*', '/', '+', '-', '(', ')', ' '):
            if number:
                lis.append(number)
                number = ''
            elif variable:
                lis.append(variable)
                variable = ''
            if char == ' ':
                continue
            else:
                lis.append(char)
        elif char in digits:
            number += char
        elif char in ascii_letters:
            variable += char
        else:
            if char == ' ':
                continue
            elif char == '*' or char == '/':
                lis.append()
            elif char == '(' or char == ')':
                pass
    if number:
        lis.append(number)
    elif variable:
        lis.append(variable)
    return lis


def check_for_invalid(string):
    """Checks for the most common typos in user input"""
    if string.count('(') != string.count(')'):
        return False
    if string.count('**') or string.count('//') or string.count('/*') or string.count('*/'):
        return False
    if string.count('+*') or string.count('*+') or string.count('+/') or string.count('/+'):
        return False
    if string.count('-*') or string.count('*-') or string.count('-/') or string.count('/-'):
        return False
    return True


def reduce_plus_minus(string):
    """The user can input multiple neighbouring pluses/minuses. This function converts these signs to one."""
    while string.count('++'):
        string = string.replace('++', '+')
    while string.count('--'):
        string = string.replace('--', '+')
    while string.count('+-'):
        string = string.replace('+-', '-')
    while string.count('-+'):
        string = string.replace('-+', '-')
    return string


def infix_to_postfix(lis):
    """Input: list()
       Output: deque()

       Converts infix to postfix notation."""
    stack = deque()
    postfix = deque()
    for exp in lis:
        if is_of_digits_only(exp) or is_of_letters_only(exp):
            postfix.append(exp)
        elif not stack or peek_at_top(stack) == '(':
            stack.append(exp)
        elif exp == '(':
            stack.append(exp)
        elif exp == ')':
            while peek_at_top(stack) != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            top = peek_at_top(stack)
            if exp == '*':
                if stack_operator_is_lower(exp, top):
                    stack.append(exp)
                else:
                    change_between_stack_postfix(stack, postfix, exp)
            elif exp == '/':
                if stack_operator_is_lower(exp, top):
                    stack.append(exp)
                else:
                    change_between_stack_postfix(stack, postfix, exp)
            elif exp == '+' or exp == '-':
                change_between_stack_postfix(stack, postfix, exp)
    while stack:
        postfix.append(stack.pop())
    return postfix


def postfix_to_result(postfix, dic):
    """Input: deque(), dic()
       Output: int

       Calculates result out of the expression in postfix notation."""
    stack = deque()
    while postfix:
        bottom = postfix.popleft()
        if bottom[0] in digits:
            stack.append(bottom)
        elif bottom[0] in ascii_letters:
            value = find_var_in_dict(dic, bottom)
            stack.append(value)
        else:
            n2 = stack.pop()
            n1 = stack.pop()
            if bottom[0] == '+':
                result = int(n1) + int(n2)
            elif bottom[0] == '-':
                result = int(n1) - int(n2)
            elif bottom[0] == '*':
                result = int(n1) * int(n2)
            else:
                result = int(n1) / int(n2)
            stack.append(result)
    return result

# MAIN LOOP, quit the program by entering '/exit'
while True:
    user_input = input().strip()
    if not user_input:
        pass
    # controls command input
    elif user_input.startswith('/'):
        if user_input == '/exit':
            print('Bye!')
            break
        elif user_input == '/help':
            print('Smart calculator build as part of hyperskill project: https://hyperskill.org/projects/74')
            print('1)You can use following operators: "+", "-", "*", "/", "(", ")"\n2)You can assign values e.g. a = 5')
            print('3)You can calculate with these values e.g. a + 5\nWrite /exit to quit the program')
        else:
            print('Unknown command')
    # controls assignment input
    elif '=' in user_input:
        if user_input.count('=') == 1:
            action = user_input.split('=')
            identifier = action[0].strip()
            assignment = action[1].strip()
            if is_of_letters_only(identifier):
                if is_digits_or_letters_only(assignment):
                    if is_of_letters_only(assignment):
                        value = find_var_in_dict(dic, assignment)
                        if value:
                            dic[identifier] = value
                        else:
                            print('Unknown variable')
                    else:
                        dic[identifier] = assignment
                else:
                    print('Invalid assignment')
            else:
                print('Invalid identifier')
        else:
            print('Invalid assignment')
    # next 4 elif statements control the correctness of one variable/number input
    # if user inputs one variable or number the program will print it
    elif is_of_digits_only(user_input):
        print(user_input)
    elif is_of_digits_and_one_plusminus(user_input):
        print(user_input)
    elif is_of_letters_only(user_input):
        value = find_var_in_dict(dic, user_input)
        if value:
            print(value)
        else:
            print('Unknown variable')
    elif user_input.endswith('-') or user_input.endswith('+') or user_input.endswith('*') or user_input.endswith('/'):
        print('Invalid expression')
    else:
        # the expressions that got here are not: commands, assignments, single variable or number
        # 1. check for invalid input
        # 2. reduce number of neighbouring pluses/minuses to one
        # 3. convert the modified string to list
        # 4. convert from infix(list) to postfix(deque)
        # 5. calculate and print the result
        if not check_for_invalid(user_input):
            print('Invalid expression')
            continue
        modified_input_as_list = from_string_to_list(reduce_plus_minus(user_input))
        main_postfix = infix_to_postfix(modified_input_as_list)
        main_result = postfix_to_result(main_postfix, dic)
        print(main_result)