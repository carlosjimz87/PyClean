# # incorrect way: all mandatory args
# def connect(host, user, port, replicate, use_ssl):
#     print(
#         f"Connect to: {user}@host:{port}, replicate={replicate},use_ssl={use_ssl}")


# connect("www.mongo.com", "chars", 5510, False, True)  # this works
# # connect("www.mongo.com", "chars")  # THIS FAILS

# print()


# def connectDefault(host="www.mongo.com", user="chars", port=5510, replicate=False, use_ssl=True):
#     print(
#         f"Connect to: {user}@host:{port}, replicate={replicate},use_ssl={use_ssl}")


# connectDefault()  # this also works


def printpalabras(*palabras: str):
    for p in palabras:
        print(p)


printpalabras("a", "b", "c")
