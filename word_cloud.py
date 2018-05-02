from PIL import Image
import numpy as np
import wordcloud

sps_stopwords = set(wordcloud.STOPWORDS)
sps_stopwords.update(["St", "Paul", "SPS", "student", "school", "students"])

crest = np.array(Image.open("sps_crest.jpg"))
crest_color_func = wordcloud.ImageColorGenerator(crest)

handbook = open("./spshandbook.txt").read()

handbook_wc = wordcloud.WordCloud(stopwords=sps_stopwords).generate(handbook)
handbook_wc.to_image().save("spshandbook_cloud.png")

handbook_crest_wc = wordcloud.WordCloud(stopwords=sps_stopwords, mask=crest,
                                  color_func=crest_color_func,
                                  background_color="white").generate(handbook)
handbook_crest_wc.to_image().save("handbook_cloud_crest.png")
