var usuario = $("#user_name_obj").text()

var modelObjID;

$(function () {

    recordsRelationalships();   

});



function recordsRelationalships() {

    $.getJSON('/api/sunshine/relationships/records?type=devices_has_device', function(data){
        
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

    $.getJSON('/api/sunshine/objects/records?type=devices', function(dataDevice){

        $(dataDevice.data).each(function(index,itemDevice) {
                       
            var modelname = itemDevice.attributes["Model Name"];

            if (modelObjID == itemDevice.id) {

                console.log(modelname);
                $("#customObjectList").append("<li>" + modelname + "</li>")

                
            };
        
        });

    });
    
};
