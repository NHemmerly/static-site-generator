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
    for file in os.listdir(path):
        if os.path.isdir(f"{path}/{os.listdir(path)[0]}"):
            shutil.rmtree(f"{path}/{os.listdir(path)[0]}")
            continue
        os.remove(os.path.join(path, file))

def copy_dir(src, dst):
    if not os.path.isdir(src):
        print(f"Copying {src} to {dst}")
        shutil.copy(src, dst)
        return True
    for file in os.listdir(src):
        new_file = os.path.join(src,file)
        if os.path.isdir(new_file):
            new_dst = os.path.join(dst, file)
            os.mkdir(new_dst)
            print(f"Copying {new_file} to {new_dst}")
            copy_dir(new_file, new_dst)
            continue
        print(f"Copying {new_file} to {dst}")
        shutil.copy(new_file, dst)

def static_to_public():
    check_path()
    path_empty("public")
    copy_dir("static", "public")