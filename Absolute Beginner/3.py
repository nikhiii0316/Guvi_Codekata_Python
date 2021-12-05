'''You are given a number A in Kilometers. Convert this into B: Meters and C: Centi-Metres.

Input Description:
A number "A" representing some distance in kilometer is provided to you as the input.

Output Description:
Convert and print this value in meters and centimeters.

Sample Input :
2
Sample Output :
2000
20000'''

code:
  
km = int (input())
mtr = (km * 1000)
cent = (km * 100000)
print(mtr)
print(cent)
