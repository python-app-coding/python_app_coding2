# coding = utf8


def demo_open_errors():
    filename = 'temp_open_errors.txt'

    print("raw text:", r'\U00012345 is chars', '\n')

    with open(filename, mode='w', encoding='utf8') as fp:
        fp.write('\U00012345 is chars')

    for err in ['strict', 'ignore', 'replace', 'surrogateescape', 'backslashreplace']:
        print("open read with errors=", err)
        with open(filename, mode='r', errors=err, encoding='ascii') as fp:
            try:
                for line in fp:
                    print(line)
            except UnicodeError as e:
                print('UnicodeError: ', e)
        print("")

    print("open write with errors: ", 'namereplace')
    with open('temp_open_errors_namereplace.txt', mode='w',
              encoding='ascii', errors='namereplace') as fp:
        fp.write('\U00012345 is chars')
    with open('temp_open_errors_namereplace.txt', mode='rb') as fp:
        print(str(fp.read())[2:-1])
    print("")

    print("open write with errors: ", 'xmlcharrefreplace')
    with open('temp_open_errors_xmlcharrefreplace.txt', mode='w',
              encoding='ascii', errors='xmlcharrefreplace') as fp:
        fp.write('\U00012345 is chars')
    with open('temp_open_errors_xmlcharrefreplace.txt', mode='rb') as fp:
        print(str(fp.read())[2:-1])
    print("")


if __name__ == '__main__':
    demo_open_errors()
