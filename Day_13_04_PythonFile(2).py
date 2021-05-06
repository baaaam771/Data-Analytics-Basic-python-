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

    f.close()


# read_file_1()
read_file_2()

