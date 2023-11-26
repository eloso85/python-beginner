# Class representing individual movies
class Movie:
    # Initializer with attributes: title, genre, and rating
    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating

    # String representation of the Movie object, used when printing the object
    def __str__(self):
        return f"{self.title} ({self.genre}, Rating: {self.rating}/5)"
    # new

# Class representing a user of the system
class User:
    def __init__(self, name):
        self.name = name          # User's name
        self.preferences = []     # List to store user's genre preferences

    # Method to add a genre to the user's preferences
    def add_preference(self, genre):
        if genre not in self.preferences:
            self.preferences.append(genre)

# Class handling the movie recommendation logic
class RecommendationEngine:
    def __init__(self):
        self.movies = []  # List to store all movies added to the system

    # Method to add a movie to the engine's movie list
    def add_movie(self, movie):
        self.movies.append(movie)

    # Method to recommend movies based on user preferences and movie rating
    def recommend(self, user):
        # List comprehension to filter and return movies matching user preferences and with high rating
        return [movie for movie in self.movies if movie.genre in user.preferences and movie.rating >= 4]

# Function to display the main menu options
def display_menu():
    print("\n1. Add Movie")
    print("2. Set User Preferences")
    print("3. Show Recommendations")
    print("4. Exit")

# Main function to run the movie recommendation application
def main():
    engine = RecommendationEngine()  # Create a RecommendationEngine instance
    user = User("User")              # Create a User instance (currently with a fixed name)

    while True:
        display_menu()               # Display the menu options
        choice = input("Enter your choice: ")

        if choice == '1':
            # Option to add a movie
            title = input("Enter movie title: ")
            genre = input("Enter movie genre: ")
            rating = float(input("Enter movie rating (1-5): "))
            engine.add_movie(Movie(title, genre, rating))
            print(f"Added movie {title}.")

        elif choice == '2':
            # Option to set user preferences
            genre = input("Enter a preferred genre: ")
            user.add_preference(genre)
            print(f"Added preference {genre}.")

        elif choice == '3':
            # Option to get movie recommendations
            recommendations = engine.recommend(user)
            print("\nRecommended Movies:")
            for movie in recommendations:
                print(movie)

        elif choice == '4':
            # Option to exit the program
            print("Exiting program.")
            break

        else:
            # Handle invalid menu option entries
            print("Invalid choice. Please try again.")

# Check if this script is the main program and not an imported module
if __name__ == "__main__":
    main()
