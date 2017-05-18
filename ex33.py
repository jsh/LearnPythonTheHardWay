
def loop(d, increment):
    i = 0
    numbers = []

    for i in range(0, d, increment):
        print "At the top, i is %d" % i
        numbers.append(i)

        print "numbers now ", numbers
        print "At the bottom, i is %d" % i

    print "The numbers:"

    for num in numbers:
        print num

loop(4, 2)
