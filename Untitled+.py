def ifItem(first, second):
    if first == second:
        print(True)
def version():
    print("This is COBALT V1.0")
def getValue(value, getSpecificValueInList, specificValue, pos):
    
    if value.find('[') == -1:
        print(value.split(':')[1])
    else:
        print(value.split('[')[1])
        print(value.split(':')[0] + ' is a list')
    
    if getSpecificValueInList == True:
        print(value.split('[')[1].split(specificValue)[pos])


getValue('testing:[thing:buddy]', False, False, False)
