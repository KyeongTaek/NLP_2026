# 영어에서의 문장 토큰화와 단어 토큰화

import nltk

# 초기 1회만
# nltk.download('punkt_tab') # 문장 토큰화 시 사용하는 비지도 학습 기반 모델. 'Mr. Smith'의 마침표는 문장의 끝이 아님을 구

from nltk.tokenize import sent_tokenize, word_tokenize

text = "I love NLP. Don't you agree? It's a fascinating field!"
# text = "Don't you agree? Dr. Kim likes 3.14 very much."

sentences = sent_tokenize(text) # 문장 토큰화
print(sentences)

words = word_tokenize(sentences[1]) # 단어 토큰화
print(words)
