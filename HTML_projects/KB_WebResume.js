/**
 * Created by student on 10/10/14.
 */
$(document).ready(function (){

    $(".about-icon").hover(
        function(){
            $(this).attr({src: "/pictures/AboutIconUni.jpeg"})
        },
        function(){
            $(this).attr({src: "/pictures/unicorn.jpg"})
    });

    function spinLarge () {
        var angle = 0;
        return setInterval(function(){
            angle-=3;
            $("#LG_cog").rotate(angle);
            },50);
    }

    function spin () {
        spinLarge()
        var smallAngle = 0;
        return setInterval(function () {
            smallAngle += 3;
            $("#SM_cog").rotate(smallAngle);
        }, 50);
    }

//    I still can't get the wheel to stop turning but at least they start on hover
    $(".cog-container").hover(
        function() {
            spin();
        },
        function() {
                $("SM_cog", "LG_cog").rotate(0);
      });

    $("#codeguildBW").hover(
        function() {
            $(this).attr({src: "/pictures/PDX_CodeGuild.png"})
        },
            function() {
                $(this).attr({src: "/pictures/PDX_CodeGuild_BW.png"})
        });

    $("#nauBW").hover(
        function() {
            $(this).attr({src: "/pictures/nau_color.png"})
        },
        function() {
            $(this).attr({src: "/pictures/nau_BW.png"})

    });

    $("#ucscBW").hover(
        function() {
            $(this).attr({src: "/pictures/UCSC_color.jpg"})
        },
        function(){
            $(this).attr({src: "/pictures/UCSC_bw.jpg"})
    });

});