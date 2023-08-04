if __name__=='__main__':
    N = int(input())
    words = set()
    for _ in range(N):
        word = input()
        words.add((word, len(word)))
        
    W = sorted(words, key = lambda x:(x[1], x[0]))
    
    for i in W:
        print(i[0])