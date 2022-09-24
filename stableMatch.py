for t in range(int(input())):
    n = int(input())
    women = [[]] * n
    men = [[]] * n
    for i in range(n):
        woman = [int(x) for x in input().split()]
        women[woman[0] - 1] = woman[1:]
    for i in range(n):
        man = [int(x) for x in input().split()]
        men[man[0] - 1] = man[1:]
    engagements = [None] * n
    i = -1
    while None in engagements:
        i = (i + 1) % n
        man = men[i]
        for woman in man:
            if woman not in engagements:
                engagements[i] = woman
                break
            try:
                rank = women[woman - 1].index(i + 1)
                if rank <= women[woman - 1].index(engagements.index(woman) + 1):
                    engagements[engagements.index(woman)] = None
                    engagements[i] = woman
                    break
            except Exception:
                pass
    for i,man in enumerate(engagements):
        print(f'{i + 1} {man}')