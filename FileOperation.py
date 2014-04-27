data=open('sketch.txt')
#print(the_file.readline());
manualscript={};
for each_item in data:
  if(each_item.find(":")>=0):
    print(each_item.find(":"));
    (role,line_spoken)=each_item.split(":");
    manualscript[role]=line_spoken;
    print(each_item);
print(manualscript)
data.seek(0);
data.close();
