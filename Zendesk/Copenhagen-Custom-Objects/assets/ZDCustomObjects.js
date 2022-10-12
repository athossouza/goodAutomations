var usuario = $("#user_name_obj").text()
var custom_object_zd = $("#custom_object_zd").text()
var custom_object_relationship = $("#custom_object_relationship").text()
var title_bject_relationship = $("#title_bject_relationship").text()

var modelObjID;

$(function () {

    recordsRelationalships();   

});



function recordsRelationalships() {

    $.getJSON('/api/sunshine/relationships/records?type=' + custom_object_relationship, function(data){
        
        $(data.data).each(function(index, item) {
            var user = item['source'].split(":");
            var userLogged = user[2];
            if(userLogged == usuario){
                userObjtgt = item["target"];
                modelObjID = userObjtgt;
                userNameObj();  // ask function for check which records linked to user
                               
            };

        });
        
    });       
    
};  
 


function userNameObj() {

    var modelObjID = userObjtgt;

    $.getJSON('/api/sunshine/objects/records?type=' + custom_object_zd, function(dataDevice){

        $(dataDevice.data).each(function(index,itemDevice) {
                       
            var modelname = itemDevice.attributes[title_bject_relationship];

            if (modelObjID == itemDevice.id) {

                console.log(modelname);
                $("#customObjectList").append("<li>" + modelname + "</li>")

                
            };
        
        });

    });
    
};
