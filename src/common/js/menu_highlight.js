$(document).ready(function(){

    /*var elem = $(window.location.hash);
    if (elem){
        $.scrollTo(elem, 500, {offset:-50});
    }*/
    
    $("ul.menu li.menu-item a").click(function(){
        $.scrollTo($(this).attr("href"), 500, {offset:-50});
        console.log("1");
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
            $("ul.menu #" + prev_section.attr("id") + ".menu-item a").css("color", "#89f");
        }else{
            $("ul.menu #" + section.attr("id") + ".menu-item a").css("color", "#89f");
        }
        
    }, {offset: "50px"});
});