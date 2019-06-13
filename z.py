
if __name__ == "__main__":
    task = ["ré-0.txt", "re\u0301-1.txt"]
    for one in task:
        print(len(one), one)
        with open(one, "w") as f:
            f.write(one)

