#

def consumer():
    r = "wp"
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def producer(g):
    r = g.send(None)
    print(r)
    n = 0
    while n < 1:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = g.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    g.close()


if __name__ == "__main__":
    g = consumer()
    producer(g)
