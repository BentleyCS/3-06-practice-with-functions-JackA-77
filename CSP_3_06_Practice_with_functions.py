#Herons Formula
import math

#returns the square root of the number n
def root(n):
    return math.sqrt(n)

#Takes in the 3 side lengths of a triangle as arguments and returns half of
#the perimeter of a triangle.
def semiPerimeter(sl1, sl2, sl3):
    return((sl1 + sl2 + sl3)/2)

#Modify the below function such that it takes in 4 arguments. multiply the first
#argument by the difference between itself and each individual argument. Reference herons formula for more context.
def multiplyDifferences(a,b,c,d):
    return(a*(a-b)*(a-c)*(a-d))

#Given the 3 sides of a triangle return the area.
#use herons formula
#Use the functions above.
def herons(sl1, sl2, sl3):
    return root( multiplyDifferences(semiPerimeter(sl1, sl2, sl3), sl1, sl2, sl3))

#quadratic equation

#takes in a number as an argument and returns that number multiplied by 2.
def denominator(x):
    return (x*2)
#Takes in two arguments. multiply the first argument by negative 1. Then
#return the modified first argument added and subtracted by the second argument.
def plusMinus(j,k):
    return (j*-1) - k, (j*-1) + k
#takes in three numbers as arguments. The first and third multiplied together then
#multiplied by 4.Then subtract that result from the second argument squared.
#Return the overall result.
def mainCalc(t,u,v):
    return (u*u) - ((t*v)*4)
#The below function should take the inputs of the quadratic equation and return the result
#Make sure to use all the formulas from this section.
def quadratic(a,b,c):
    minus, plus = plusMinus(b,math.sqrt(mainCalc(a,b,c)))
    return plus/denominator(a), minus/denominator(a)