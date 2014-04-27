def print_lol(the_list):
  for each_item in the_list:
    if(isinstance(each_item,list)):
      print_lol(each_item);
    else:
      print(each_item);




movies=["The Holy Grails",1975,"Terry Jones & Terry Gillian",91,
          ["Graham Chapman",["Michael Palin","John Cleese","Terry Gilliam","Eric Idle","Terry Jones"]]]
print(movies);

for each_item in movies:
  if(isinstance(each_item,list)):
    for item_of_each_item in each_item:
      if(isinstance(item_of_each_item,list)):
        for item_of_item_of_each_item in item_of_each_item:
          print(item_of_item_of_each_item)
      else:
        print(item_of_each_item)
  else:
    print(each_item)



print('***********This is a new Line************')

print_lol(movies)
