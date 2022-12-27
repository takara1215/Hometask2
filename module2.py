import shutil
import os
 

base_path = 'C:/Users/Pulkit/GFG_Articles/root'
 

dir_list = ['test2', 'test4', 'test5', 'does_not_exist']
 

dest = os.path.join(base_path, 'dest')
 
print("Before moving directories:")
print(os.listdir(base_path))
 

for dir_ in dir_list:
 
    
    source = os.path.join(base_path, dir_)
 
  
    if os.path.isdir(source):
 
        shutil.move(source, dest)
 
print("After moving directories:")
print(os.listdir(base_path))