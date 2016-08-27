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

    $(".upload-project").click(function () {
        var FormId = $(this).attr("data-id");
        var formData = new FormData($(this).closest("#"+FormId)[0]);
        var callbacks = {
            "success": function(data){
                document.getElementById('uploadSuccess').style.display='block';
                window.location.reload();
            },
            "error":function(data){
                alert('error');
            }
        };
        window.pmprojectutils.getResponse("post",'/api/admin/upload-project',formData,callbacks,true)
    });

    $(".delete-project").click(function(){
        if( window.confirm("Are You Sure??") ) {
            var orderData = {
                "orderId": $(this).attr("data-id")
            };
            var callbacks = {
                "success": function(data){
                    document.getElementById('deleteSuccess').style.display='block';
                    window.location.reload();
                },
                "error":function(data){
                }
            };
            window.pmprojectutils.getResponse("delete",'/api/admin/delete-project',orderData,callbacks,false)
        }
    });

    $(".update-project").click(function(){
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
        window.pmprojectutils.getResponse("put",'/api/admin/update-project',formData,callbacks,true)
    });

    $(".edit-project").click(function(){
        $("#updateProjectForm [name=projectTitle]").val($(this).attr("data-title"));
        $("#updateProjectForm [name=projectFramework]").val($(this).attr("data-framework"));
        $("#updateProjectForm [name=targetStream]").val($(this).attr("data-target-stream"));
        $("#updateProjectForm [data-label='" + $(this).attr("data-iee-papers") + "']").prop("checked", true);
        $("#updateProjectForm [name=projectAbstract]").val($(this).attr("data-abstract"));
        $("#updateProjectForm [name=projectId]").val($(this).attr("data-id"));
        document.getElementById('projectEditModal').style.display='block';
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
