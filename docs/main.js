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
        $(this).parent("li.menu-item").css("padding-left", menu_select_padding);
    });
    $("ul.menu li.menu-item a").mouseleave(function(){
        $(this).parent("li.menu-item").css("padding-left", "0px");
    });
    
});