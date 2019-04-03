$(document).ready(function(){
    var menu_toggle = false;
    
    const menu_select_color = "#89f";
    const menu_select_padding = "10px";
    
    $("ul.menu").css("height", "50px");
    
    $("ul.menu li.menu-button a").click(function(){
        if (menu_toggle){
            $("ul.menu").css("height", "50px");
        } else {
            $("ul.menu").css("height", "250px");
        }
        menu_toggle = !menu_toggle;
        return false;
    });
    
    $("ul.menu li.menu-item a").click(function(){
        $.scrollTo($(this).attr("href"), 500, {offset:-50});
        return false;
    });
    
    $("div.page-section").waypoint(function(direction){
        id = this.element.id;
        section = $("#"+id+".page-section");
        prev_section = section.prev("div.page-section");
        
        if (prev_section.attr("id") == undefined){
            prev_section = section;
        }
        
        $("ul.menu li.menu-item a").css("color", "white");
        if (direction == "up"){
            $("ul.menu #" + prev_section.attr("id") + ".menu-item a").css("color", menu_select_color);
        }else{
            $("ul.menu #" + section.attr("id") + ".menu-item a").css("color", menu_select_color);
        }
        
    }, {offset: "50px"});
    
    $("ul.menu li.menu-item a").mouseenter(function(){
        $(this).css("padding-left", menu_select_padding);
    });
    $("ul.menu li.menu-item a").mouseleave(function(){
        $(this).css("padding-left", "0px");
    });

    var counter = 1;
    
    
    /*$("#news.page-section h1").click(function(){
        $.get("posts/" + counter.toString() + ".html", function(data){
            console.log(data);
            counter += 1;
            $("div.post-container").html(data);
            MathJax.Hub.Queue(['Typeset', MathJax.Hub, "div.post-container"]);
        }, "text");
    });*/
    
    
    $.get("posts.txt", function(data){
        $("div.post-list").html("");
        
        var post_list = data.split('\n').slice(0, -1);
        post_list.forEach(function(post,idx){
            
            var html = "<div class = \"post-container\">" 
            html += "<h1>" + post + "</h1>"
            
            html += "<\div>"
            
            
            
            $("div.post-list").html($("div.post-list").html() + html);
            console.log(post, idx);
        });
    }, "text");
    
});