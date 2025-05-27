import itertools
tap_sinh = list(itertools.chain(range(4), range(5,10), range(15,20)))
print(tap_sinh)
#[0, 1, 2, 3, 5, 6, 7, 8, 9, 15, 16, 17, 18, 19]
tap_sinh = list(zip(range(4), range(7, 12), reversed(range(11) ) ) )
print(tap_sinh)
#[(0, 7, 10), (1, 8, 9), (2, 9, 8), (3, 10, 7)]
