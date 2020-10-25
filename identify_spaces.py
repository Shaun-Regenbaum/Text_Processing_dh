import numpy as np
import json


file = open("data.txt", "r")
data = json.load(file)
print(data[1])

