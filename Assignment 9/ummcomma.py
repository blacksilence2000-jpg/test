def avg_score_from_file(file_path):
    total = 0.0
    count = 0
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(',')
            if len(parts) != 2:
                continue
            name = parts[0].strip()
            score_str = parts[1].strip()
            try:
                score = float(score_str)
            except ValueError:
                continue
            total += score
            count += 1
    if count == 0:
        return 0.0
    return total / count

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print('usage: python ummcomma.py <file>')
        sys.exit(1)
    fname = sys.argv[1]
    try:
        avg = avg_score_from_file(fname)
        print('điểm trung bình :', avg)#nah im done ưith writing in vietnamese, my laptop unik is broke now.I will back to english soon :)))
    except FileNotFoundError:
        print('không tìm thấy:', fname)
        sys.exit(2)
    except Exception as e:
        print('lỗi rồi bro:', e)
        sys.exit(3)
