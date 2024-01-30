# desc : 홀수/짝수 구분 또는 배수 
number = int(input('정수입력 > ')) # 입력받은 후 정수로 변경

if number % 2 == 0: # 짝수
    print('2의 배수!')
else: # 홀수
    print('나머지수!')