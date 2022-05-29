import numpy as np

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

