import wikipedia

title = input("Enter title: ")
while title != "":
    page = wikipedia.page(title, auto_suggest=False)
    print(page.title)
    print(page.summary)
    print(page.url)
    title = input("Enter title: ")
