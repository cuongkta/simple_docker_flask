import pandas as pandas
from pandas import read_csv, isnull, notnull
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer



def get_dataframe_movies_csv(text):
    movie_cols = ['movie_id', 'title', 'genres']
    movies = pandas.read_csv(text, sep=',', names=movie_cols, encoding='latin-1')
    return movies



# normalize matrix  -- matrix  favorite with tags 
def tfidf_matrix(movies):
    tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 1), min_df=0)
    new_tfidf_matrix = tf.fit_transform(movies['genres'])
    return new_tfidf_matrix



def cosine_sim(matrix):
    new_cosine_sim = linear_kernel(matrix, matrix)
    return new_cosine_sim
