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

    $(".userLogin").click(function(){
        var emailId = $("#login-email-id").val();
        var password = $("#login-password").val();
        window.pmproject.auth.logIn(emailId, password, {
            "success": function(data){
                window.pmproject.myAccount.setAccountMail(data['email']);
                window.pmproject.myAccount.setAccountName(data["result"]);
                window.pmproject.setNewCSRFToken();
                if (window.location.pathname == "/user-action/login"){
                    window.location = "/"
                }
            },
            "error": function(){
                alert("please try again");
            }
        })
    });

    $(".register-now").click(function(){
        var username = $("#customer-user-name").val();
        var email = $("#customer-email").val();
        var mobileNumber = $("#customer-mobile").val();
        var password = $("#customer-password").val();
        window.pmproject.auth.signup(username,mobileNumber,email, password,true, {
            "success": function(data){
                window.pmproject.myAccount.setAccountMail(data['email']);
                window.pmproject.myAccount.setAccountName(data["name"]);
                window.pmproject.setNewCSRFToken();
                if (window.location.pathname == "/user-action/login"){
                    window.location = ""
                }
            },
            "error": function(){
                alert("Failed To register");
            }
        })
    })


});