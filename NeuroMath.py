def mse(out_list, ideal_list):
    if len(out_list) != len(ideal_list):
        print('MSE ERROR: out_list != ideal_list')
    n = len(out_list)
    sum = 0
    for i in range(n):
        sum += (out_list[i] - ideal_list[i])**2
    result = sum / n
    return result

def f_sigmoid(out):
    return (1-out)*out
