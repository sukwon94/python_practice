print('문자열')
print('문자열의 배열은 대괄호로 나타내고 수식을 포함할 수 있다.')

fruit = 'banana'
letter = fruit[1]
print(letter)


x=3
w=fruit[x-1]
print(w)
print('문자열 자르기')
print('"문자열[a:b]" a부터 b까지, b는포함안함')
print('자르기 범위에 아무것도 안나오게 설정해도 Traceback 안나옴 빈칸으로 출력됌')
print(fruit[2:4])
print(fruit[:5])
print(fruit[:6])
print(fruit[3:])
print(fruit[:])
print(fruit[-1:2])#빈칸
print(fruit[:-1])#banan
print(fruit[-5:-1])
print(fruit[-6:-1])
print(fruit[-1:-1])
