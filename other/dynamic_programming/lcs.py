from functools import lru_cache

@lru_cache(maxsize=None)
def lcs_length(seq_x, seq_y):
    if not seq_x or not seq_y:
        return 0
    elif seq_x[-1] == seq_y[-1]:
        return 1 + lcs_length(seq_x[:-1], seq_y[:-1])
    else:
        return max(lcs_length(seq_x[:-1], seq_y),
                   lcs_length(seq_x, seq_y[:-1]))


X = "AGGTABoinslklaaoinqf"
Y = "GXTXAYBgkfnoifomqenfop"
print(lcs_length(X, Y))