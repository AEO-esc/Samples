class Words():
    mySentence = ""
    wordToReplace = ""
    wordReplacement = ""

    def replaceWords():
        str = "The quick brown fox jumped over the lazy dog."
        print("Current sentence: ", str)
        Words.wordToReplace = input("Enter the word to replace:")
        Words.wordReplacement = input("Enter the word replacemt:")
        print(str.replace(Words.wordToReplace, Words.wordReplacement))
    

wordDictionary = {
    "names"
}

def main() -> None:
    Words.replaceWords();

if __name__ == "__main__":
    main();