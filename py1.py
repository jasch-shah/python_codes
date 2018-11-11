n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(0,N):
	cmd = input().split()
	func = cmd[0]
	if func == "pop":
		s.pop()
	else:
		arg = cmd[1]
		eval('s.{0}({1})'.format(func,arg))
print(sum(s))			