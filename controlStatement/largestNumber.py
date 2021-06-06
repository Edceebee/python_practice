# (Find the Largest Number) The process of finding the largest value is used frequently in computer
# applications. For example, a program that determines the winner of a sales contest would input the number of units
# sold by each salesperson. The salesperson who sells the most units wins the con-test. Write a pseudocode program
# , then a Java application that inputs a series of 10 integers and deter-mines and prints the largest integer.

def findLargestNumber():
    numbers = input("Enter numbers to compare separated by space: ")
    newNumbers = list(map(int, numbers.split()))

    for number in newNumbers:
        largestNumber = number

        if number > largestNumber:
            largestNumber = number

    print(f'largest number is {largestNumber}')


findLargestNumber()
