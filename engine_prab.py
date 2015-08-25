from pandas import *
from sentianal import Sentianal
from normalizer import Normalizer
from stpremoval import StpRemoval
import numpy as numpy

import matplotlib.pyplot as plt

sourcefile = "prabowotweet.txt"

#dump the sourcefile into dataframe
fin = open(sourcefile,'r')
tweet = []

for line in fin:
	line = line.strip()
	tweet.append(line)

#store in dataframe
prab_data = DataFrame(tweet)

#rename the column
prab_data.columns = ['tweet']

#score the tweet
score = []

#create normalizer object
norm = Normalizer()

#create Stop word Removal object
st = StpRemoval()

#create sentiment analysis object
s = Sentianal()

for i in range(0,len(prab_data)):
	#normalize
	line = norm.normalize(prab_data['tweet'][i])
	
	#remove stopword
	line = st.removeStp(line)

	#score sentiment
	score.append(s.compute(line))

#join the dataframe
score_data = DataFrame(score)
prab_data = prab_data.join(score_data)
prab_data.columns = ['tweet_processed','score']

#write to csv file
prab_data.to_csv("score_prabowo2.csv")

#try to find common words
