import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfTransformer,CountVectorizer

def get_preds(commentaire):
    loaded_model_lr = pickle.load(open("models/avis_amazon_lr.model", 'rb'))
    loaded_model_svc = pickle.load(open("models/avis_amazon_svc.model", 'rb'))
    loaded_model_sgd = pickle.load(open("models/avis_amazon_sgd.model", 'rb'))
    transformer = TfidfTransformer()
    loaded_vec = CountVectorizer(decode_error="replace",vocabulary = pickle.load(open("models/base.pkl", "rb")))
    tfidf = transformer.fit_transform(loaded_vec.fit_transform(np.array([commentaire])))
    d = {'mauvais':"Commentaire negatif", 'bon' : "Commentaire positif"}
    results = {"LogisticRegression" : d[loaded_model_lr.predict(tfidf.toarray())[0]],
               "LinearSVC" : d[loaded_model_svc.predict(tfidf.toarray())[0]],
               "SGDClassifier" : d[loaded_model_sgd.predict(tfidf.toarray())[0]]}
    return results