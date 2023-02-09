def decimal(num):
    x = "{:08b}".format(int(num))
    return x
def split(x):
    # step 4
    Element_1 = int(x/10000)
    Element_2 = x - Element_1*10000
    return Element_1, Element_2
def twoscomplement(num1, num2):
    
    return num1

if __name__ == '__main__':
    # step1 to convert into character into ascii code
    c = input("enter the character that u need to convert into it's ascii value: ")
    num1 = ord(c) + 100
    x = int(decimal(num1))
    Element = split(x)
    complementElement = twoscomplement(Element[0], Element[1])
    print(Element[0])
    print(Element[1])
    print(complementElement)
    print(x)
