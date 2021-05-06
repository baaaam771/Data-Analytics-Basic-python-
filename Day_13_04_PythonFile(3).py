# Day_13_04_PythonFile.py


def read_file_1():
    # f = open('./data/poem.txt')
    # f = open('data\\poem.txt')        # 윈도우 전용
    f = open('data/poem.txt', 'r', encoding='utf-8')     # euc-kr

    lines = f.readlines()
    print(lines)

    for line in lines:
        # print(line, end='')
        line = line.strip()
        print(line)

    f.close()

    # 공백: space, tab, enter
    # strip: 문자열 양쪽의 모든 공백 제거
    s = '\n   \n   \n\t  Good morning!!  \t  \t   \t\n\n'
    print('[{}]'.format(s))
    print('[{}]'.format(s.strip()))


def read_file_2():
    f = open('data/poem.txt', 'r', encoding='utf-8')     # euc-kr

    while True:                 # 무한 루프
        line = f.readline()

        # 참: 거짓이 아닌 모든 값
        # 거짓: 0, 0.0, False, None, '', [], {}
        # if len(line) == 0:
        if not line:
            break

        line = line.strip()
        print(line)

    f.close()


def read_file_3():
    f = open('data/poem.txt', 'r', encoding='utf-8')     # euc-kr

    for line in f:
        print(line.strip())

    f.close()


def read_file_4():
    with open('data/poem.txt', 'r', encoding='utf-8') as f:
        for line in f:
            print(line.strip())

        f.close()


# read_file_1()
# read_file_2()
# read_file_3()
read_file_4()
