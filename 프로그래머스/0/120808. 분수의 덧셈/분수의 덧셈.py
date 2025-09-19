def solution(numer1, denom1, numer2, denom2):
    a = numer1*denom2 + numer2*denom1 #분자
    b = denom1*denom2 #분모

    #최대공약수 구하기
    result=[]
    for i in range(a,0,-1):
        if a%i ==0 and b%i==0:
            d=i # d 최대공약수
            break
    result.append(a/d)
    result.append(b/d)
    return result