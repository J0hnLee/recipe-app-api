import time


def newfunc(argsl, func):
    def newone(args):
        print(argsl)
        print('I am new one', args)
        result = func(args)
        return result
    return newone


@newfunc('huhu')
def oldfunc(args):
    print('I am old one', args)


if __name__ == "__main__":
    oldfunc('haha')
