/**
 * Created by srikanthmv on 17/3/17.
 */

$( document ).ready(function() {
    $("#bulk-upload-projects").click(function(){
        var FormId = $(this).attr("data-id");
        console.log($("#bulkUploadFile").val());
        var formData = new FormData($(this).closest("#"+FormId)[0]);
        var callbacks = {
            "success": function(data){
                $("#bulkUploadFile").val('');
                $("#successAlertMsg").text("All projects uploaded sucessfully..");
                $("#successAlertModal").show();

            },
            "error":function(data){
                $("#bulkUploadFile").val('');
                $("#errorAlertMsg").text(data.responseJSON.errorData.errorCode + ":" + data.responseJSON.errorData.errorMsg);
                $("#errorAlertModal").show();
            }
        };
        window.pmprojectutils.getResponse("post",'/api/admin/upload-in-bulk-projects',formData,callbacks,true)
    });

});