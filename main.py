
def isPalidrome (string):
    if len(string) == 1:
        print('1st if ', string)
        return True

    if string[0] == string[len(string) - 1]:
        print('second if', string[1:-1])
        return isPalidrome(string[1 : -1])
    else:
        print('false', string)
        return False


string = input("Please enter a string: ")

isPalidrome(string)


def is_Number(x):
    if x % 2 == 0:
        print('Even num')
        return True
    else:
        print('Odd num')
        return False

x = int(input("Please enter num: "))
is_Number(x)
