from threading import Thread

a = 0


def function(arg):
    global a
    temp = 0
    for _ in range(arg):
        temp += 1
    a += temp


def main():
    threads = []
    for i in range(5):
        thread = Thread(target=function, args=(1000000,))
        thread.start()
        threads.append(thread)

    [t.join() for t in threads]
    print("----------------------", a)


main()
