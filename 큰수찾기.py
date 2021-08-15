print('큰 숫자 찾기')
print('여태까지 가장 큰 것과 새로운것 비교')

largest_so_far = -1

for a in [9,41,12,3,74,15]:
    if a > largest_so_far:
        largest_so_far = a
    print(largest_so_far,a)
