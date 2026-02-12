# %% Porter stemming in action

import nltk
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()
words = ["compute", "computers", "computed", "computing"]
for w in words:
    print(f"{w} -> {stemmer.stem(w)}")


# %% Tokenize
nltk.download("punkt")
sentence = """
When the Boogeyman goes to sleep every night,
he checks his closet for Chuck Norris.
"""

tokens = nltk.word_tokenize(sentence)
print(tokens)


# %% Remove stopwords and punctuation
nltk.download("stopwords")

from nltk.corpus import stopwords
from string import punctuation

stop_words = stopwords.words("english")
print(
    [
        t
        for t in tokens
        if t.lower() not in stop_words and t not in punctuation
    ]
)

# %%
stopwords.words("spanish")


# %% Part-of-speech Tagging
nltk.download("averaged_perceptron_tagger")
tagged = nltk.pos_tag(tokens)
print(tagged)


# %% Identify named entities
nltk.download("maxent_ne_chunker")
nltk.download("words")
entities = nltk.chunk.ne_chunk(tagged)
print(entities)

# %% spacy Tokenization
import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

for token in doc:
    print(token.text)


# %% Part-of-speech tags and dependencies
for token in doc:
    print(
        token.text,
        token.lemma_,
        token.pos_,
        token.tag_,
        token.dep_,
        token.shape_,
        token.is_alpha,
        token.is_stop,
    )


# %% Named Entities
for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)


# %% Note: Use the interupt button to stop
spacy.displacy.serve(doc, style="dep")


# %% Note: Use the interupt button to stop
spacy.displacy.serve(doc, style="ent")


# %% Sentence Segmentation
doc = nlp(
    """This is a sentence. This is another sentence. Apple is looking at buying U.K. startup for $1 billion."""
)
for sent in doc.sents:
    print(sent.text)


# %% Word Vectors
for sent in doc.sents:
    for token in sent:
        print(token.text, token.is_stop)
    print()


# %%
nlp = spacy.load("en_core_web_md")
tokens = nlp("dog cat banana afskfsd")
for token in tokens:
    print(token.text, token.has_vector, token.vector_norm, token.is_oov)


# %% Semantic Similarity
tokens = nlp("dog cat banana")
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))


# %% gensim word2vec
from gensim.models import Word2Vec

sentences = [["cat", "say", "meow"], ["dog", "say", "woof"]]
model = Word2Vec(sentences, min_count=1)
print(model.wv.similarity("cat", "dog"))
print(model.wv.similarity("meow", "woof"))


# %% LDA
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.datasets import fetch_20newsgroups

data, _ = fetch_20newsgroups(
    shuffle=True,
    random_state=1,
    remove=("headers", "footers", "quotes"),
    return_X_y=True,
)
tf_vectorizer = CountVectorizer(
    max_df=0.95, min_df=2, max_features=1000, stop_words="english"
)
tf = tf_vectorizer.fit_transform(data)
tf


# %%
lda = LatentDirichletAllocation(
    n_components=10,
    max_iter=5,
    learning_method="online",
    learning_offset=50,
    random_state=0,
)
lda.fit(tf)


# %% Show top keywords for the topics
def show_topic(model, feature_names, top):
    for index, distribution in enumerate(model.components_):
        sorted_word_indices = distribution.argsort()[::-1][:top]
        print(f"Topic {index}:")
        feats = [feature_names[i] for i in sorted_word_indices]
        print(" ".join(feats))


tf_feature_names = tf_vectorizer.get_feature_names_out()
show_topic(lda, tf_feature_names, 10)

# %% Text Classification
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

train = fetch_20newsgroups(subset="train")

# %%
tfidf_vect = TfidfVectorizer()
train_x = tfidf_vect.fit_transform(train.data)
train_y = train.target

# %%
clf = MultinomialNB()
clf.fit(train_x, train_y)
train_pred = clf.predict(train_x)
print(f"train acc: {accuracy_score(train_y, train_pred)}")

