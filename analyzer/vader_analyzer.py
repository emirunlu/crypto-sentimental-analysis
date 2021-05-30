from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from analyzer.data import *

def analyze_sentences(sents):
    analyzer = SentimentIntensityAnalyzer()
    analyzer.lexicon.update(crypto_words)
    compound_sum = 0
    for sentence in sents:
        vs = analyzer.polarity_scores(sentence)
        compound = vs["compound"]
        pos = vs["pos"]
        neu = vs["neu"]
        neg = vs["neg"]
        compound_sum += compound
        # print("{:-<65} {}".format(sentence, str(vs)))
    average_score = compound_sum / len(sents)
    # print("Average Compound Score: ", average_score)
    return average_score