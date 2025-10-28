def data (sentence):
    dict = {}
    for x in sentence:
        if x in dict:
            dict.update({x: dict[x]+1})
        else:
            dict.update({x: 1})
    print(dict)

data('all')