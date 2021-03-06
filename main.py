import os
import shutil
import markdown
import configparser
import numpy

MAX_POSTS = 5

# def compile_posts():
#     post_list = open("docs/posts.txt", "w")
#     for root, dirs, files in os.walk("posts"):

#         int_names = [int(name, 10) for name in dirs]
#         int_names.sort()
#         str_names = [str(name) for name in int_names]
#         str_names.reverse()

#         for name in str_names[:MAX_POSTS]:
#             # index.md
#             input = open(os.path.join(root, name, "index.md"), "r")
#             os.mkdir(os.path.join("docs/posts", name))
#             output = open(os.path.join("docs/posts", name, "post.html"), "w")
#             print(markdown.markdown(input.read(), extensions=['mdx_math']),file=output)

#             # config.cfg
#             cfg = configparser.ConfigParser()
#             cfg.read(os.path.join(root, name, "config.cfg"))
            
#             print("post:", name)
#             print(name, file=post_list)

#             output = open(os.path.join("docs/posts", name, "summary.html"), "w")
#             print("<div class=\"post-container\">",file=output)
#             print("<h1>" + cfg["DEFAULT"]["title"] + "</h1>",file=output)
#             print(cfg["DEFAULT"]["summary"],file=output)
#             print("<div class = \"date-container\">" + cfg["DEFAULT"]["date"] + "</div>",file=output)
#             print("</div>",file=output)
#         break



def page_section_begin(index, block, color):
        print("<div class = \"page-section\" id=\"" + block.lower() + "\" style=\"background-color: " + color + "\">", file=index)
        print("<h1 class = \"page-section-title\">" + block + "</h1>", file=index)
def page_section_end(index):
    print("1<br>", file=index)
    print("1<br>", file=index)
    print("1<br>", file=index)
    print("1<br>", file=index)
    print("1<br>", file=index)
    print("1<br>", file=index)
    print("</div>", file=index)

def news_section(index, number=None):

    for root, dirs, files in os.walk("posts"):
        int_names = [int(name, 10) for name in dirs]
        int_names.sort()
        str_names = [str(name) for name in int_names]
        str_names.reverse()

        if (number is None) == False:
            str_names = str_names[:number]

        for name in str_names:
            # config.cfg
            cfg = configparser.ConfigParser()
            cfg.read(os.path.join(root, name, "config.cfg"))
        
            print("post:", name)
            print("<div class=\"post-container\">",file=index)
            print("<h1>" + cfg["DEFAULT"]["title"] + "</h1>",file=index)
            print(cfg["DEFAULT"]["summary"],file=index)
            print("<div class = \"date-container\">" + cfg["DEFAULT"]["date"] + "</div>",file=index)
            print("</div>",file=index)
        break



def gen_index():
    index = open("docs/index.html", "w")

    


    print("<!DOCTYPE html>", file=index)
    print("<html lang = \"en-US\">", file=index)
    print("<head>", file=index)

    head = open("src/common/html/head.html", "r")
    index.write(head.read())

    print("<script src=\"js/redirect.js\"></script>", file=index)
    print("<script src=\"js/menu_slide.js\"></script>", file=index)
    print("<script src=\"js/menu_highlight.js\"></script>", file=index)
    print("<script src=\"js/menu_scroll.js\"></script>", file=index)

    print("<link rel=\"stylesheet\" href=\"css/common.css\">", file=index)

    print("</head>", file=index)

    print("<body>", file=index)

    menu = open("src/common/html/menu.html", "r")
    index.write(menu.read())


    page_section_begin(index, "About", "#ffffff")
    page_section_end(index)

    page_section_begin(index, "News", "#f7f7f7")
    print("<a href=\"news.html\" class=\"post-link\">More Posts <i class=\"fas fa-angle-double-right\"></i></a>", file=index)
    news_section(index, MAX_POSTS)
    page_section_end(index)

    page_section_begin(index, "Papers", "#ffffff")
    page_section_end(index)

    page_section_begin(index, "Contact", "#f7f7f7")
    page_section_end(index)

    print("</body>", file=index)
    print("</html>", file=index)



def gen_news():
    index = open("docs/news.html", "w")

    print("<!DOCTYPE html>", file=index)
    print("<html lang = \"en-US\">", file=index)
    print("<head>", file=index)

    head = open("src/common/html/head.html", "r")
    index.write(head.read())

    print("<script src=\"js/redirect.js\"></script>", file=index)
    print("<script src=\"js/menu_slide.js\"></script>", file=index)

    print("<link rel=\"stylesheet\" href=\"css/common.css\">", file=index)
    print("<link rel=\"stylesheet\" href=\"css/news.css\">", file=index)

    print("</head>", file=index)

    print("<body>", file=index)

    menu = open("src/common/html/menu.html", "r")
    index.write(menu.read())

    page_section_begin(index, "News", "#f7f7f7")
    news_section(index)
    page_section_end(index)   

    print("</body>", file=index)
    print("</html>", file=index)

def clean():
    if os.path.exists("docs"):
        shutil.rmtree("docs")


clean()

os.mkdir("docs")
os.mkdir("docs/css")
os.mkdir("docs/js")

shutil.copy("src/common/css/common.css", "docs/css/common.css")
shutil.copy("src/common/css/news.css", "docs/css/news.css")

shutil.copy("src/common/js/jquery.waypoints.min.js", "docs/js/jquery.waypoints.min.js")
shutil.copy("src/common/js/jquery.scrollTo.min.js", "docs/js/jquery.scrollTo.min.js")

shutil.copy("src/common/js/redirect.js", "docs/js/redirect.js")
shutil.copy("src/common/js/menu_slide.js", "docs/js/menu_slide.js")
shutil.copy("src/common/js/menu_highlight.js", "docs/js/menu_highlight.js")
shutil.copy("src/common/js/menu_scroll.js", "docs/js/menu_scroll.js")

gen_index()
gen_news()



#compile_posts()
