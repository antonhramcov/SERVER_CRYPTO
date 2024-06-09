from statistics import mean

def add_new_price(dic1:dict):
    with open('prices.txt', 'r') as f:
        strings = list(map(lambda x: x.rstrip(), f.readlines()))
    dic2 = {}
    for string in strings:
        s = string.split()
        dic2[s[0]] = s[1:]
    for key,val in dic1.items():
        if len(dic2[key])==1440:
            dic2[key].pop(0)
        dic2[key].append(dic1[key])
    with open('prices.txt', 'w') as f:
        for key, val in dic2.items():
            f.write(key+' ')
            for price in dic2[key]:
                f.write(price+' ')
            f.write('\n')

def calc_characteristics():
    with open('prices.txt', 'r') as f:
        strings = list(map(lambda x: x.rstrip(), f.readlines()))
    dic2 = {}
    for string in strings:
        s = string.split()
        dic2[s[0]] = list(map(float, s[1:]))
    dic_avg = {}
    for key, val in dic2.items():
        dic_avg[key] = {'avg':str(mean(dic2[key]))}
        dic_avg[key]['min'] = str(min(dic2[key]))
        dic_avg[key]['max'] = str(max(dic2[key]))
        dic_avg[key]['last'] = str((dic2[key])[-1])
    return dic_avg
