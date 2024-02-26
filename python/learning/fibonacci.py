def main():
    num = input("Enter Nth Fibonacci: ")
    print(fib(int(num)))

def fib(n):
    if n <= 1: return n

    return (fib(n-1) + fib(n-2))


if __name__ == "__main__":
    main()