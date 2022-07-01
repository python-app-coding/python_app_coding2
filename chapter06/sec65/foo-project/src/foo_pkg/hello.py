# coding = utf8


def hello(msg='World'):
    """
    show a welcome words

    Args:
        msg(str): object to welcome

    Return:
        None

    Output:
        Hello, msg!

    >>> hello()
    Hello, World!
    """
    print("Hello, " + msg + "!")


if __name__ == '__main__':
    hello()
