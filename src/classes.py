class Cookie:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color


if __name__ == "__main__":
    cookie1 = Cookie('green')
    cookie2 = Cookie('yellow')

    print(cookie1.get_color())
    print(cookie2.get_color())
    cookie1.set_color('brown')
    print(cookie1.get_color())
    print(cookie2.get_color())
