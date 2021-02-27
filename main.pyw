import time
def main():
    global time
    time = time.strftime('%H:%M:%S')
    if time > '06:00:00' and time < '12:00:00':
        print("Good Morning Python!")
    elif time > '12:00:00' and time < '18:00:00':
        print('Good Noon Pyhton!')
    elif time > '18:00:00' and time < '24:00:00':
        print('Good Night Pyhton!')
    elif time > '24:00:00' and time < '06:00:00':
        print('Good Sleeping Pyhton!')
    print('-------------------')
    print('The Time Is:')
    print(time)
    print('-------------------')
main()
