#encoding=utf-8
from gensim.models import word2vec
if __name__ == '__main__':
    sentences=word2vec.Text8Corpus(u'data/words.txt')
    model=word2vec.Word2Vec(sentences, size=50)

    for i in model.most_similar(u"北京"):
        print(i[0],i[1])
