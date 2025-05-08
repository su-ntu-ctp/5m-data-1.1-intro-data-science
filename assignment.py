# Question 1

# Write a function that prints "Fizz" when the number is divisible by 3, "Buzz" when the number is divisible by 5
# and "FizzBuzz" when the number is divisible by both 3 and 5.
# If the number is not divisible by either 3 or 5, the function should return the number itself.


def fizz_buzz(number):
    """Returns Fizz if number is divisible by 3, Buzz if divisible by 5, FizzBuzz if divisible by both 3 and 5.
    If not divisible by either 3 or 5, returns the number itself.
    >>> fizz_buzz(3)
    'Fizz'
    >>> fizz_buzz(5)
    'Buzz'
    >>> fizz_buzz(15)
    'FizzBuzz'
    """

    if (number % 3 == 0 and number % 5 != 0): # divisible by 3 but not 5
        return ('Fizz')
    elif (number % 3 != 0 and number % 5 == 0): # divisible by 5 but not 3 
        return ('Buzz')
    elif (number % 3 == 0 and number % 5 == 0): # divisible by 3 and 5
        return ('FizzBuzz')
    else: # not divisible by 3 or 5
        return(number)


# Question 2

# Write a function that takes a list of numbers and returns the sum of the squares of all the numbers.


def sum_of_squares(numbers):
    """Returns the sum of the squares of all the numbers in a list.
    >>> sum_of_squares([1, 2, 3])
    14
    >>> sum_of_squares([2, 4, 6])
    56
    """
    sum = 0
    for x in numbers:
        sum += x * x # square and add to sum

    return (sum)


# Question 3

# Write a function that counts the number of vowels in a string.


def count_vowels(string):
    """Returns the number of vowels in a string.
    >>> count_vowels("hello")
    2
    >>> count_vowels("aeiou")
    5
    """
    num_vowels = 0
    for x in string:
        if (x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u'):
            num_vowels += 1 # add to num_vowels if character is a vowel

    return (num_vowels)


# Question 4

# Write a function that counts the number of repeated characters in a string.


def count_repeats(string):
    """Returns the number of repeated characters in a string.
    >>> count_repeats("hello")
    2
    >>> count_repeats("aeiou")
    0
    """

    char_count_dict = {} # creates a dictionary of the characters to count the number of times the character appears
    for x in string:
        if x in char_count_dict: # check if the character is already in the dictionary
            char_count_dict[x] += 1 # increment if it has already appeared previously
        else:
            char_count_dict[x] = 1 # initialize to 1 if this is the first time it appears
    
    num_char_repeats = 0
    for x in char_count_dict.values():
        if x > 1:
            num_char_repeats += x # not sure why repeated characters are counted by the number of times it appears. Shouldn't the it be counted as one regardless of how many times it appears?
    
    return (num_char_repeats)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
