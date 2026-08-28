def solution(n):
    answer = [n]
     
    while n != 1:
        # x가 짝수일 때 2로 나눠 x
        if n%2 == 0:
            n = n//2
            answer.append(n)
            
        # X가 홀수일 때 x를 3*x+1 로 바꾼다    
        else:
            n = 3*n+1
            answer.append(n)        
    
    
        
        
    # X가 홀수일 때 x를 3*x+1 로 바꾼다
    # 1이 될때까지 돌리고 그것을 리스트로 
    return answer