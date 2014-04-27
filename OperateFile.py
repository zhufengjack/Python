try:
  data=open('sketch.txt')
  #print(the_file.readline());
  manualscript={};
  for each_item in data:
    try:
      print(each_item.find(":"));
      (role,line_spoken)=each_item.split(":");
      manualscript[role]=line_spoken;
      print(each_item);
    except:
      print("Something wrong");
      pass;
  print(manualscript)
  data.close();
except IOError:
  print("File donesn't existed")
