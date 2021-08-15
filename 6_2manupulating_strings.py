print('문자열 계산')
print('"in"은 True False를 반환하는 logical operator 로 작동할 수 있다.')
fruit='banana'

'n' in fruit#True
'm' in fruit#False
'nan' in fruit#True

print('if 함수와 같이 쓸 수 있다.')
if 'a' in fruit:
    print('a가 banana안에 있다.')
print('\n')
print('대소문자 변환')
print('대소문자로 변환해주는 "lower","upper"는 파이썬에 내장된 함수임')
print('원래 값을 변경시키지 않고 바뀐 결과값을 줌->받을곳이 필요함')

a = fruit.lower()
A = fruit.upper()
print(a)
print(A)

print('\n')
print('위치찾기')
pos=fruit.find('na')
print(pos)
print('banana에서 앞의 na 가 2번째 나왔다는걸 의미')
aa=fruit.find('aa')
print(aa)
print('없으면 -1 줌')
print('\n')
print('검색하고 바꾸기')
nstr = fruit.replace('ba','ca')
print(nstr)
print('banana에서 ba 를 ca로 바꾼것')

print('공백자르기')
vegetable = '          carrot          '
print(vegetable)
print('↑그냥출력')
print(vegetable.lstrip())
print('↑왼쪽 자른거 lstrip')
print(vegetable.rstrip())
print('↑오른쪽 자른거 rstrip')
print(vegetable.strip())
print('↑그냥 strip')

print('\n')
print('prefix 접두사')
print('이것도 파이썬 내장함수로 처리결과를 받을 새로운 곳 필요')
line = 'please have a seat'
print(line.startswith('please'))
print('↑line이 please로 시작하냐')
print(line.startswith('P'))
print('↑line이 P로 시작하냐')
print(line.startswith('t'))
print('↑line이 t로 시작하냐')

print('\n')
print('구분짓기, 추출하기')
data = 'suk941217@hanmail.net Sat Jan 07/25 2021'
print("data = 'suk941217@hanmail.net Sat Jan 07/25 2021'")
atpos = data.find('@')
print(atpos)
print('find("@")로 @위치 찾기')
spos = data.find(' ', atpos)
print('find(a,b) b나온 이후부터 a 위치 찾기')
print(spos)
host = data[atpos:spos]
print(host)
