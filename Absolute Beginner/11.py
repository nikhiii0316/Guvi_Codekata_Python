'''You are given three numbers A, B & C. Print the largest amongst these three numbers.

Input Description:
Three numbers are provided to you.

Output Description:
Find and print the largest among the three

Sample Input :
1
2
3
Sample Output :
3'''

code:
  
arr = []
for i in range(3):
    arr.append(int(input()))
print(max(arr))    
