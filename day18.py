def OpenBox():
    global count
    print("open box!")
    count = count -1
    if count == 0:
        print("put on the ring, return")
        return
    OpenBox()
    print("packing box")

count = 10
OpenBox()