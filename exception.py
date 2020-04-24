
def devide(a,b):
    try:
      c=a/b
      return c

    except ZeroDivisionError:
        print('cannot devide with 0')
print(devide(0,5))
