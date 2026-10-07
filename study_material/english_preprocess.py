# 영어 기준 전반적인 전처리 파이프라인

import re

import nltk
# 초기 1회
# nltk.download('stopwords')

from nltk.tokenize import word_tokenize # 단어 토큰화
from nltk.corpus import stopwords # 불용어들의 목록을 미리 모아둔 말뭉치 데이터

def preprocess_text(text):
    # 1단계: 정제 - HTML 태그, URL 제거
    text = re.sub(r'<[^>]+>', '', text) # HTML 태그(<a href="./index.html"> 등) 제거
    text = re.sub(r'https?://\S+|www\.\S+', '', text) # URL 제거

    # 2단계: 정규화 - 소문자 통일
    text = text.lower()

    # 3단계: 특수문자 제거
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # 4단계: (단어)토큰화
    tokens = word_tokenize(text)

    # 5단계: 불용어 제거
    stop_words = set(stopwords.words('english')) # 영어 불용어 목록 set 담음
    tokens = [t for t in tokens if t not in stop_words] # 불용어 아닌 것들만 담음

    return tokens

sample = "The Movie was AMAZING!! Check it out at http://example.com, the best site online. <br>"
result = preprocess_text(sample)
print(result)
