var hh  = "hola";
console.log(hh);





function Get(yourUrl){
    var Httpreq = new XMLHttpRequest(); // a new request
    Httpreq.open("GET",yourUrl,false);
    Httpreq.send(null);
    return Httpreq.responseText;          
}

function getResult(){
    var sl=document.getElementById('sepal_lenght').value;
    var sw=document.getElementById('sepal_width').value;
    var pl=document.getElementById('petal_lenght').value;
    var pw=document.getElementById('petal_width').value;

    var url= "https://openwhisk.ng.bluemix.net/api/v1/web/kelvin.ferreiras%40rochester.edu_dev/default/GetWMLResult.json?"+"sl="+sl+"&"+"sw="+sw+"&"+"pl="+pl+"&"+"pw="+pw;
    var json_obj = JSON.parse(Get(url));

    console.log("HERE: "+json_obj.values[0][8]);
    document.getElementById('resultText').innerHTML = json_obj.values[0][8];

}



