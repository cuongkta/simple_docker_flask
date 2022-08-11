from app.contentbase_filtering.utils import get_dataframe_movies_csv, tfidf_matrix, cosine_sim
import pandas as pd

class ContentBase(object):
    """
        Khởi tại dataframe "movies" với hàm "get_dataframe_movies_csv"
    """
    def __init__(self, movies_csv):
        self.movies = get_dataframe_movies_csv(movies_csv)
        self.tfidf_matrix = None
        self.cosine_sim = None

    def build_model(self):
        """
            Tách các giá trị của genres ở từng bộ phim đang được ngăn cách bởi '|'
        """
        self.movies['genres'] = self.movies['genres'].str.split('|')
        self.movies['genres'] = self.movies['genres'].fillna("").astype('str')
        self.tfidf_matrix = tfidf_matrix(self.movies)
        self.cosine_sim = cosine_sim(self.tfidf_matrix)

    def refresh(self):
        """
             Chuẩn hóa dữ liệu và tính toán lại ma trận
        """
        self.build_model()

    def fit(self):
        self.refresh()


    def genre_recommendations(self, title, top_x):
        titles = self.movies['title']
        indices = pd.Series(self.movies.index, index=self.movies['title'])
        idx = indices[title]
        sim_scores = list(enumerate(self.cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:top_x + 1]
        movie_indices = [i[0] for i in sim_scores]
        return sim_scores, titles.iloc[movie_indices].values