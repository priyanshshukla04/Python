def searcher():
    import time
    time.sleep(3)
    book = "This is priyansh shukla writing this code tutorials"
    print("Time consuming task running now.....")

    while True:
        value = (yield)
        if value in book:
            print("Word in book")
        else:
            print("Not in book")

search = searcher()
print("search started")
next(search)
print("Next method run")
search.send("this")
search.send("shukla")
input("press any key")
search.send("trgt")
input("press any key")
search.send("thi si")
input("press any key")
search.send("joker")
input("press any key")
search.send("like this tutorial")
search.close()