test = fetch_20newsgroups(subset="test")
test_x = tfidf_vect.transform(test.data)
test_y = test.target
test_pred = clf.predict(test_x)
print(f"test acc: {accuracy_score(test_y, test_pred)}")


# %% tfidf
sents = [
    "The car is driven on the road.",
    "The truck is driven on the highway.",
]

from sklearn.feature_extraction.text import (
    TfidfVectorizer,
    CountVectorizer,
)

tf_vect = CountVectorizer()
for row in tf_vect.fit_transform(sents).toarray():
    print(row)
print(tf_vect.get_feature_names_out())

print("-" * 80)

tfidf_vect = TfidfVectorizer()
for row in tfidf_vect.fit_transform(sents).toarray():
    print(row)
print(tfidf_vect.get_feature_names_out())


# %% Custom Tokenizer
from sklearn.feature_extraction.text import TfidfVectorizer
import spacy

nlp = spacy.load("en_core_web_sm")
custom_tfidf_vect = TfidfVectorizer(
    tokenizer=lambda text: [token.text for token in nlp(text)]
)
print(custom_tfidf_vect.fit_transform(sents).toarray())
print(custom_tfidf_vect.get_feature_names_out())


# %%
from sklearn.feature_extraction.text import TfidfVectorizer
import spacy

nlp = spacy.load("en_core_web_sm")


def spacy_tokenize(docuemnt):
    return [token.text for token in nlp(docuemnt)]


custom_tfidf_vect = TfidfVectorizer(tokenizer=spacy_tokenize)
print(custom_tfidf_vect.fit_transform(sents).toarray())
print(custom_tfidf_vect.get_feature_names_out())


# %% Pipeline
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

text_clf = Pipeline(
    [
        ("tfidf", TfidfVectorizer()),
        ("clf", MultinomialNB()),
    ]
)
train = fetch_20newsgroups(subset="train")
test = fetch_20newsgroups(subset="test")
text_clf.fit(train.data, train.target)
train_pred = text_clf.predict(train.data)
test_pred = text_clf.predict(test.data)
print(f"train acc: {accuracy_score(train.target, train_pred)}")
print(f"test acc: {accuracy_score(test.target, test_pred)}")


# %% Advanced Pipeline
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.decomposition import PCA, TruncatedSVD
from sklearn.preprocessing import FunctionTransformer
from sklearn.metrics import accuracy_score

dense = FunctionTransformer(lambda x: x.toarray())
union = FeatureUnion(
    [
        ("pca", PCA(n_components=50)),
        ("svd", TruncatedSVD(n_components=150)),
    ]
)
text_clf = Pipeline(
    [
        ("tfidf", TfidfVectorizer(max_features=500)),
        ("dense", dense),
        ("union", union),
        ("clf", LogisticRegression()),
    ]
)
train = fetch_20newsgroups(subset="train")
test = fetch_20newsgroups(subset="test")
text_clf.fit(train.data, train.target)
train_pred = text_clf.predict(train.data)
test_pred = text_clf.predict(test.data)
print(f"train acc: {accuracy_score(train.target, train_pred)}")
print(f"test acc: {accuracy_score(test.target, test_pred)}")

# %%
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import spacy

nlp = spacy.load("en_core_web_sm")
custom_tfidf_vect = TfidfVectorizer(
    tokenizer=lambda text: [
        (token.text, token.pos_) for token in nlp(text)
    ]
)

train_x = custom_tfidf_vect.fit_transform(train.data)
train_y = train.target
clf = MultinomialNB()
clf.fit(train_x, train_y)
train_pred = clf.predict(train_x)
print(f"train acc: {accuracy_score(train_y, train_pred)}")
print(len(custom_tfidf_vect.get_feature_names_out()))


# %%
test_pred = clf.predict(custom_tfidf_vect.transform(test.data))
print(f"test acc: {accuracy_score(test.target, test_pred)}")

# %%
