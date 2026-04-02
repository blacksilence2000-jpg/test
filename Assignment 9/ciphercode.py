def caesar_cipher(file_name, shift, direction):
    with open(file_name, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if direction.lower() == 'left':
        shift = -shift
    result = ''
    for c in content:
        if c.isdigit():
            result += c
        elif c.isupper():
            x = ord(c)
            y = (x - 65 + shift) % 26 + 65
            result += chr(y)
        elif c.islower():
            x = ord(c)
            y = (x - 97 + shift) % 26 + 97
            result += chr(y)
        else:
            result += c

    output_file = file_name.replace('.txt', '_cipher.txt')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(result)
    print('cipher text saved to', output_file)


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 4:
        print('usage: python ciphercode.py <file> <shift> <direction>')
        print('hướng: ')
        sys.exit(1)
    fname = sys.argv[1]
    try:
        sh = int(sys.argv[2])
    except ValueError:
        print('số nha')
        sys.exit(1)
    dir = sys.argv[3]
    if dir.lower() not in ['L', 'R']:
        print('hướng là trái hoặc phải')
        sys.exit(1)
    try:
        caesar_cipher(fname, sh, dir)
    except FileNotFoundError:
        print('không tìm thấy:', fname)
        sys.exit(2)
    except Exception as e:
        print('lỗi rồi bro:', e)
        sys.exit(3)