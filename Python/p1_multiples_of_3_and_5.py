# Multiples of 3 and 5
# Problem 1
#
# https://projecteuler.net/problem=1
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

def sum_of_multiples(incl_range=[0,1,2,3], multiples=[3,5]):
    matching_critera = []
    for num in incl_range:
        for mutli in multiples:
            if num % mutli == 0:
                matching_critera.append(num)
                break
    return sum(matching_critera)

# test case expect to equal 23
if sum_of_multiples(range(1,10),[3,5]) == 23:
    print "success"

print sum_of_multiples(range(1,1000),[3,5])
