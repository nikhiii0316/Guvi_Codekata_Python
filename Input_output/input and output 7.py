'''Write a code to get the input in the given format and print the output in the given format

Input Description:
A single line contains a string.

Output Description:
Print the characters in a string separated by space.

Sample Input :
guvi
Sample Output :
g u v i'''

code:
  
a = input()
n = len(a)
for i in a[:n-1]:
       print(i, end =" ")
print(a[n-1])
       
       
       
