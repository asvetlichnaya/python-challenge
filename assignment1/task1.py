# Assignment1, Task1

# Write a function (or just code without a function around it) that will print into the console integer numbers
# from 1 to 100.

# In addition, an algorithm should print in the same row as number specific word (or words) i.e.:

# For each number divisible by three it should print “number-that-is-divisible-by-three” and “Fizz” word
# (e.g: “3 – Fizz”)
# For each number divisible by five it should print “number-that-is-divisible-by-five” and “Buzz” word
# (e.g.: “5 – Buzz”)
# If a number is divisible by both three and five it should print “FizzBuzz” word (e.g.: “15 – FizzBuzz”)


for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        print(x, " - FizzBuzz")
    elif x % 5 == 0:
        print(x, ' – Buzz')
    elif x % 3 == 0:
        print(x, ' - Fizz')
    else:
        print(x)
