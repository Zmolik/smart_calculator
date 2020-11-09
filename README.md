# smart_calculator
Calculator that not only adds, subtracts, and multiplies, but is also smart enough to remember previous calculations.

Smart calculator was developed based on a project at hyperskill.org: 
https://hyperskill.org/projects/74?track=2

It uses conversion from infix to postfix notation in order to calculate complex expressions e.g. 3 + 8 * ((4 + 3) * 2 + 1) - 6 / (2 + 1)

Part of the program is assignment of values to variables e.g. a = 5, that can later be used in an expression.

Examples('>' represent user input):
> 8 * 3 + 12 * (4 - 2)
48
> 2 - 2 + 3
3
> 4 * (2 + 3
Invalid expression
> -10
-10
> a=4
> b=5
> c=6
> a*2+b*3+c*(2+3)
53
> 1 +++ 2 * 3 -- 4
11
> 3 *** 5
Invalid expression
> 4+3)
Invalid expression
> /command
Unknown command
> /exit
Bye!
