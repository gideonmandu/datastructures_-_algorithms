from rich import print


def fn_three():
    print("three")


def fn_two():
    fn_three()
    print("two")


def fn_one():
    fn_two()
    print("one")


fn_one()
