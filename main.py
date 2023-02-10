def decimal(num):
    x = "{:08b}".format(int(num))
    return x
def split(x):
    Element_1 = int(x/10000)
    Element_2 = x - Element_1*10000
    return Element_1, Element_2
def twoscomplement(val):
    val = str(val)
    num1 = int(val, 2)
    val = ~num1 
    val = "{:04b}".format(int(val))
    return val
def Concatenate(num1, num2):
    temp = int(str(num1) + str(num2))
    return temp

if __name__ == '__main__':
    # step1 to convert into character into ascii code
    c = input("enter the character that u need to convert into it's ascii value: ")
    num1 = ord(c) + 100
    x = int(decimal(num1))
    Element = split(x)
    complementElement1 = twoscomplement(Element[0])
    complementElement2 = twoscomplement(Element[1])
    print(complementElement1)
    print(complementElement2)
    Concatenated_num = Concatenate(complementElement1, complementElement2)
    print(Concatenated_num)
    print(x)
