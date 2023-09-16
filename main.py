from optimal.collections.circular_queue import CircularQueue


def main():
    q = CircularQueue(3)
    q.append(4)
    print(q)
    q.append(5)
    print(q)
    q.append(6)
    print(q)
    q.append(7)
    print(q)
