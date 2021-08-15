print('루프에서 숫자세기')
c=0
for thing in [9,41,12,3,74,15]:
    c = c+1
    print(c , thing)

print('루프에서 합계구하기')
s=0
for thing in [9,41,12,3,74,15]:
    s = s + thing
    print(s, thing)

print('루프에서 평균구하기')
a=0
v=0
for thing in [9,41,12,3,74,15]:
    a = a+1
    v = v+thing
print('합:', v, '평균:', (v/a))

print('루프에서 가장 작은수 구하기')#가장 큰 수는 따로 안적겠음.
smallest = None
for thing in [9,41,12,3,74,15]:
    if smallest is None:
        smallest = thing
    elif smallest > thing:
        smallest = thing
print(smallest)
