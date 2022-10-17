def miniMaxSum(A):
  total = sum(A)
  print(total - max(A), end= ' ')
  print(total - min(A))
miniMaxSum([1,3,5,7,9])