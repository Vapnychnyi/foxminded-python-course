def revers_word(word: str) -> str:
    """returns a reversed version of given word"""
    letters_only: list[str] = [char for char in word if char.isalpha()]

    result: list[str] = []

    for char in word:
        if char.isalpha():
            result.append(letters_only.pop())
        else:
            result.append(char)

    return "".join(result)


def revers_text(text: str) -> str:
    """returns a reversed version words in given text"""
    words: list[str] = text.split(" ")

    reversed_words: list[str] = [revers_word(word) for word in words]

    return " ".join(reversed_words)


if __name__ == "__main__":
    cases = [
        ("abcd efgh", "dcba hgfe"),
        ("a1bcd efg!h", "d1cba hgf!e"),
        ("", ""),
    ]

    for text, reversed_text in cases:
        assert revers_text(text) == reversed_text
