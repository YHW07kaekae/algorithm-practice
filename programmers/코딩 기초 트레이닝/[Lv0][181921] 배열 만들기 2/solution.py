def solution(l, r):
    answer = []
    count = 0
    
    # l과 r 사이 정수 찾기
    for numbers in range(l, r + 1):
        
        
    # 이 정수는 '0'과 '5'로 구성돼야 함
    # 자리마다 0인지 5인지 구분 -> 하나씩 뽑아 0인지 5인지 확인 -> 텍스트 돼야함 -> 0도 아니고 5도 아닌 수 탈락
        number = str(numbers)
        what = True
        for char in number:
            if char != '0' and char != '5': # 0도 5도 아니다.
                what = False
                
        if what == True:
            answer.append(numbers)
            count += 1
                
    if count == 0:
        
        return [-1]
            
            

                
            
    # 모든 정수를 오름차순으로 저장한 배열 return
        
    
    
    return answer