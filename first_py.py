
"""def count_upper_case(message):

    Count the number of upper case characters in a given message
    `message` is the piece of text to be checked

    Returns the number of uppercase characters in a message

    return sum([1 for c in message if c.isupper()])


assert count_upper_case("") == 0, "Empty string"
assert count_upper_case("A") == 1, "One upper case"
assert count_upper_case("AA") == 2, "Two upper case"
assert count_upper_case("a") == 0, "One lower case"


# An example of a failed test would be -
# assert count_upper_case("A") == 0, "One upper case"

print("All the tests passed")"""



def even_number_of_events(numbers):
    if numbers == []:
        return False
    else:
        # Set a `number_of_evens` variable that will be incremented each time
        # an even number is found
        evens = 0

    # Iterate of over each item and if it's an even number, increment the
    # `evens` variable
    for number in numbers:
        if number % 2 == 0:
            evens += 1

    if evens == 0:
        return False
    else:
        return even

#test23

assert even_number_of_events([]) == False, "No numbers"
assert even_number_of_events([2]) == False, "One even number"
#assert even_number_of_events([2, 4]) == True, "Two even numbers"
assert even_number_of_events([2, 3]) == False, "Two numbers, only one even"
assert even_number_of_events([2, 3, 9, 10, 1, 7, 8]) == False, "Multiple numbers, three even"
#assert even_number_of_events([2, 3, 9, 10, 1, 7, 8, 5, 12]) == True, "Multiple numbers, four even"
assert even_number_of_events([1, 2, 9]) == False, "No even numbers"

print