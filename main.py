from multiprocessing.pool import ThreadPool


def function(arg):
    answer = 0
    for _ in range(arg):
        answer += 1
    return answer


def generator(n):
    while n > 0:
        yield 10000
        n -= 1


def main():
    num_processes = 5
    with ThreadPool(processes=num_processes) as pool:
        a = sum(pool.map(function, generator(num_processes)))
    print("----------------------", a)


main()
