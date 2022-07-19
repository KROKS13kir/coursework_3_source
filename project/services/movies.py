from project.dao.movies import MoviesDao


class MoviesService:
    def __init__(self, movies_dao: MoviesDao):
        self.movie_dao = movies_dao

    def get_one(self, mid):
        return self.movie_dao.get_one(mid)

    def get_all(self, page: str = None, status: str = None):
        check_status = status == 'new'
        if not check_status:
            movies = self.movie_dao.get_all(page, sort=False)
        else:
            movies = self.movie_dao.get_all(page, sort=True)
        return movies

