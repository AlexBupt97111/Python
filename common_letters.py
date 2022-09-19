def common():
    sentence_1 = set(input("Input first sentence: "))
    sentence_2 = set(input("Input second sentence: "))
    #print(sentence_1, sentence_2)
    print(sentence_1.intersection(sentence_2))

common()
