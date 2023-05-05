import numpy as np
import math
from numpy import log as ln


def round_to(num, digits=6):
    if num == 0: return 0
    scale = int(-math.floor(math.log10(abs(num - int(num))))) + digits - 1
    if scale < digits: scale = digits
    return round(num, scale)

def mse(w, t, p):
    return -sum(w*(t - p)) / sum(w)


def msle(w, t, p):
    one = np.array([1] * len(p))
    first = ln(one + t)
    second = ln(one + p)
    return -sum(2*w*(first - second)/(p + one)) / sum(w)

def logloss(w, t, p):
    one = np.array([1] * len(p))
    c = np.array([max(max(t), max(p)) + 1] * len(p))
    first = t / p
    second = (c - t) / (c - p)
    return -sum(w * (first - second)) / sum(w)


# X_next = X_prev - eta * mse_proiz
def grad_func(metric, w, t):
    e = 0.000000001
    eta = 0.25
    start_p = np.min(t)
    next_p = start_p - eta * metric(w, t, np.array([start_p] * len(t)))
    while abs(next_p - start_p) > e:
        start_p = next_p
        next_p = start_p - eta * metric(w, t, [start_p] * len(t))
    return start_p


n, m = map(int, input().split())
a, b = [], []
for i in range(n):
    tmp_arr = list(map(float, input().split()))
    a.append(tmp_arr[m])
    b.append(tmp_arr[m + 1])

t = np.array(a) / np.array(b)
w = np.array(b)

print(round_to(grad_func(mse, w, t), 6), end=' ')
print(round_to(grad_func(msle, w, t), 6), end=' ')
print(round_to(grad_func(logloss, w, t), 6), end=' ')