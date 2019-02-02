def cookbook_read():
  with open('cookbook.txt') as file:
    lines = file.readlines()
  cook_book = {}
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
  return cook_book

# print('\n', 'Задание_1:', '\n', '\n', cookbook_read(), '\n', sep = '')

def get_shop_list_by_dishes(cook_book, person_count):
  dishes = list(cook_book.keys())
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

print('Задание_2:', '\n', '\n', get_shop_list_by_dishes(cookbook_read(), int(input('Введите кол-во персон: '))), sep='')
