import os

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

def public_empty():
    if not os.listdir("public"):
        print("Public empty")
        return True
    
    


def static_to_public():
    check_path()
    public_empty()