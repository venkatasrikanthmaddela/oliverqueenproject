/**
 * Created by srikanthmv on 1/12/16.
 */

$(document).ready(function(){
    $(".loginFromModal").click(function(){
        var emailId = $("#login-email-id").val();
        var password = $("#login-password").val();
        window.pmproject.auth.logIn(emailId, password, {
            "success": function(data){
                window.pmproject.myAccount.setAccountMail(data['email']);
                window.pmproject.myAccount.setAccountName(data["result"]);
                window.pmproject.setNewCSRFToken();
                if (window.location.pathname == "/new-project-idea"){
                    window.location = "/new-project-idea/success"
                }
            },
            "error": function(){
                alert("please try again");
            }
        })
    });
    $(".registerFromModal").click(function(){
        var username = $("#customer-user-name").val();
        var email = $("#customer-email").val();
        var mobileNumber = $("#customer-mobile").val();
        var password = $("#customer-password").val();
        window.pmproject.auth.signup(username,mobileNumber,email, password,true, {
            "success": function(data){
                window.pmproject.myAccount.setAccountMail(data['email']);
                window.pmproject.myAccount.setAccountName(data["name"]);
                window.pmproject.setNewCSRFToken();
                if (window.location.pathname == "/new-project-idea"){
                    window.location = "/new-project-idea/success";
                }
            },
            "error": function(){
                alert("Failed To register");
            }
        })
    });
    $(".sendNewProjectIdea").click(function(){
         var elementData = this;
         window.pmproject.auth.checkUserLogin({
        "success":function(){
            saveProjectIdea(elementData);
        },
        "error": function(){
            document.getElementById('loginModal').style.display='block';
        }
    });
    });

});
function saveProjectIdea(currentElement){
    var formId = $(currentElement).attr("data-form-id");
    var formData = new FormData($("#"+formId)[0]);
    var projectCallBacks = {
        "success": function(){
            window.location.href = "/new-project-idea/success";
        },
        "error": function(){
            alert("error in saving project details. please try after some time. Inconvienience regretted.")
        }
    };
    window.pmproject.getResponse("POST", "/api/new-project-idea/save-project-idea", formData, projectCallBacks,true)
}