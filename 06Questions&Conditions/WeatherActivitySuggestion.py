# Suggest an activity based on the weather(eg, Sunny - "Go for a walk", Rainy - "Read a book")
# Snowy - Build a snowman


weather = input("What's weather like? ")

if weather == "Sunny":
    ISuggest = "Go for a walk"
elif weather == "Rainy":
    ISuggest = "Read a book"
elif weather == "Snowy":
    ISuggest = "Build a snowman"
else:
    ISuggest = "Sleep"  

print(f"For {weather} i suggest you should ", ISuggest)      