import markdown


def compile_post(post):
    input = open("posts/" + post + ".md", "r")
    output = open("docs/posts/" + post + ".html", "w")

    print("<html>", file=output)
    print("<body style=\"margin: 0;\">", file=output)
    print(markdown.markdown(input.read()), file=output)
    print("</body>", file=output)
    print("</html>", file=output)



index = open("docs/index.html", "w")


def menu_item(item):
    print("<li class=\"menu-item\"><a href=\"#" + item.lower() + ".page-section\" id=\"" + item.lower() + "\"><b>" + item + "</b></a></li>", file=index)


def page_section_begin(block, color):
    print("<div class = \"page-section\" id=\"" + block.lower() + "\" style=\"background-color: " + color + "\">", file=index)
    print("<h1 class = \"page-section-title\">" + block + "</h1>", file=index)
    

def page_section_end():
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
print("<script src=\"jquery.waypoints.min.js\"></script>", file=index)
print("<script src=\"jquery.scrollTo.min.js\"></script>", file=index)
print("<script src=\"main.js\"></script>", file=index)
print("<link rel=\"stylesheet\" href=\"https://use.fontawesome.com/releases/v5.8.1/css/all.css\" integrity=\"sha384-50oBUHEmvpQ+1lW4y57PTFmhCaXp0ML5d60M1M7uH2+nqUivzIebhndOJK28anvf\" crossorigin=\"anonymous\">", file=index)
print("</head>", file=index)

print("<body>", file=index)
# BODY BEGIN

# MENU BEGIN
print("<ul class=\"menu\">", file=index)

print("<li class=\"menu-button\"><a href=\"index.html\"><i class=\"fas fa-bars\"></i></a></li>", file=index)
print("<li class=\"menu-title\"><a href=\"index.html\"><b>Author Name</b></a></li>", file=index)


menu_item("About")
menu_item("News")
menu_item("Papers")
menu_item("Contact")

print("</ul>", file=index)
# MENU END

# SECTIONS BEGIN
page_section_begin("About", "#ffffff")
page_section_end()


page_section_begin("News", "#f7f7f7")
#print("<iframe class=\"post-contaner\" src = \"posts/1.html\"></iframe>", file=index)
page_section_end()


page_section_begin("Papers", "#ffffff")
page_section_end()


page_section_begin("Contact", "#f7f7f7")
page_section_end()
# SECTIONS END


# BODY END
print("</body>", file=index)
print("</html>", file=index)


#print("", file=index)






