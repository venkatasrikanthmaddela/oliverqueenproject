/**
 * Created by Oliver Queen on 8/10/2016.
 */
$( document ).ready(function() {
    $(".register-here").click(function(){
        $(".login-page").addClass("w3-hide");
        $(".registration-page").removeClass("w3-hide");
    });
    $(".sign-in-here").click(function () {
        $(".registration-page").addClass("w3-hide");
        $(".login-page").removeClass("w3-hide");
    });

    $(".scroll-source").click(function(){
        ScrollToTarget($(this).attr("data-scroll-target"));
    });
    function ScrollToTarget(targetElement){
        $('html, body').animate({
            scrollTop: $(targetElement).offset().top
        }, 1500);
    }

});