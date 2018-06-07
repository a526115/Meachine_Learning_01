#-*-coding:utf-8-*-
file_path = r'D:\BO\U32_KAM Bonus Report.txt'

file_object2 = open(file_path,'r')
title_list = ['Object List','Condition List','Hierarchies List','Tables List','Join List','Context List']
skip_line = ['Universe','Page']
output_list = []
header = ''
def key_value(var1):
    global header
    global output_list
    list(output_list).append(header+var1)


try:
  lines = file_object2.readlines()
  print("type(lines)=",type(lines))
  for line in lines:
      if not line.strip():
          pass
      elif line.count(skip_line[0])>0:
          pass
      elif line.count(skip_line[1])>0:
          pass
      elif line.strip() in title_list:
          print('"""""""""""""""""""""""""""""""""')
          header = line
          print()
          print('"""""""""""""""""""""""""""""""""')
      else:
          print("line=", header.strip()+" : " + line.strip())
finally:
    file_object2.close()