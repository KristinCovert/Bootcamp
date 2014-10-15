/**
 * Created by Kristin on 10/15/14.
 */
$(document).ready(function (){

    $(".about-icon").hover(
        function(){
            $(this).attr({src: "/pictures/unicorn.jpg"})
        },
        function(){
            $(this).attr({src: "/pictures/AboutIcon.jpeg"})
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



    (function($) {
        $(document).ready(function () {
            /*-------------------- EXPANDABLE PANELS ----------------------*/
            var panelspeed = 600; //panel animate speed in milliseconds
            var totalpanels = 3; //total number of collapsible panels
            var defaultopenpanel = 0; //leave 0 for no panel open
            var accordian = false; //set panels to behave like an accordian, with one panel only ever open at once

            var panelheight = new Array();
            var currentpanel = defaultopenpanel;
            var iconheight = parseInt($('.icon-close-open').css('height'));
            var highlightopen = true;

            //Initialise collapsible panels
            function panelinit() {
                    for (var i=1; i<=totalpanels; i++) {
                        panelheight[i] = parseInt($('#cp-'+i).find('.expandable-panel-content').css('height'));
                        $('#cp-'+i).find('.expandable-panel-content').css('margin-top', -panelheight[i]);
                        if (defaultopenpanel == i) {
                            $('#cp-'+i).find('.icon-close-open').css('background-position', '0px -'+iconheight+'px');
                            $('#cp-'+i).find('.expandable-panel-content').css('margin-top', 0);
                        }
                    }
            }

            $('.expandable-panel-heading').click(function() {
                var obj = $(this).next();
                var objid = parseInt($(this).parent().attr('ID').substr(3,2));
                currentpanel = objid;
                if (accordian == true) {
                    resetpanels();
                }

                if (parseInt(obj.css('margin-top')) <= (panelheight[objid]*-1)) {
                    obj.clearQueue();
                    obj.stop();
                    obj.prev().find('.icon-close-open').css('background-position', '0px -'+iconheight+'px');
                    obj.animate({'margin-top':0}, panelspeed);
                    if (highlightopen == true) {
                        $('#cp-'+currentpanel + ' .expandable-panel-heading').addClass('header-active');
                    }
                } else {
                    obj.clearQueue();
                    obj.stop();
                    obj.prev().find('.icon-close-open').css('background-position', '0px 0px');
                    obj.animate({'margin-top':(panelheight[objid]*-1)}, panelspeed);
                    if (highlightopen == true) {
                        $('#cp-'+currentpanel + ' .expandable-panel-heading').removeClass('header-active');
                    }
                }
            });

            function resetpanels() {
                for (var i=1; i<=totalpanels; i++) {
                    if (currentpanel != i) {
                        $('#cp-'+i).find('.icon-close-open').css('background-position', '0px 0px');
                        $('#cp-'+i).find('.expandable-panel-content').animate({'margin-top':-panelheight[i]}, panelspeed);
                        if (highlightopen == true) {
                            $('#cp-'+i + ' .expandable-panel-heading').removeClass('header-active');
                        }
                    }
                }
            }

           //Uncomment these lines if the expandable panels are not a fixed width and need to resize
           /* $( window ).resize(function() {
              panelinit();
            });*/

            $(window).load(function() {
                panelinit();
            }); //END LOAD
        }); //END READY
    })(jQuery);
});