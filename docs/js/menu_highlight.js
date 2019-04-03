$(document).ready(function(){
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