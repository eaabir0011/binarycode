def twttr(txt):
    vowels = "aeiou"
    new_txt = ""
    for char in txt:
        if char.lower() not in vowels:
            new_txt += char
    return new_txt

if __name__ == "__main__":
    text = twttr(input("Input: "))
    print("Output:", text)
