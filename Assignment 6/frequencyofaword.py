import re
from collections import Counter
def wordfrequency(text):
    words = re.findall(r'\b\w+\b', text.lower())
    total_words = len(words)

    if total_words == 0:
        print("No words found in the text.")
        return

    freq = Counter(words)
    top_5 = freq.mostcommon(5)
    top_5_dict = dict(top_5)
    sum_top_5 = sum(count for word, count in top_5)
    proportion = (sum_top_5 / total_words) * 100

    print(f"top 5: {top_5_dict}")
    print(f"total: {total_words}")
    print(f"proportion: {sum_top_5} / {total_words} = {proportion:.2f}%")
#example (i can put in the input in the main function)
if __name__ == "__main__":
    text = "The world is mine, the world is out there, the world is beautiful."
    wordfrequency(text)