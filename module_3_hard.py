
sm = 0


def summ(s):
    global sm
    if isinstance(s, dict):
        for i in s:
            sm += s[i]
    if isinstance(s, int) or isinstance(s, str):
        if isinstance(s, int):
            sm += s
        else:
            sm += len(s)
        return
    for i in s:
        summ(i)


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

summ(data_structure)
print(sm)
