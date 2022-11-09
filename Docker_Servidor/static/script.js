function createHeader(data) {
    
    var body = document.getElementsByTagName('body')[0];
    var tb = document.createElement('table');
    tb.setAttribute('id', 'mastertable');
    
    var thead = document.createElement('thead');
    
    var tr = document.createElement('tr');
   
    var headers_to_add = ["Nombre", "Tipo de Sensor", "Intervalo de Tiempo", "Función Modbus Lectura", "Dirección", "Nº Registros", "Comentarios", "Acciones"];

    for(var i = 0, l = headers_to_add.length; i < l; i++){ 
        
        var thx = document.createElement('th');
        thx.appendChild(document.createTextNode(headers_to_add[i]))
        tr.appendChild(thx)

    }

    thead.appendChild(tr);
    
    tb.appendChild(thead);
    var container = document.querySelector('#main');
    
    var maindiv= document.createElement('div');
    maindiv.setAttribute('id', 'maindiv');
    var title = document.createElement('h2');
    title.innerHTML="Sensores configurados";

    var bt = document.createElement('button');
    var a = document.createElement('a');

    bt.setAttribute('id', 'sendbutton');
    bt.setAttribute('onclick', 'sendtoDevice()');
    a.innerHTML = 'Guardar cambios';

    bt.appendChild(a);

    maindiv.insertBefore(bt, maindiv.firstChild);
    maindiv.insertBefore(tb, maindiv.firstChild);
    maindiv.insertBefore(title, maindiv.firstChild);
    container.insertBefore(maindiv, container.firstChild);

    
  }

function deleteRow(btn) {

    var count = document.getElementById('mastertable').rows.length;
    if(count == 2){
        document.getElementById('maindiv').remove();
        sendtoDevice();
    }
    else{
        var row = btn.parentNode.parentNode;
        row.parentNode.removeChild(row);
    }
    

  }

function addRow(name, type, interval, modbusfunc, address, number, comments){
    if(document.querySelector('#mastertable') == null){
        createHeader();
    }

    var aux = [name, type, interval, modbusfunc, address, number, comments];

    var tbodyRef = document.getElementById('mastertable').getElementsByTagName('tbody')[0];

    if( tbodyRef == undefined){
        var tb = document.getElementById('mastertable');
        tbodyRef = document.createElement('tbody');
        tb.appendChild(tbodyRef);
    }

    var data_to_add = ["name", "type", "interval","modbusfunc","address", "number", "comments"];
    var button_to_add = ["Medir valor", "Calibrar", "Eliminar"]
    var button_functions = [" "," ","deleteRow(this)"]

    var newRow = tbodyRef.insertRow(-1);

    for(var i = 0, l = data_to_add.length; i < l; i++){
        var newCell = newRow.insertCell();
        if(aux[i] == undefined){
            var newdata = document.createTextNode(document.getElementById(data_to_add[i]).value);
        }
        else{
            var newdata = document.createTextNode(aux[i]);
        }

        newCell.appendChild(newdata);
    }

    var newCell = newRow.insertCell();
    for (var i = 0, l = button_to_add.length; i < l; i++) {
        var newbutton = document.createElement("button");
        newbutton.innerText = button_to_add[i];
        newbutton.setAttribute('onclick', button_functions[i]);
        newCell.appendChild(newbutton);
    }

}

function sendtoDevice(){
    try{
        let table = document.getElementById("mastertable");
        let tableinfo = JSON.stringify(tableToJson(table));
        const request = new XMLHttpRequest();
        request.open('POST', `/download/${tableinfo}`);
        request.send();
        alert("Configuración guardada")
    }
    catch(Buit){
        const request = new XMLHttpRequest();
        request.open('GET', `/remove`);
        request.send();
        alert("Configuración borrada")
    }
        
}

function tableToJson(table) {
    var data = [];

    // first row needs to be headers
    var headers = [];
    for (var i=0; i<table.rows[0].cells.length - 1; i++) {
        headers[i] = table.rows[0].cells[i].innerHTML.toLowerCase().replace(/ /gi,'');
    }

    // go through cells
    for (var i=1; i<table.rows.length; i++) {

        var tableRow = table.rows[i];
        var rowData = {};
        var j;
        for (j=0; j<table.rows[0].cells.length - 1; j++) {

            rowData[ headers[j] ] = tableRow.cells[j].innerHTML;

        }
        if(j!=0){
            data.push(rowData);
        }

    }       

    return data;
}

function unEscape(htmlStr) {
    htmlStr = htmlStr.replace(/&lt;/g , "<");	 
    htmlStr = htmlStr.replace(/&gt;/g , ">");     
    htmlStr = htmlStr.replace(/&quot;/g , "\"");  
    htmlStr = htmlStr.replace(/&#39;/g , "\'");   
    htmlStr = htmlStr.replace(/&amp;/g , "&");
    return htmlStr;
}

function Update_Table(string_sensors){
    if(string_sensors!="[]"){
        if(document.querySelector('#mastertable') == null){
            createHeader();
        }

        var sensors_object = eval(string_sensors);
        for (var i = 0; i < sensors_object.length; i++){
            var obj = sensors_object[i];
            
        addRow(obj["nombre"],obj["tipodesensor"],obj["intervalodetiempo"], obj["funciónmodbuslectura"], obj["dirección"], obj["nºregistros"], obj["comentarios"] );
        }   
    }
}

function load_addresses(){
    const FuncioModbusTriada = document.querySelector("#modbusfunc").value;
    const Address = document.querySelector("#address");
    const num = document.querySelector("#number");
    Address.disabled = false;
    Address.length = 1;     
    Address.options[Address.options.length] = new Option("Dirección", " ", false, false);
    Address.options[1].hidden= true;

    const zeroPad = (num, places) => String(num).padStart(places, '0')

    for ( addr  of adressesbyfunction[FuncioModbusTriada]) {
        if(addr <= 9){
            addr = zeroPad(addr, 2);
        }
        Address.options[Address.options.length] = new Option(
        addr,
        addr
        );
    }
    num.value = undefined;
    num.disabled = false;
}
var adressesbyfunction = {
    "Function 01 (Read Coil Status)": [00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18],
    "Function 02 (Read Input Status)": [00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13],
    "Function 03 (Read Holding Registers)": [00, 02, 04, 06, 08, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 
        36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 200, 202, 204, 206, 208, 
        210, 212, 214, 216, 218, 220, 222, 224, 226, 228, 230, 232, 234, 236, 238, 240, 242, 244, 246, 248, 250, 252, 
        254],
    "Function 04 (Read Input Registers)": [00, 02, 04, 06, 08, 10, 12, 14, 16, 18, 20, 22, 24, 26],
    "Function 05 (Force Single Coil)": [00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15],
    "Function 16 (Preset Multiple Registers)": [00, 02, 04, 06, 08, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34,
         36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 200, 202, 204, 206, 208, 
        210, 212, 214, 216, 218, 220, 222]
  };
