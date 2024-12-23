from textnode import TextNode, TextType

def main():
    print("Hello SSG")
    first_node = TextNode("This is my first node", TextType.BOLD, "http://localhost:8888")
    print(first_node)

if __name__ == "__main__":
    main()