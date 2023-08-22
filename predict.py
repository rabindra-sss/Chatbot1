model.load("model.tflearn")

def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]
    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1

    return np.array(bag)


def chat():
    print("The bot is ready to talk!!(Type 'quit' to exit)")
    while True:
        inp = input("\nYou: ")
        if inp.lower() == 'quit':
            break

    #Porbability of correct response 
        results = model.predict([bag_of_words(inp, words)])

    # Picking the greatest number from probability
        results_index = np.argmax(results)

        tag = labels[results_index]


        for tg in data['intents']:

            if tg['tag'] == tag:
                responses = tg['responses']
            print("Bot:" + random.choice(responses))


chat()
