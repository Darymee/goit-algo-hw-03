def hanoi(n, source, target, auxiliary, pegs):
    if n == 1:
        disk = pegs[source].pop()
        pegs[target].append(disk)
        print(f"Move disk from {source} to {target}: {disk}")
        print(f"Intermediate state: {pegs}")
    else:
        hanoi(n - 1, source, auxiliary, target, pegs)
        hanoi(1, source, target, auxiliary, pegs)
        hanoi(n - 1, auxiliary, target, source, pegs)


def main():
    n = int(input("Enter the number of disks: "))
    pegs = {
        'A': list(range(n, 0, -1)),
        'B': [],
        'C': []
    }
    print(f"Initial state: {pegs}")
    hanoi(n, 'A', 'C', 'B', pegs)
    print(f"Final state: {pegs}")


if __name__ == "__main__":
    main()
