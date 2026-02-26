def keep_evens(nums):
    return [n for n in nums if n % 2 == 0]

def keep_odds(nums):
    return [n for n in nums if n % 2 != 0]

def main():
    original = [1, 2, 3, 4, 5, 6, 7, 8, 9] #or some whatever list you want to test
    evens = keep_evens(original)
    odds = keep_odds(original)

    print("original list:", original)
    print("even:", evens)
    print("odd:", odds)

if __name__ == "__main__":
    main()
