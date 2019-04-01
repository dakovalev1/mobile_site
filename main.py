index = open("docs/index.html", "w")


def menu_item(item):
    print("<li class=\"menu-item\"><a href=\"#" + item.lower() + ".page-section\" id=\"" + item.lower() + "\"><b>" + item + "</b></a></li>", file=index)


def page_section(block, color):
    print("<div class = \"page-section\" id=\"" + block.lower() + "\" style=\"background-color: " + color + "\">", file=index)
    #print("123", file=index)
    print("<h1 class = \"page-section-title\">" + block + "</h1>", file=index)
    print("...some text...<br>", file=index)
    print("...some text...<br>", file=index)
    print("...some text...<br>", file=index)
    print("</div>", file=index)



print("<!DOCTYPE html>", file=index)
print("<html lang = \"en-US\">", file=index)

print("<head>", file=index)
print("<meta charset=\"utf-8\">", file=index)
print("<title>Author Name</title>", file=index)
print("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">", file=index)
print("<link rel=\"stylesheet\" href=\"main.css\">", file=index)
print("<script src=\"https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js\"></script>", file=index)
print("<script src=\"main.js\"></script>", file=index)
print("<link rel=\"stylesheet\" href=\"https://use.fontawesome.com/releases/v5.8.1/css/all.css\" integrity=\"sha384-50oBUHEmvpQ+1lW4y57PTFmhCaXp0ML5d60M1M7uH2+nqUivzIebhndOJK28anvf\" crossorigin=\"anonymous\">", file=index)
print("</head>", file=index)

print("<body>", file=index)
# BODY BEGIN

# MENU BEGIN
print("<ul class=\"menu\">", file=index)

print("<li class=\"menu-button\"><a href=\"index.html\"><i class=\"fas fa-bars\"></i></a></li>", file=index)
print("<li class=\"menu-title\"><a href=\"index.html\"><b>Author Name</b></a></li>", file=index)


menu_item("Home")
menu_item("News")
menu_item("Papers")
menu_item("Contact")

print("</ul>", file=index)
# MENU END

# SECTIONS BEGIN
page_section("Home", "#ffffff")
page_section("News", "#f7f7f7")
page_section("Papers", "#ffffff")
page_section("Contact", "#f7f7f7")
# SECTIONS END


# BODY END
print("</body>", file=index)
print("</html>", file=index)


#print("", file=index)



