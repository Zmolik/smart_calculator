# smart_calculator
Calculator that not only adds, subtracts, and multiplies, but is also smart enough to remember previous calculations.  
It uses conversion from infix to postfix notation in order to calculate complex expressions   
e.g. 3 + 8 * ((4 + 3) * 2 + 1) - 6 / (2 + 1)

Part of the program is assignment of values to variables e.g. a = 5, that are saved into a dictionary. 
Saved variables can be used in an expression e.g. input: a + 5, output: 10

Quit the program by writing '/exit'.


**Examples:**  
  
Input: *8 * 3 + 12 * (4 - 2)*  
Result: *48*  
    
Input: *1 +++ 2 * 3 -- 4*  
Result: *11*  
  
Input: *a=4*  
Input: *b = 5*  
Input: *c=6*  
Input: *a/*2+b/*3+c/*(2+3)*  
Result: *53*  


Smart calculator was developed based on a project at hyperskill.org:  https://hyperskill.org/projects/74?track=2  
