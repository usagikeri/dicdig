
def dicdig(dic, word):
    for key in list(filter(lambda x: (x == word) or \
                                     (type(dic[x]) == dict) or \
                                     (type(dic[x]) == list), dic.keys())):
        if key == word:
            return dic[key]
        else:
            val = dic[key]
            if type(val) == dict:
                return dicdig(val, word)
            elif type(val) == list:
                for d in val:
                    if type(d) == dict:
                        if dicdig(d, word) != None:
                            return dicdig(d, word)
                    else:
                        raise ValueError("Error: unexpected struct of dictionary.")
                        break


if __name__ == "__main__":
    d = {"a": 1, "b": [{"c": 3}, {"d": [{"e": "Goal!!", "f": 4}]}]}
    x = dicdig(d, "e")
    print(x)
