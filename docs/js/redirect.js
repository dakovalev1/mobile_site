$(document).ready(function(){
    var elem = $(window.location.hash);
    if (elem){
        $.scrollTo(elem, 500, {offset:-50});
    }
});