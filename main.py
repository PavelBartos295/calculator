
def manual_sum(x, y):
    return x + y

def manual_sub(x, y):
    return x - y

def manual_div(x, y):
    if y == 0:
        return 0
    else:
        return x // y

def manual_mul(x, y):
    return x * y

data = input("Your mathematical problem: ")
split_data = data.split(" ")

x = int(split_data[0])
y = int(split_data[2])

if split_data[1] == "+":
    print(manual_sum(x, y))
elif split_data[1] == "-":
    print(manual_sub(x, y))
elif split_data[1] == "/":
    print(manual_div(x, y))
elif split_data[1] == "*":
    print(manual_mul(x, y))
else:
    print("Operation is not supported")
