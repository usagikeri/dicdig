def dicdig(dic, word):
    if type(dic) == dict:
        for key in list(filter(lambda x: (x == word) or
                                         (type(dic[x]) == dict) or
                                         (type(dic[x]) == list), dic.keys())):
            if key == word:
                return dic[key]
            else:
                val = dic[key]
                if type(val) == dict:
                    return dicdig(val, word)
                elif type(val) == list:
                    for i in list(filter(lambda x: (type(x) == dict) or
                                                   (type(x) == list), val)):
                        if type(i) == dict:
                            if dicdig(i, word) is not None:
                                return dicdig(i, word)
                        else:
                            if dicdig(i, word) is not None:
                                return dicdig(i, word)
    elif type(dic) == list:
        for j in list(filter(lambda x: (type(x) == dict) or
                                       (type(x) == list), dic)):
            if type(j) == dict:
                if dicdig(j, word) is not None:
                    return dicdig(j, word)
            elif type(j) == list:
                for k in list(filter(lambda x: (type(x) == dict) or
                                               (type(x) == list), j)):
                    if dicdig(k, word) is not None:
                        return dicdig(k, word)


if __name__ == "__main__":
    d = {"a": 1, "b": [{"c": 3},
         {"d": [[1], [{"g": 5},
          {"e": "Goal!!", "f": 4}]]}]}
    x = dicdig(d, "e")
    print(x)
