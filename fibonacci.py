def fibonacci(position):
    if position <= 2:
        return (position - 1);
    return fibonacci(position - 1) + fibonacci(position - 2)


if __name__ == '__main__':
    position = int(input("Enter last position: "));
    for i in range(1, position + 1):
        print(fibonacci(i));
