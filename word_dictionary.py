# Python project for finding meaning of any word 

from PyDictionary import PyDictionary

# Initialize the PyDictionary object
dictionary = PyDictionary()

def main():
    while True:
        # Prompt the user to enter a word or 'q' to quit
        word = input("Enter word to get its meaning or 'q' for quit: ").strip().lower()
        
        if word == "q":
            # Check if the user wants to quit
            print("(: Exiting the dictionary, Goodbye :)")
            break
        else:
            try:
                # Get the meaning of the word
                meaning = dictionary.meaning(word)
    
                if meaning:
                    # If meaning is found, print the meanings
                    for part_of_speech, definitions in meaning.items():
                        print(f"{part_of_speech.capitalize()}:")
                        for definition in definitions:
                            print(f"- {definition}")
                else:
                    # If no meaning is found, inform the user
                    print(f"No meaning found for: {word} \n")

            except Exception as e:
                print("Error:", e)

# Run the main function if the script is executed directly
if __name__ == "__main__":    
    main()