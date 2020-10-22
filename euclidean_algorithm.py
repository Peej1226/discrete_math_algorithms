# @https://en.wikipedia.org/wiki/Euclidean_algorithm
# single line of input, two number seperated by a space, then converted into two ints
print("enter two numbers seperated by a space")
numb, divisor = [int(x) for x in input("=> ").split()]
print("-")
rmd = 1
while rmd > 0:
    # flip to always divide the larger number by the smaller
    if divisor > numb:
        numb, divisor = divisor, numb
    print("The number is {} and the divisor is {}".format(numb, divisor))
    rmd = numb % divisor
    print("The quotient is {} and the remainder is {}".format(int(numb / divisor), rmd))
    print("-")
    # as apart of the Euclidean Algorithm, the initial larger number is replaced by the smaller
    # and the remainder takes the place of the smaller number, assign just once here, switch when
    # the while loop starts again, we don't switch now, because if we are done and the loop exits,
    # the divisor is the greatest common divisor.
    numb = rmd
print("The greatest common divisor is", divisor)
