'''
outputstandard output
Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given n numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given n numbers finds one that is different in evenness.

Input
The first line contains integer n (3 ≤ n ≤ 100) — amount of numbers in the task. The second line contains n space-separated natural numbers, not exceeding 100. It is guaranteed, that exactly one of these numbers differs from the others in evenness.

Output
Output index of number that differs from the others in evenness. Numbers are numbered from 1 in the input order.
'''

n = int(input())
l = list(map(int, input().split()))

j = 0
o = 0
if l[0] % 2 == 0:
    o += 1
else:
    j += 1

if l[1] % 2 == 0:
    o += 1
else:
    j += 1

if l[2] % 2 == 0:
    o += 1
else:
    j += 1

if j > o:
    for i in range(n):
        if l[i] % 2 == 0:
            print(i + 1)
            break
else:
    for i in range(n):
        if l[i] % 2 == 1:
            print(i + 1)
            break

