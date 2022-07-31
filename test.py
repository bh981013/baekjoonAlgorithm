from itertools import product

if __name__ == '__main__':
    iterator1 = ['A', 'B', 'C']
    iterator2 = ['1', '2', '3']

    for i in product(iterator1, iterator2, repeat=2):
        print(i)
