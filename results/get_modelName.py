import os
for dir_name in os.listdir("./"):
    if(os.path.isdir(dir_name)):
        print(f"    \"{dir_name}\",")