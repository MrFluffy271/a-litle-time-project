import time
def main():
    global result
    global time
    time = time.strftime('%H:%M:%S')
    if time > '06:00:00' and time < '12:00:00':
        result = ("Good Morning Python!")
    elif time > '12:00:00' and time < '18:00:00':
        result = ('Good Noon Pyhton!')
    elif time > '18:00:00' and time < '24:00:00':
        result = ('Good Night Pyhton!')
    elif time > '24:00:00' and time < '06:00:00':
        result = ('Good Sleeping Pyhton!')
    print('-------------------')
    print(result)
    print('-------------------')
    print('The Time Is:')
    print(time)
    print('-------------------')
main()
