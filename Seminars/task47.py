# Задача №47.

transformation = lambda x: x
values = [1, 23, 42, 'asdfg']
transformed_values = list(map(transformation, values))
# transformed_values = list(map(lambda x: x, values))
if values == transformed_values:
 print('ok')
else:
 print('fail')