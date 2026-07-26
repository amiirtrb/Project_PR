def Devision(a,b):
    try:
        return int(a) // int(b)
    except ZeroDivisionError:
        return "please enter a valid value"
    except ValueError:
        return "please enter digits"

a = input()
b = input()
print(Devision(a,b))


