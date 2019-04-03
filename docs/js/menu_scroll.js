$(document).ready(function(){
    $("ul.menu li.menu-item a").click(function(){
        id = $(this).parent("li.menu-item").attr("id");
        $.scrollTo("#" + id + ".page-section", 500, {offset:-50});
        return false;
    });
});