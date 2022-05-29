import numpy as np
'''
Example Calculate([0,1,2,3,4,5,6,7,8])

Result:
{
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
  'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
  'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
  'max': [[6, 7, 8], [2, 5, 8], 8],
  'min': [[0, 1, 2], [0, 3, 6], 0],
  'sum': [[9, 12, 15], [3, 12, 21], 36]
}
'''
def calculate(numbers):
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")
    arr = np.reshape(np.array(numbers),(3,3))
    calculations = {}
    calculations['mean'] = [np.mean(arr, 0).tolist(), np.mean(arr, 1).tolist(), np.mean(arr).tolist()]
    calculations['variance'] = [np.var(arr, 0).tolist(), np.var(arr, 1).tolist(), np.var(arr).tolist()]
    calculations['standard deviation'] = [np.std(arr, 0).tolist(), np.std(arr, 1).tolist(), np.std(arr).tolist()]
    calculations['max'] = [np.max(arr, 0).tolist(), np.max(arr, 1).tolist(), np.max(arr).tolist()]
    calculations['min'] = [np.min(arr, 0).tolist(), np.min(arr, 1).tolist(), np.min(arr).tolist()]
    calculations['sum'] = [np.sum(arr, 0).tolist(), np.sum(arr, 1).tolist(), np.sum(arr).tolist()]
    return calculations

