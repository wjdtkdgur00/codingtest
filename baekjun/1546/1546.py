
n = int(input())
score = list(map(int, input().split()))
max_score = max(score)
for i in range(len(score)):
    score[i] /= max_score
    score[i] *= 100
print(sum(score) / len(score))