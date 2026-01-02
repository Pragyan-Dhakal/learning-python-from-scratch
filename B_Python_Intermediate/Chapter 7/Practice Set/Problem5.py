#Write a program to find the sum of first 10 n natural number using while loops.
n = int(input("Enter a number: "))
i =1
sum = 0
while i<=n:
    sum+=i
    i=i+1

print(sum)