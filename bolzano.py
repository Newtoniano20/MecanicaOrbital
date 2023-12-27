import numpy as np

def bolzano(f, guess=0, step=1):
    i = 10**5
    initial = f(guess)
    if -0.0001 < initial < 0.0001:
        return guess
    i_2 = f(guess+step)
    if (initial < i_2):
        step = -step
    while f(guess) > 0 and i > 0:
        guess += step
        i -= 1
    if i <= 0:
        raise Exception("No sign change or bad guess")
    return bolzano(f, guess=guess-step, step=step/1.5)



def f_test(x):
    return np.cos(x) + np.sin(x)
print(bolzano(f=f_test, guess=0))