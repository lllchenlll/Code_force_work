'''
Vasya has found a strange device. On the front panel of a device there are: a red button, a blue button and a display showing some positive integer. After clicking the red button, device multiplies the displayed number by two. After clicking the blue button, device subtracts one from the number on the display. If at some point the number stops being positive, the device breaks down. The display can show arbitrarily large numbers. Initially, the display shows number n.

Bob wants to get number m on the display. What minimum number of clicks he has to make in order to achieve this result?

Input
The first and the only line of the input contains two distinct integers n and m (1 ≤ n, m ≤ 104), separated by a space .

Output
Print a single number — the minimum number of times one needs to push the button required to get the number m out of number n.
'''

instr = list(map(int, input().split(" ")))
num = 0
while instr[0] < instr[1]:
    if instr[1] % 2:
        instr[1] += 1
    else:
        instr[1] //= 2
    num += 1
print (instr[0] - instr[1] + num)

