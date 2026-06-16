def reverse_words(sentence):
    return " ".join(sentence.split()[::-1])

if __name__ == "__main__":
    user_input = input("Enter a sentence: ")
    print(reverse_words(user_input))
