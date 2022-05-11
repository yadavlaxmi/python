def outer():
    s = 'I love india'
    def inner():
        b = 'Me too'
        print(b)
    inner()
    print(s)
outer()