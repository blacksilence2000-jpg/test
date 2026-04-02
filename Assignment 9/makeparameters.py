def find_keyword_lines(file_path, keyword):
    lines = []
    with open(file_path, 'r', encoding='utf-8') as f:
        i = 0
        for line in f:
            i = i + 1
            if keyword in line:
                lines.append(i)
    return lines

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print('usage: python makeparameters.py <file> <keyword>')
        sys.exit(1)
    fname = sys.argv[1]
    key = sys.argv[2]
    try:
        res = find_keyword_lines(fname, key)
        print('dòng chứa', key, ':', res)
    except FileNotFoundError:
        print('không tìm thấy file:', fname)
        sys.exit(2)
    except Exception as e:
        print('có lôix:', e)
        sys.exit(3)