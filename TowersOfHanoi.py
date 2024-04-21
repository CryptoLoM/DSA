def hanoi(n, source, target, auxiliary, ):
    if n > 0:
        # Move n-1 disks from the primary core to the secondary
        hanoi(n - 1, source, auxiliary, target)

       # Display information about the movement
        print(f"Move disk {n} from {source} to {target}")

        # Update the number of disks on each rod
        towers[source] -= 1
        towers[target] += 1

        print_towers()
        move_disk()
        # Move n-1 disks from the auxiliary rod to the target one
        hanoi(n - 1, auxiliary, target, source)


def print_towers():
    for key, count in towers.items():
        print(f"On the rod {key}: {count} disks")
    print('--' * 11)


def move_disk():
    global move_count
    move_count += 1
    print(f"Total number of moves: {move_count}")
    print("---" * 8)


num_disks = int(input("Enter the number of disks:"))
towers = {'A': num_disks, 'B': 0, 'C': 0}

move_count = 0
hanoi(num_disks, 'A', 'C', 'B')
print("All disks have been moved!!!")
