import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

#importing Dataset
df=pd.read_csv("Restaurant_Reviews.tsv", sep="    ")

#creating the text variable
text=" ".join(cat for cat in df.Review)

#Generate word cloud
word_cloud=WordCloud(
    width=3000,
    height=2000,
    random_state=1,
    background_color="salmon",
    colormap="Pastel1",
    collocations=False,
    stopwords=STOPWORDS,
).generate(text)

#Display the generated word cloud
plt.imshow(word_cloud)
plt.axis("off")
plt.show()
