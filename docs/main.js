$(document).ready(function(){
    var menu_toggle = false;
    $("ul.menu").css("height", "40px");
    
    $("ul.menu li.menu-button a").click(function(){
        if (menu_toggle){
            $("ul.menu").css("height", "40px");
        } else {
            $("ul.menu").css("height", "200px");
        }
        menu_toggle = !menu_toggle;
        return false;
    });
});