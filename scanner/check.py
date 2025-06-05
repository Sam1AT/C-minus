def normalize(line):
    return line.strip().replace(' ', '').lower()

def check():
    with open("tokens.txt", encoding="utf-8") as f1, open("ANTLR_p1", encoding="utf-8") as f2:
        tokens1 = [normalize(line) for line in f1 if line.strip()]
        tokens2 = [normalize(line) for line in f2 if line.strip()]

    matched = sum(1 for a, b in zip(tokens1, tokens2) if a == b )
    total = max(len(tokens1), len(tokens2)) or 1

    percent = matched / total * 100

    print(f"{percent:.2f}% similarity")
    
if __name__ == "__main__":
    check()