def chk(N):
    cnt = 0
    if N<100:
        cnt += 1
    else:
        for i in range(100, N+1):
            n_hundred = (i//100)
            n_ten = (i%100)//10
            n_one = (i%100)%10
            if (n_hundred - n_ten) == (n_ten - n_one):
                cnt += 1
        return cnt+99
    return N
if __name__ == "__main__":
    N = int(input())
    res = chk(N)
    print(res)