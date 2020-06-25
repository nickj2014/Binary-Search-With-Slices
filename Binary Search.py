def main():
    # get input from user, basic error check for number input only
    while True:
        try:
            num_input = int(input("Enter a number: "))
            break
        except:
            print("I said a number!")

    # call check function, input user number, print true or false result
    in_list = check(num_input)
    if in_list:
        print(num_input," is in the list!")
    else:
        print(num_input, "is not in the list.")


def check(num_input):

    numbers = [1, 2, 3, 5, 6, 9, 10, 15, 19, 25, 32, 48, 53, 102, 245, 311]

    while True:
        # get middle index number
        mid_list = round(int(len(numbers) / 2))

        # if middle number matches number, return true
        if num_input == numbers[mid_list]:
            return True

        # if down to one number and still no match, return false
        elif len(numbers) == 1:
            return False

        # if the number is smaller than middle number, cut off larger half of list
        elif num_input < numbers[mid_list]:
            numbers = numbers[:mid_list]

        # otherwise cut off smaller half of list
        elif num_input > numbers[mid_list]:
            numbers = numbers[mid_list:]


main()