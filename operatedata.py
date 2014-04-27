with open("sarah.txt") as saf:
  data=saf.readline();
  data=data.replace('-',".").replace(":",".");
sarah=data.strip().split(',');

with open("mikey.txt") as mkf:
  data=mkf.readline();
  data=data.replace('-',".").replace(":",".");
mikey=data.strip().split(',');

with open("james.txt") as jaf:
  data=jaf.readline();
  data=data.replace('-',".").replace(":",".");
james=data.strip().split(',');

with open("julie.txt") as juf:
  data=juf.readline();
  data=data.replace('-',".").replace(":",".");
julie=data.strip().split(',');

'''
print(sarah);
print(julie);
print(james);
print(mikey);'''

print(sorted(sarah));
print(sorted(julie));
print(sorted(james));
print(sorted(mikey));

def getdata(filename):
  with open(filename) as fln:
    data=fln.readline();
    data=data.replace('-',".").replace(":",".");
  datalist=data.strip().split(',');
  return datalist;

def dedup(data_list):
  datamap={};
  for each_item in data_list:
    datamap[each_item]=1;
  #print(datamap);
  return datamap.keys();

def sort_score(data_list):
  data_list=dedup(sarah);
  data_list.sort();
  return data_list;

sarahnew=getdata("sarah.txt");
sarahnew=sort_score(sarahnew);
print('Here is new list'+str(sarahnew));

sarah=sort_score(sarah);
print(sarah);

sarah=sort_score(sarah);
print(sarah[0:3])
print(sort_score(julie));
print(sort_score(james));
print(sort_score(mikey));



'''
sarah.sort();
print(sarah);
print(julie);
print(james);
'''
'''
print(sarah.sort());
print(julie.sort());
print(james.sort());
print(mikey.sort());
'''
