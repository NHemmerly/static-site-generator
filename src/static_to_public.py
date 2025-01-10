import os
import shutil

def check_path():
    public = os.path.exists("public/")
    static = os.path.exists("static/")
    if public and static:
        print("public and static directories exist")
        return True
    if not public:
        print("Public directory not detected, creating...")
        os.mkdir("public/")
    if not static:
        print("Static directory not detected, creating...")
        os.mkdir("static/")

def path_empty(path):
    if not os.listdir("public"):
        print(f"{path} empty")
        return True
    if os.listdir(f"{path}/{os.listdir(path)[0]}"):
        shutil.rmtree(f"{path}/{os.listdir(path)[0]}")
        return True
    print(f"Removing {path}/{os.listdir(path)[0]}")
    os.remove(f"{path}/{os.listdir(path)[0]}")
    path_empty(path)

def copy_dir(src, dst):
    src_dir = os.listdir(src)
    if len(os.listdir(src)) == 0:
        return True
    if os.path.isdir(f"{src}/{src_dir[0]}"):
        os.mkdir(f"{dst}/{src_dir[0]}")
        dst = f"{dst}/{src_dir[0]}"
        copy_dir(f"{src}/{src_dir[0]}", dst)
    shutil.copy(f"{src}/{src_dir[0]}", dst)
    # You stopped here: src is a string doofus
    #copy_dir(f"{src}/{os.listdir(src)[1:][0]}", dst)

def static_to_public():
    check_path()
    path_empty("public")
    copy_dir("static", "public")