import math
def medium(listInput):
  if len(listInput) == 0:
    return "No medium"
  listInput.sort()
  return listInput[math.floor(len(listInput)/2)] if len(listInput) % 2 == 1 else (listInput[math.floor(len(listInput)/2)] + listInput[math.floor(len(listInput)/2) - 1])/2


test = [1, 2, 3, 4,6, 8, 2, 4]
print(medium(test))