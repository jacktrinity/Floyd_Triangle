def floyd_triangle(user_input):
    triangle_list = []
    temp_list = []

    index = 0
    range_list = 1

    while index < user_input:
        temp_list.append(range_list)
        range_list += 1

        if len(temp_list) > index:
            triangle_list.append(temp_list)
            index += 1
            temp_list = []

    return triangle_list


def forward_triangle(triangle_list):
    print("Floyd's Triangle:")
    for each_list in triangle_list:
        temp_string = ""
        for num in each_list:
            temp_string += str(num) + " "
        print(temp_string)


def reverse_triangle(triangle_list):
    print("Reverse Floyd's Triangle:")
    for each_list in reversed(triangle_list):
        temp_string = ""
        for num in each_list:
            temp_string += str(num) + " "
        print(temp_string)


def possible_input():
    try:
        possible_user_input = int(input("Please enter in a number: "))
        return possible_user_input
    except ValueError:
        print("Invalid Input")
        return possible_input()


# Main Body
number_input = possible_input()
floyd_list = floyd_triangle(number_input)

forward_triangle(floyd_list)
print()
reverse_triangle(floyd_list)
