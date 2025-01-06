def add_before_ui_after_ui(func):
    def wrapper():
        print("Before running the UI")
        print("Strat the browser")
        func()
        print("After running the UI")
    return wrapper()


@add_before_ui_after_ui
def Test_UI():
    print(">>>>I WILL TEST THE UI")