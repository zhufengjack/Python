'''
This module is used to loop list and print all item in list inclued nested list.
'''

'''def print_lol(the_list):

  (the_list)->None

  This function is used to loop all items in the_list and print them recursively

  >>>Students=[["Jack","Zhu"],28,Male]
  >>>print_lol(Students)
  Jack
  Zhu
  28
  Male



  for each_item in the_list:
    if(isinstance(each_item,list)):
      print_lol(each_item);
    else:
      print(each_item);
'''


def print_lol(the_list,indent=False,level=0):
  '''
  (List,Integer)-->None

  loop all items in the_list and print all item recursively.

  >>>Student=[28,'Male',["Jack","Zhu"]]
  28
  Male
    Jack
    Zhu
  '''
  for each_item in the_list:
    if(isinstance(each_item,list)):
      print_lol(each_item,indent,level+1);
    else:
      if(indent):
        for tab_stop in range(level):
          print("\t",end='');
      print(each_item);
