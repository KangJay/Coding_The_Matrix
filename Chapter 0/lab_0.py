S = {-4, -2, 1, 2, 5, 0}
result = [{i, j, k} for i in S for j in S for k in S if i != j and j != k and i != k and (i + j + k) == 0]
print(result)