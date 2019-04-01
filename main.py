index = open("docs/index.html", "w")


def menu_item(item):
    print("<li class=\"menu-item\"><a href=\"#" + item.lower() + ".body-section\" id=\"" + item.lower() + "\"><b>" + item + "</b></a></li>", file=index)


print("<!DOCTYPE html>", file=index)
print("<html lang = \"en-US\">", file=index)

print("<head>", file=index)
print("<meta charset=\"utf-8\">", file=index)
print("<title>Author Name</title>", file=index)
print("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">", file=index)
print("<link rel=\"stylesheet\" href=\"main.css\">", file=index)
print("<script src=\"https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js\"></script>", file=index)
print("<script src=\"main.js\"></script>", file=index)
print("</head>", file=index)

print("<body>", file=index)
# BODY BEGIN

# MENU BEGIN
print("<ul class=\"menu\">", file=index)

print("<li class=\"menu-button\"><a href=\"index.html\"><b>X</b></a></li>", file=index)
print("<li class=\"menu-title\"><a href=\"index.html\"><b>Author Name</b></a></li>", file=index)


menu_item("Home")
menu_item("News")
menu_item("Papers")
menu_item("Contact")

print("</ul>", file=index)
# MENU END


# BODY END
print("</body>", file=index)
print("</html>", file=index)


#print("", file=index)



