def solution(arr, queries):
    # 쿼리 꺼내기
    for query in queries:
        s = query[0]
        e = query[1]
        k = query[2]
        

        for i in range(s, e+1):
            if i%k == 0:
                arr[i] += 1
                
    # s <= i i <= e 
    # i%k == 0 일 때(=배수), arr[i] + 1
    # arr 반환
    
    return arr