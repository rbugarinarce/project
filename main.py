def vote_menu():
    print('--------------------')
    print("VOTE MENU")
    print('--------------------')
    print("Enter 'v' to Vote")
    print("Enter 'x' to Exit")

    while True:
        option = input("Option: ").strip()  # Add .strip() here
        if option.lower() == 'v':
            return 'v'
        elif option.lower() == 'x':
            return 'x'
        else:
            print("Invalid option. Please choose 'v' to vote or 'x' to exit.")

def candidate_menu():
    print('--------------------')
    print("CANDIDATE MENU")
    print('--------------------')
    print("Enter 1 to Vote for John")
    print("Enter 2 to Vote for Jane")

    while True:
        try:
            option = int(input("Option: "))
            if option == 1:
                return 1
            elif option == 2:
                return 2
            else:
                print("Invalid option. Please choose 1 for John or 2 for Jane.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    john_votes = 0
    jane_votes = 0

    while True:
        vote_option = vote_menu()

        if vote_option == 'x':
            break

        candidate_option = candidate_menu()

        if candidate_option == 1:
            john_votes += 1
        elif candidate_option == 2:
            jane_votes += 1
        else:
            print("Error in candidate selection.")

    total_votes = john_votes + jane_votes
    print("\nJohn-{}, Jane-{}, Total-{}".format(john_votes, jane_votes, total_votes))

if __name__ == "__main__":
    main()
