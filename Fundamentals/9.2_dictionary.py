# Write a program in Python that uses a dictionary to store how many times each item has been seen.
# The program should ask the user to enter a list of items, one at a time.
# When the user has finished entering items, the program should display a count of how many times each item was entered


def item_counter():
    # Initialize an empty dictionary to store item counts
    item_counts = {}

    print("Enter items one at a time. Type 'done' to finish.")

    while True:
        # Prompt the user to enter an item
        item = input("Enter an item: ").strip().lower()

        # Check if the user wants to finish
        if item == 'done':
            break

        # Update the count for the entered item in the dictionary
        if item in item_counts:
            item_counts[item] += 1
        else:
            item_counts[item] = 1

    # Display the counts of each item
    print("\nItem counts:")
    for item, count in item_counts.items():
        print(f"{item}: {count}")


# Call the function to run the program
item_counter()
