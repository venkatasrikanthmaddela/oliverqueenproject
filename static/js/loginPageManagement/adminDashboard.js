/**
 * Created by srikanthmv on 14/8/16.
 */
$( document ).ready(function() {
    $(".side-nav-open-for-mobile").click(function(){
        sideNavOpen()
    });
    $(".side-nav-close").click(function(){
        sideNavClose();
    });

    $(".upload-projects").click(function(){
        var FormId = $(this).attr("data-id");
        var formData = new FormData($(this).closest("#"+FormId)[0]);
        var callbacks = {
            "success": function(data){
                window.location.reload();
            },
            "error":function(data){
                alert('error');
            }
        };
        window.pmprojectutils.getResponse("post",'/api/admin/upload-project-data',formData,callbacks,true)
    });

    function sideNavOpen() {
        if (mySidenav.style.display === 'block') {
            mySidenav.style.display = 'none';
            overlayBg.style.display = "none";
        } else {
            mySidenav.style.display = 'block';
            overlayBg.style.display = "block";
        }
    }
    function sideNavClose() {
        mySidenav.style.display = "none";
        overlayBg.style.display = "none";
    }

});
