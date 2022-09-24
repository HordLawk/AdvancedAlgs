k = int(input())

for _ in range(k):
    board = [[int(x) for x in input().split()] for _ in range(8)]
    maxScore = 0
    def backtracking(row: int, score: int, queens: list[int]) -> None:
        if row == 8:
            global maxScore
            if score > maxScore:
                maxScore = score
            return
        for column in range(8):
            if(
                (column not in queens[:row])
                and
                all(
                    [
                        (abs(otherRow - row) != abs(otherColumn - column))
                        for otherRow,otherColumn
                        in enumerate(queens[:row])
                    ]
                )
            ):
                queens[row] = column
                backtracking(row + 1, score + board[row][column], queens)
    backtracking(0, 0, [0 for _ in range(8)])
    print(str(maxScore).rjust(5))