def Devision(a,b):
    try:
        return int(a) // int(b)
    except ZeroDivisionError:
        return "please enter a valid value"
    except ValueError:
        return "please enter digits"

a = int(input())
b = int(input())
print(f"Result: {Devision(a,b)}")
