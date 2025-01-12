from static_to_public import static_to_public
from generate_page import generate_pages_recursive

def main():
    print("Hello SSG")
    static_to_public()
    generate_pages_recursive("content", "template.html", "public/")
if __name__ == "__main__":
    main()