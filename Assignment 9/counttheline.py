def count_lines(file_path):
    cnt = 0
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip() != '':
                cnt = cnt + 1
    return cnt

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print('usage: python counttheline.py <file>')
        sys.exit(1)
    fname = sys.argv[1]
    try:
        c = count_lines(fname)
        print('số lượng dòng =', c)
    except FileNotFoundError:
        print('không tìm thấy:', fname)
        sys.exit(2)
    except Exception as e:
        print('có lỗi:', e)
        sys.exit(3)
