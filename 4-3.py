# 프로그래머스 Lv.1 로또의 최고 순위와 최저 순위

def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    result = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[result + ans], rank[ans]