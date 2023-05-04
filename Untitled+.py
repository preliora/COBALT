import os

print('Welcome to COBALT!')

output = ""

def ifItem(first, second):
    if first == second:
        print(True)
def version():
    print("This is COBALT V1.1")
def getValue(value, push, pushitem):
    global output
    
    if value.find('[') == -1:
        print(value.split(':')[1])
    else:
        print(value.split('[')[1])
        print(value.split(':')[0] + ' is a list')
    if push == True:
        output = output + pushitem
        print(output)

def math(one, method, two):
    if method == "*":
        print(one * two)
    elif method == "+":
        print(one + two)
    elif method == "-":
        print(one - two)
    elif method == "/":
        print(one / two)

def searchValues(string, searchPos):
    print(string.split('[')[1].split('}')[searchPos - 1].split(':')[1])

def cmd(command):
    os.system(command)

