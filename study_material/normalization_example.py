# 영어에서의 어간 추출(Stemming)과 표제어 추출(Lemmatization) 예

import nltk

# 초기 1회만.
# nltk.download('wordnet') # wordnet 패키지 다운로드

from nltk.stem import PorterStemmer, WordNetLemmatizer

# 영어의 대표적인 어간 추출 알고리즘.
stemmer = PorterStemmer() # 규칙 기반으로 빠르게 처리할 수 있음. 그러나 결과가 실제 단어가 아닐 수 있고, 다른 단어를 잘못 묶는 과도한 어간 추출이 생길 수 있음.

# 형태소 분석과 사전 정보를 활용해 단어의 실제 기본형인 표제어를 추출.
lemmatizer = WordNetLemmatizer() # 언어학적으로 정확한 결과를 제공함. 그러나 품사 정보와 사전 DB가 필요해 계산 비용이 상대적으로 높음.

print("품사 지정 전)")
words = {"studies": "v", "running": "v", "better": "a"}
for word in words.keys():
    print(f"{word} -> 어간추출:{stemmer.stem(word)}, 표제어추출:{lemmatizer.lemmatize(word)}") # 품사를 지정하지 않음. better->better

print("품사 지정 후)")
for word, grammar in words.items():
    print(f"{word} -> 어간추출:{stemmer.stem(word)}, 표제어추출:{lemmatizer.lemmatize(word, pos=grammar)}") # 품사를 동사(verb), 형용사(adjective)로 지정함. better->good

