dict=[{'name': 'affirm', 'confidence': 0.9448149204254}, 
           {'name': 'affirm', 'confidence': 0.944814920425415},
           {'name': 'inform', 'confidence': 0.9842240810394287}, 
           {'name': 'inform', 'confidence': 0.9842240810394287}]
c = []
for i in range(0, len(dict)):
    if dict[i] not in dict[i+1:]:
        c.append(dict[i])
print(c)
