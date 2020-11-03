def solution(number, k):
    answer = ''
    num = list(number) 
    stack = [num[0]] 
    count = 0
    
    for i in range(1,len(num)):
        if count == k:
            stack = stack + num[i:]
            break
        
        stack.append(num[i])
        if stack[-1] > stack[-2]:
            while len(stack) != 1 and stack[-1] > stack[-2] and count < k:
                del stack[-2]
                count += 1
    return "".join(stack[:len(num)-k])



# 문제에 대한 해설은 https://datacodingschool.tistory.com/170
