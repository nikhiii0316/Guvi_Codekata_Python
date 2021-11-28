'''You are provided with a number, "N". Find its factorial.
n = int(input())
product = 1
for i in range(1,n+1):
    product *= i
print(product)
Input Description:
A positive integer is provided as an input.

Output Description:
Print the factorial of the integer.

Sample Input :
2
Sample Output :
2'''

code:
  
n = int(input())
product = 1
for i in range(1,n+1):
    product *= i
print(product)
