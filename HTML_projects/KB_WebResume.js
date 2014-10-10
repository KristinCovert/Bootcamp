/**
 * Created by student on 10/10/14.
 */
$(document).ready(function (){

    //to-do: get all icons and loop through adding the JQuery event handler to them
    //[icon,icon,icon].forEach(function(icon){$(icon).bind(function(){$(this).hover(function(){$(this).toggleClass(".icon-hover")})})})

    var $icons = $("div.home-icons").children().children();
    //console.log($icons);

    $(".icon").hover(function () {
        $(this).css({

        })
    })
});