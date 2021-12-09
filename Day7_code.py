def part1():
    res=[]
    res=[int(i) for i in res]
    ans=float("inf")
    for i in range(min(res), max(res)+1):
        diff=sum(abs(i-j) for j in res)
        ans=min(ans, diff)
    print(ans)
def part2():
    res=[]
    res=[int(i) for i in res]
    ans=float("inf")
    for i in range(min(res), max(res)+1):
        diff=sum(abs(i-j)*(abs(i-j)+1)//2 for j in res)
        ans=min(ans, diff)
    print(ans)

if __name__ == '__main__':
	with open("C:\\Users\\Ge007543\Documents\\day7.txt") as f:
		res = f.read().split(",")
	part1(res)
	part2(res)
