def outer (name):
    def inner ():
        print("Hello", name)

    return inner

message = outer ("Subbu")
message()