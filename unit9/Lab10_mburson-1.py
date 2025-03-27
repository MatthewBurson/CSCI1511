import string

def word_frequency(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()

        # Remove punctuation and convert to lowercase
        text = text.translate(str.maketrans('', '', string.punctuation)).lower()

        # Split the text into words
        words = text.split()

        # Count word frequencies
        word_counts = {}
        for word in words:
            if word: # Handle potential empty strings from extra spaces.
                word_counts[word] = word_counts.get(word, 0) + 1

        # Sort words alphabetically and print counts
        for word, count in sorted(word_counts.items()):
            print(f"{word:<20} {count}")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def get_user_choice():
    while True:
        choice = input("Do you want to enter another file? (y/n): ").lower()
        if choice in ["y", "n"]:
            return choice == "y"
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    while True:
        filename = input("Enter the filename: ")
        word_frequency(filename)
        if not get_user_choice():
                break