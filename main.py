# Encryption Algorithm
# step 3 converting ASCII to binary
def decimal(num):
    if num >= 1:
        decimal(num//2)
    print(num % 2, end='')

    
if __name__ == '__main__':
    num1 = 45
    decimal(num1)
