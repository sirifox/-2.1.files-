cook_book = {}

with open('cookbook.txt') as file:
  lines = file.readlines()

for num, line in enumerate(lines):
  if line == '\n':
    continue
  elif num == 0 or lines[num-1] == '\n':
    ingridients = []
    for ingr in lines[num+2:num+2+int(lines[num+1])]:
      ingr = ingr.split(' | ')
      ingridients.append({'ingridient_name': ingr[0], 'quantity': int(ingr[1]), 'measure': ingr[2].strip()})
    cook_book[line.strip()] = ingridients

del lines

print('\n', 'Задание_1:', '\n', sep = '')
print(cook_book, '\n', sep = '')

def get_shop_list_by_dishes(dishes, person_count):
  ingridients_dict = {}
  for dish in dishes:
    if dish in list(cook_book.keys()):
      for ingr in cook_book[dish]:
        if ingr['ingridient_name'] not in list(ingridients_dict.keys()):
          ingridients_dict[ingr['ingridient_name']] = {'measure': ingr['measure'],
                                                       'quantity': ingr['quantity'] * person_count}
        else:
          ingridients_dict[ingr['ingridient_name']]['quantity'] += ingr['quantity'] * person_count
  return ingridients_dict

print('Задание_2:', '\n', sep = '')
print(get_shop_list_by_dishes(list(cook_book.keys()), 2))
