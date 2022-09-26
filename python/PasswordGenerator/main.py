import string
import random

class PasswordGenerator():
    def __init__(self) -> None:
        passwordLength = 0
    def generatePassword(self) -> str:
        # allow only digits, numbers, and special symbols
        allowedCharacters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
        password = []

        random.shuffle(allowedCharacters)

        # randonly add the allowed shuffled characters to the password array
        for x in range(self.passwordLength):
            password.append(random.choice(allowedCharacters))
        # shuffle one last time before returning
        random.shuffle(password)

        # returned joined array back
        password = "".join(password)
        return password;

    def passwordHelper(self):
        length = 0
        length = input("Enter password length requirement: " )

        if length.isnumeric():
            self.passwordLength = int(length)
        else:
            while length.isnumeric() == False:
                print("Bad number entered. Try again")
                length = input()


def main() -> None:
    myPassword = PasswordGenerator()
    myPassword.passwordHelper()
    print(myPassword.generatePassword())


if __name__ == "__main__":
    main();