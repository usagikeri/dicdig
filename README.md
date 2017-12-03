# DicDig
This is a tool to dig a dictionary.

## Description
Do you encounter complex dictionaries or JSON files? It is difficult to extract the desired value from them. However, if you use this you can easily retrieve it.

## Usage
* Normal
```
In [1]: d = {"a": 1, "b": [{"c": 3}, {"d": [{"e": "Goal!!", "f": 4}]}]}

In [2]: d["b"][1]["d"][0]["e"]
Out[2]: 'Goal!!'
```

* dicdig
```
In [1]: from dicdig import dicdig

In [2]: d = {"a": 1, "b": [{"c": 3}, {"d": [{"e": "Goal!!", "f": 4}]}]}

In [3]: dicdig(d,"e")
Out[3]: 'Goal!!'
```
