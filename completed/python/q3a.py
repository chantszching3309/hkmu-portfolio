import os
import sys
from datetime import datetime

files = []
total_size = 0
    
#for loop and list directory
for name in os.listdir("."):
    full_path = os.path.join(".",name)
    
    if os.path.isfile(full_path):
        #get file status
        status = os.stat(full_path)
        
        #storage
        info = {
            "name":name,
            "size": status.st_size,
            "last_modified_time":status.st_mtime,
            #str format time
            "time_format":datetime.fromtimestamp(status.st_mtime).strftime("%a %b %d %H:%M:%S %Y")
            
        }
        
        #add in list
        files.append(info)
        total_size += status.st_size
    
sort_field ="name"
sort_order = "asc"
    
#key
if sort_field == "name":
    #lamda = def , : is return
    key = lambda file : file ["name"].lower()
elif sort_field == "size":
    key = lambda file : file ["size"]
elif sort_field == "last_modified_time":
    key = lambda file : file ["last_modified_time"]
else:
    key = lambda file : file ["name"].lower()

if sort_order == "desc":
    files.sort(key=key, reverse = True )
else:
    files.sort(key=key, reverse = False )
    
#print output
print(f"$ python q3a.py date {sort_order}")
print(f"{'Filename':<40} {'Size':<10} {'Last Modified'}")

for file in files:
    print(f"{file['name']} / {file['size']} / {file['time_format']}")
    
print(f"Total file size: {total_size}")
