# Create a program that takes a sentence as input and counts the number of words in it

#method1

def count_words(senetence):
    words = senetence.split()
    return len(words)
user_input = input("Enter you sentence here ")
result = count_words(user_input)
print(f"your {user_input} sentence has {result} these many words")


# method2
def each_words(sentence):
    words = sentence.split()
    print("lenght of words is", len(words))
    print("the length of letters in each word is")

    for word in words:
        print(f" '{word}': {len(word)} characters ")

user_input = input("Type your sentence: ")
each_words(user_input)