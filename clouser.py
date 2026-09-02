def outer (name):
    def inner ():
        print("Hello", name)

    return inner

message = outer ("Hello Subbu")
message()