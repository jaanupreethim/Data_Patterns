def swap_integers(a, b):
    temp = a
    a = b
    b = temp
    return a, b

if __name__ == "__main__":
    x = int(input("Enter first integer (A): "))
    y = int(input("Enter second integer (B): "))
    x, y = swap_integers(x, y)
    print(f"Swapped values: A = {x}, B = {y}")
