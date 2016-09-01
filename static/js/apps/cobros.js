// === metodo para mandar el csrf_token a django mediante ajax ====
$.ajaxSetup({ 
     beforeSend: function(xhr, settings) {
         function getCookie(name) {
             var cookieValue = null;
             if (document.cookie && document.cookie != '') {
                 var cookies = document.cookie.split(';');
                 for (var i = 0; i < cookies.length; i++) {
                     var cookie = jQuery.trim(cookies[i]);
                     // Does this cookie string begin with the name we want?
                     if (cookie.substring(0, name.length + 1) == (name + '=')) {
                         cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                         break;
                     }
                 }
             }
             return cookieValue;
         }
         if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
             // Only send the token to relative URLs i.e. locally.
             xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
         }
     } 
});



// === para recetear la tabla de cartera =====
// funcion para resetear la tabla
function resetTabla() {  
    // var t2 = document.getElementById('tb-cartera').getElementsByTagName('tbody')[0];
    // console.log(t2.rows.length);
    // if (t2.rows.length > 1){    
    //   //funcion para eliminar tr por el id 
    //     function  deleteRow(id) {
    //         document.getElementById('tb-cartera').getElementsByTagName('tbody')[0].removeChild(
    //         document.getElementById(id)
    //         );
    //     }

    //  // for para contar los tr y eliminarlos
    
    //   for (i = 0; i < t2.rows.length; i++) {
    //     console.log(t2.rows[i]);
        
    //     deleteRow('tr_'+i);
        
    //   }
    // }
    $("#tb-cartera > tbody > tr").remove();


}
// total de la recepcion de pago ========================00

function totales_cobro() {
    var informe_final = $('#informe_final').val()*1;
    var fisoterapia = $('#fisoterapia').val()*1;
    var medicina_laboral = $('#medicina_laboral').val()*1;
    var puesto_trabajo = $('#puesto_trabajo').val()*1;
    var trabajo_social = $('#trabajo_social').val()*1;

    var total_cobro = informe_final + fisoterapia + medicina_laboral + puesto_trabajo + trabajo_social;
          
    $('#totales').val(total_cobro);
}


$(".calculo_totales_down").keyup(function(){
  totales_cobro();
});

// ===== para guardar los datos del modal empresa en el servidor ======

$('#buscar').click(function(){
    console.log('llegooo aquiiiiiii');
        
        var t = document.getElementById('tb-cartera').getElementsByTagName('tbody')[0];
        resetTabla();
        $.ajax({
          url: '/buscar_cliente/',
          dataType: 'json',
          data: {'codigo_gl': $('#codigogl').val()},
          success: function(datos) {
            console.log(datos[0]);
            $.map(datos, function (d) {
               console.log(d.cartera); 
               $('#nombres').val(d.nombres);
               $('#pk_cliente').val(d.pk);
            });

            
          
           for (var c in datos[0].cartera){
                
                // obteniendo el tr de la tabla
                var rowCount = t.rows.length;
                // insertando los  td
                var row = t.insertRow(rowCount);
                // insertando ids a los tr de la tabla
                row.id='tr_'+rowCount;
                //agregando celdas
                var cell1 = row.insertCell(0);
                var cell2 = row.insertCell(1);
                var cell3 = row.insertCell(2);
                var cell4 = row.insertCell(3);
                

                // insertando los datos en los td
                cell1.innerHTML = datos[0].cartera[c].examen;
                cell2.innerHTML = datos[0].cartera[c].deuda;
                cell3.innerHTML = datos[0].cartera[c].pago;
                cell4.innerHTML = datos[0].cartera[c].saldo;
                if (datos[0].cartera[c].examen == "CONTRATO") {
                    $('#informe_final').val(datos[0].cartera[c].saldo);
                };
                if (datos[0].cartera[c].examen == "FISIOTERAPIA") {
                    $('#fisoterapia').val(datos[0].cartera[c].saldo);
                };
                if (datos[0].cartera[c].examen == "MEDICINA LABORAL") {
                    $('#medicina_laboral').val(datos[0].cartera[c].saldo);
                };
                if (datos[0].cartera[c].examen == "PUESTO DE TRABAJO") {
                    $('#puesto_trabajo').val(datos[0].cartera[c].saldo);
                };
                if (datos[0].cartera[c].examen == "TRABAJO SOCIAL") {
                    $('#trabajo_social').val(datos[0].cartera[c].saldo);
                };
                              

            };
            totales_cobro();
            
          }

        }).fail(function(data){
            var status = data.status;
            var reason = data.reason;
            var stack_bar_top = {"dir1": "down", "dir2": "right", "push": "top", "spacing1": 0, "spacing2": 0};
            console.log('el cliente con el codigo gl '+$('#codigogl').val()+' no existe');
            new PNotify({
                title: 'Error',
                text: 'el cliente con el codigo gl '+$('#codigogl').val()+' no existe',
                type: 'error',
               
                
                hide: true
            }); 
        });
    
});

// ===== para buscar clienteee ======

$('#buscarcli').click(function(){
    console.log('llegooo aquiiiiiii');
        $.ajax({
          url: '/buscar_cliente/',
          dataType: 'json',
          data: {'nombre_cliente': $('#nombre_cliente').val(), 'ci_cliente': $('#ci_cliente').val()},
          success: function(datos) {
            
            $.map(datos, function (d) {
               console.log(d.nombres); 
               $('#nombre_cli1').val(d.nombres);
               $('#codigo_gl1').val(d.codigo_gl);
               $('#ci_cliente1').val(d.ci);
            });
            
          }
        }).fail(function(data){
            var status = data.status;
            var reason = data.reason;
            var stack_bar_top = {"dir1": "down", "dir2": "right", "push": "top", "spacing1": 0, "spacing2": 0};
            console.log('el cliente con el codigo gl '+$('#codigogl').val()+' no existe');
            new PNotify({
                title: 'Error',
                text: 'el cliente con el codigo gl '+$('#codigogl').val()+' no existe',
                type: 'error',
               
                
                hide: true
            }); 
        });
    
});

$('#aceptar_busqueda').click(function(){
   $('#codigogl').val($('#codigo_gl1').val());
    // para limpiar los imputs del modal
   $('.modal-body').find('textarea,input').val('');

   // para cerrar el modal
   $('#Modalcliente').modal('hide');
         
});

// ===== para guardar los datos del cobro ======

$('#register-cobro').click(function(){
    console.log('am i called');
    if ($("#formclinica").valid()) {
        $.ajax({
            type: "POST",
            url: "/registrar_cobro/",
            dataType: "json",
            data: $("#formcobro").serialize(),
            success: function(data) {
               // console.log(data);
               window.open("http://sisgoodlife.herokuapp.com/detallecartera/"+data.pk, "_blank");
               // para eliminar lo seleccionado en select clinica
          }
        }); 
    } 

    
});