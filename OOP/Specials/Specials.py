class Movie:
    def __init__(self, name, director, duration):
        self.name = name
        self.director = director
        self.duration = duration

    def __str__(self):
        return f"{self.name} movie generated by {self.director}. The movie is {self.duration} minutes"


    def __len__(self):
        return self.duration

movie1 = Movie("Test Movie", "Hasan Kacar", 150)
print(movie1)
print(len(movie1))