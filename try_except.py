#. try & except

x=3
y='bob'
try:
    print(x+y)
except:
    print('dont add string with numbers')
#    quit()

#. right dangerous code in try indent. it would be safe factor
#. too much code in try could make you hard to find where the traceback happened
#. we can use quit() in except indent to not make more traceback further
