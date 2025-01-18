import random
import re
from typing import Tuple

allowedLowerCaseCharacters = "abcdefghijklmnopqrstuvwxyz"
allowedUpperCaseCharacters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
allowedNumbers = "1234567890"
allowedSpecialCharacters = "!@#$%^&*()_+-={}[];:<>,./?ß!"
iterations = 1000
keyLength = 64
randomSaltLength = 20


def generatePassword(
    length: int,
    upperCaseCharacters: int,
    numbers: int,
    specialCharacters: int
) -> str:
    firstPasswordDraft = ""
    for _ in range(length):
        randomAllowedCharacterOrNumber = generateRandomAllowedCharacterOrNumber()
        firstPasswordDraft += randomAllowedCharacterOrNumber

    patchedPassword = firstPasswordDraft
    while True:
        isLowerCaseCharactersValid, isNumbersValid, isSpecialCharactersValid, isUpperCaseCharactersValid = checkPasswordPolicy(
            patchedPassword,
            upperCaseCharacters,
            numbers,
            specialCharacters
        )

        if (
            isLowerCaseCharactersValid and
            isNumbersValid and
            isSpecialCharactersValid and
            isUpperCaseCharactersValid
        ):
            break

        if not isLowerCaseCharactersValid:
            patchedPassword = patchCharacters(
                patchedPassword,
                "lower",
                findRequiredLengthToSatisfyPasswordPolicy(
                    patchedPassword, "lower", 1)
            )
        if not isUpperCaseCharactersValid:
            patchedPassword = patchCharacters(
                patchedPassword,
                "upper",
                findRequiredLengthToSatisfyPasswordPolicy(
                    patchedPassword, "upper", upperCaseCharacters)
            )
        if not isNumbersValid:
            patchedPassword = patchCharacters(
                patchedPassword,
                "numbers",
                findRequiredLengthToSatisfyPasswordPolicy(
                    patchedPassword, "numbers", numbers)
            )
        if not isSpecialCharactersValid:
            patchedPassword = patchCharacters(
                patchedPassword,
                "special",
                findRequiredLengthToSatisfyPasswordPolicy(
                    patchedPassword, "special", specialCharacters)
            )

    return patchedPassword


def findRequiredLengthToSatisfyPasswordPolicy(
    password: str,
    characterClass: str,
    requiredLength: int
) -> int:
    if characterClass == "lower":
        matches = re.findall(r'[a-z]', password)
        return abs(len(matches) - requiredLength)
    elif characterClass == "upper":
        matches = re.findall(r'[A-Z]', password)
        return abs(len(matches) - requiredLength)
    elif characterClass == "numbers":
        matches = re.findall(r'\d', password)
        return abs(len(matches) - requiredLength)
    elif characterClass == "special":
        specialCharRegex = r'[!@#$%^&*()_+\-={}\[\];:<>,./?ß]'
        matches = re.findall(specialCharRegex, password)
        return abs(len(matches) - requiredLength)
    else:
        return 0


def patchCharacters(
    password: str,
    characterClass: str,
    requiredLength: int
) -> str:
    if requiredLength <= 0 or requiredLength > len(password):
        return password

    allowedCharacters = getAllowedCharactersBasedOnCharacterClass(
        characterClass)

    patchedPassword = password
    for _ in range(requiredLength):
        randomIndex = random.randint(0, len(password) - 1)
        randomCharacterIndex = random.randint(0, len(allowedCharacters) - 1)
        randomCharacter = allowedCharacters[randomCharacterIndex]

        patchedPassword = (
            patchedPassword[:randomIndex] +
            randomCharacter +
            patchedPassword[randomIndex + 1:]
        )

    return patchedPassword


def getAllowedCharactersBasedOnCharacterClass(characterClass: str) -> str:
    if characterClass == "lower":
        return allowedLowerCaseCharacters
    elif characterClass == "numbers":
        return allowedNumbers
    elif characterClass == "upper":
        return allowedUpperCaseCharacters
    elif characterClass == "special":
        return allowedSpecialCharacters
    else:
        return allowedLowerCaseCharacters


def generateRandomAllowedCharacterOrNumber() -> str:
    allowedCharacters = (
        allowedLowerCaseCharacters +
        allowedUpperCaseCharacters +
        allowedNumbers +
        allowedSpecialCharacters
    )

    index = random.randint(0, len(allowedCharacters) - 1)
    return allowedCharacters[index]


def checkPasswordPolicy(
    password: str,
    upperCaseCharacters: int,
    numbers: int,
    specialCharacters: int
) -> Tuple[bool, bool, bool, bool]:
    isNumbersValid = validatePasswordNumbers(password, numbers)
    isSpecialCharactersValid = validatePasswordSpecialCharacters(
        password, specialCharacters)
    isLowerCaseCharactersValid = validatePasswordLowerCaseCharacters(
        password, 1)
    isUpperCaseCharactersValid = validatePasswordUpperCaseCharacters(
        password, upperCaseCharacters)

    return (
        isNumbersValid,
        isLowerCaseCharactersValid,
        isUpperCaseCharactersValid,
        isSpecialCharactersValid
    )


def validatePasswordUpperCaseCharacters(password: str, length: int) -> bool:
    regex = re.compile(f"([A-Z].*?){{{length},}}")
    return bool(regex.search(password))


def validatePasswordNumbers(password: str, length: int) -> bool:
    regex = re.compile(f"(\\d.*?){{{length},}}")
    return bool(regex.search(password))


def validatePasswordLowerCaseCharacters(password: str, length: int) -> bool:
    regex = re.compile(f"([a-z].*?){{{length},}}")
    return bool(regex.search(password))


def validatePasswordSpecialCharacters(password: str, length: int) -> bool:
    allowedSpecialCharactersInRegixUnderstandableFormat = r"!@#\$%\^&\*\$_\+\-={}\[\];:<>,\./\?ß"
    regex = re.compile(
        f"([{allowedSpecialCharactersInRegixUnderstandableFormat}].*?){{{length},}}")
    return bool(regex.search(password))
