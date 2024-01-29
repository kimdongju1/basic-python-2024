# date : 20240129
# desc : 자료형 

## 기본자료형 - 숫자형, 문자형, 불형, None형...  
## 추가자료형 - 리스트형, 튜플형, 딕셔너리, 집합... (집합형은 나중에)

## None형 == null(C, C++, C#, Java, SQL) 
## 값은 값인데 아무것도 지정할 수 없는 값 => None

apple = None
print(apple)

## 숫자형 - 정수형, 실수형, 진수형 
ten = 10 
hundred = 100 
temp = -8

### 실수 
pi = 3.141592 
tax_rate = 10.0 
emp_earn_rate = 3.3
test_val = 2e10 
print(test_val)

### 진수 
bit8 = 0b10001110
oct9 = 0o10
hex255 = 0xff
print(bit8)
print(oct9)
print(hex255)

## 문자형 - 파이썬에는 문자, 문자열 차이가 없음 
greeting = 'Hello!'
greeting = "Hello!" # 홑따옴표, 쌍따옴표 모두 문자열 나타냄 
print(greeting)
multi_str = '''Hello\n
I am a programmer. \n
Have a good afternoon.''' # 홑따옴표 ''', 쌍따옴표 """ 동일 
print(multi_str)
multi_str2 = ('Line1\n'
              'Line2\n'
              'Line3')    # () 를 다 쓰거나, 문장 끝마다 \를 붙이기 

print(multi_str2)

## 불형 (Bool, Boolean)
isCheck = False
print(isCheck)

isCheck = True
print(isCheck)

answer = (3 == 6)
print(answer)
answer = (3.0 == 3)
print(answer)

## 자료형이 어떤 타입인지 체크
print(type(apple))
print(type(hundred))
print(type(test_val))
print(type(hex255))
print(type(greeting))
print(type(isCheck))