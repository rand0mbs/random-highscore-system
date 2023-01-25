highscore = 0

while True:
    try:
        score = int(input("\nAdj egy számot: "))

        if score >= highscore:
            highscore = score

        print(f"Legnagyobb: {highscore}")

    except:
        print("\"számot\"")
