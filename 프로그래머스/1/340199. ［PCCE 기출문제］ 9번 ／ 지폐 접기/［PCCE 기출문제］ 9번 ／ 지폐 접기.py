def solution(wallet, bill):
    wallet = sorted(wallet)
    bill = sorted(bill)
    answer = 0

    while bill[0] > wallet[0] or bill[1] > wallet[1]:
        if bill[0] > bill[1]:
            bill[0] //= 2
        else:
            bill[1] //= 2
        bill = sorted(bill)
        answer += 1
    return answer