import pandas as pd


def judge_1(a):
    for b in str(a):
        if(b == "1"):
            result = 1
            break
    else:
        result = 0
    return result


a = list()
ran = 100000000000000000000000000
keta = 100000000
_sum = 0.0
j = 0
_j = list()
_result = list()

for i in range(ran):
    if(j % keta == 0):
        print(f'{j/keta}:   {_sum}')
        _j.append(j/keta)
        _result.append(_sum)
        dict = {"num": _j, "result": _result}
        df = pd.DataFrame(dict)
        df.to_csv("result.csv")
    j = i+1
    if(judge_1(j) == 0):
        num = 1/j
        _sum += num
    else:
        continue
