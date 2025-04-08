#====================================TASK-4====================================
# Content-Based Recommendation System 
def recommend_movies(preferred_genre, movie_database):
    # Create a list of recommended movies based on the user's preferred genre
    recommendations = [
        movie 
        for movie, genre in movie_database.items() 
        if genre.lower() == preferred_genre.lower()
    ]
    
    # The recommendations
    if recommendations:
        return f"We recommend: {', '.join(recommendations)}"
    else:
        return "Sorry, we couldn't find any movies matching your preferred genre."

# Movie database (movie: genre)
movie_database = {
    "Inception": "Science Fiction",
    "The Matrix": "Science Fiction",
    "Interstellar": "Science Fiction",
    "Blade Runner 2049": "Science Fiction",
    "Arrival": "Science Fiction",    
    "The Godfather": "Crime",
    "The Dark Knight": "Crime",
    "Pulp Fiction": "Crime",
    "Scarface": "Crime",
    "The Shawshank Redemption": "Drama",
    "Forrest Gump": "Drama",
    "A Beautiful Mind": "Drama",
    "The Pursuit of Happyness": "Drama",    
    "Parasite": "Thriller",
    "Gone Girl": "Thriller",
    "Se7en": "Thriller",
    "Shutter Island": "Thriller",
    "Toy Story": "Animation",
    "Finding Nemo": "Animation",
    "Inside Out": "Animation",
    "Coco": "Animation",
    "Titanic": "Romance",
    "The Notebook": "Romance",
    "Pride & Prejudice": "Romance",
    "La La Land": "Romance",
    "Avengers: Endgame": "Action",
    "Mad Max: Fury Road": "Action",
    "John Wick": "Action",
    "Gladiator": "Action"
}

# User’s preference
preferred_genre = input("Enter your preferred genre (e.g. Crime, Drama, Action, etc.): ")

# Get movie recommendations
print(recommend_movies(preferred_genre, movie_database))