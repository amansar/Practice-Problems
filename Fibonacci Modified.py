Problem link:https://www.hackerrank.com/challenges/fibonacci-modified
def findTerm(first, second, third):
    third = third - 2
    for i in range(third):
        total = (second * second) + first
        first = second
        second = total
    return total

def main():
    first, second, third = input().split(' ')
    first = int(first)
    second = int(second)
    third = int(third)
    theTerm = findTerm(first, second, third)
    print(theTerm)
    
main()
