try:
  data=open("sketchs.txt");
  man=[];
  woman=[];
  mandata=open("man.txt",'w');
  womandata=open("woman.txt",'w');
  for each_item in data:
    try:
      (role,words)=each_item.split(":");
      if(role=="man"):
        man.append(words)
      else:
        woman.append(words);
      print(words);
    except:
      print("Something wrong in file");
  data.close();
  mandata.write(str(man));
  womandata.write(str(woman));
  #print(man,file=mandata);
  #print(woman,file=womandata);
  #mandata.write(man);
  #womandata.write(woman);
except IOError as  error:
  print("File donesn't existed"+str(error))
finally:
  if 'mandata' in locals():
    mandata.close();
  if 'womandata' in locals():
    womandata.close();
  print("this code must execute");
