/**
 * Created by srikanthmv on 1/2/17.
 */

$(".request-for-project").click(function(){
         var elementData = this;
         window.pmproject.auth.checkUserLogin({
        "success":function(){
            alert("this is dsfd");
            saveProjectIdea(elementData);
        },
        "error": function(){
            projectIdeaElement = elementData;
            document.getElementById('loginModal').style.display='block';
        }
    });
    });
var projectIdeaElement = "";
