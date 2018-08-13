'''
Valera has got a rectangle table consisting of n rows and m columns. Valera numbered the table rows starting from one, from top to bottom and the columns – starting from one, from left to right. We will represent cell that is on the intersection of row x and column y by a pair of integers (x, y).

Valera wants to place exactly k tubes on his rectangle table. A tube is such sequence of table cells (x1, y1), (x2, y2), ..., (xr, yr), that:

r ≥ 2;
for any integer i (1 ≤ i ≤ r - 1) the following equation |xi - xi + 1| + |yi - yi + 1| = 1 holds;
each table cell, which belongs to the tube, must occur exactly once in the sequence.
Valera thinks that the tubes are arranged in a fancy manner if the following conditions are fulfilled:

no pair of tubes has common cells;
each cell of the table belongs to some tube.
Help Valera to arrange k tubes on his rectangle table in a fancy manner.

Input
The first line contains three space-separated integers n, m, k (2 ≤ n, m ≤ 300; 2 ≤ 2k ≤ n·m) — the number of rows, the number of columns and the number of tubes, correspondingly.

Output
Print k lines. In the i-th line print the description of the i-th tube: first print integer ri (the number of tube cells), then print 2ri integers xi1, yi1, xi2, yi2, ..., xiri, yiri (the sequence of table cells).

If there are multiple solutions, you can print any of them. It is guaranteed that at least one solution exists.
'''

def next(x, y, xx):
    if x == n and xx == 1:
        y += 1
        xx *= -1
    elif x == 1 and xx == -1:
        y += 1
        xx *= -1
    else:
        x += xx

    return x, y, xx

n, m, num = map(int, input().split(" "))
x = 1
xx = -1
y = 0
for i in range(num - 1):
    j = 0
    s = "2 "
    while j < 2:
        x, y, xx = next(x, y, xx)
        s += "{} {} ".format(str(x), str(y))
        j += 1
    print(s)
s = str(n * m - 2 * (num - 1)) + " "
for i in range(n * m - 2 * (num - 1)):
    x, y, xx = next(x, y, xx)
    s += "{} {} ".format(str(x), str(y))
print(s)
