# Create a string and break it in exactly 140 characters
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""

for headline in headlines:
    if len(news_ticker) + len(headline) <= 140:
        news_ticker += headline + " "

    else:
        for character in headline:
            if len(news_ticker) + len(character) <= 140:
                news_ticker += character
            else:
                break

print(news_ticker)
print(len(news_ticker))