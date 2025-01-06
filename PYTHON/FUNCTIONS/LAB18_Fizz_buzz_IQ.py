# Write a program the prints numbers from 1 to 100
# However for the multiple of 3 print "FIZZ" instead of Number
# and For multiples of 5 print "Buzz ".
# For the numbers that are multiple of both 3 and 5 print "FIZZBUZZ".(for,if)


for number in range(1,101):
    # print(number)
    if number % 3 == 0 and number % 5 == 0:
        print("FIZZBUZZ")
    elif number % 5 == 0:
        print("BUZZ")

    elif number % 3 == 0 :
        print("FIZZ")
    else:
        print(number)