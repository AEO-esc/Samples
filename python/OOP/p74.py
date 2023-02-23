class Movie:
    def __init__(self, title, rating) -> None:
        self._title = title
        self._rating = rating

    @property
    def rating(self):
        print("Calling the getter...")
        return self._rating
    @rating.setter
    def rating(self, new_rating):
        print("Calling the setter...")
        if 1.0 <= new_rating <= 5.0:
            self._rating = new_rating
        else:
            print("Enter a valid rating.")


def main() -> None:
    fav_movie = Movie("Shrek", 9.8)
    print(fav_movie.rating)
    fav_movie.rating = 4.5
    print(fav_movie.rating)

if __name__ == "__main__":
    main()