import nitk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load model
lemmatizer = WordNetLemmatizer()
intents = json. loads (open('intents.json').read())
words= pickle.load(open(words.pk17, nb:)) classes = pickle.load(open('classes.pk1', 'rb'))
model = load model('chatbot model.model')
def clean up sentence (sentence):
   sentence_words = nltk.word_tokenize(sentence)
   sentence words = [lemmatizer.lemmatize (word) for word in sentence_words]
   return sentence_words
