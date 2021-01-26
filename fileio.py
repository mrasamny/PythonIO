# This module demonstrates file IO capabilities
# in Python.

def write_to_file():
    secret_file = open("notSoSecret.txt", "w")
    secret_file.write("My not so secret message\n")
    secret_file.write("------------------------\n")
    secret_file.write("Hello, world!\n")
    secret_file.close()


def read_from_file():
    secret_file = open("notSoSecret.txt", "r")
    while True:
        line = secret_file.readline()
        if len(line) == 0:
            break
        # can process line in some way
        print(line, end="")
    secret_file.close()


def read_from_file2():
    secret_file = open("notSoSecret.txt", "r")
    for line in secret_file:
        print(line, end="")
    secret_file.close()


def copy_file(source, destination):
    f = open(source, "rb")
    g = open(destination, "wb")
    while True:
        buf = f.read(1024)
        if len(buf) == 0:
            break
        g.write(buf)
    f.close()
    g.close()
