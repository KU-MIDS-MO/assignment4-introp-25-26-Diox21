import numpy as np

def mask_and_classify_scores(arr):

    if type(arr) != np.ndarray:
        return None


    if arr.ndim != 2:
        return None


    n_rows, n_cols = arr.shape
    if n_rows != n_cols:
        return None
    if n_rows < 4:
        return None

    n = n_rows  

    cleaned = arr.copy()

    for i in range(n):
        for j in range(n):
            value = cleaned[i, j]
            if value < 0:
                cleaned[i, j] = 0
            elif value > 100:
                cleaned[i, j] = 100


    levels = np.zeros((n, n), dtype=int)

    for i in range(n):
        for j in range(n):
            value = cleaned[i, j]
            if value < 40:
                levels[i, j] = 0      
            elif value < 70:
                levels[i, j] = 1      
            else:
                levels[i, j] = 2      
    row_pass_counts = np.zeros(n, dtype=int)

    for i in range(n):
        count = 0
        for j in range(n):
            if cleaned[i, j] >= 50:
                count += 1
        row_pass_counts[i] = count

    return cleaned, levels, row_pass_counts
