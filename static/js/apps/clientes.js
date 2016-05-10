
// ====== para mostrar fecha de ingreso en el input ====
var now = new Date();
console.log(now);
$('#id_fecha_ingreso').val(now);
var day = ("0" + now.getDate()).slice(-2);
var month = ("0" + (now.getMonth() + 1)).slice(-2);
var today = (day)+"-"+(month)+"-"+now.getFullYear() ;

$('#id_fecha_ingreso3').val(today);
$('#id_fecha_ingreso3').attr('disabled', true);

// ===== validador cliente =========


 $('#formcliente').validate({
    
    rules: {
        nombres: {
           
            required: true
        },
        apellidos: {
           
            required: true
        },
        edad: {
           
            required: true
        },
        ci: {
           
            required: true
        },
        telefono: {
           
            required: true
        },
        empresa: {
           
            required: true
        },
        tramite: {
           
            required: true
        },
        afps: {
           
            required: true
        },
        clinica: {
           
            required: true
        },
   
    
        fecha_inactivo: {
           
            required: true
        }
    },
    highlight: function(element) {
        $(element).closest('.form-group').addClass('has-error');
    },
    unhighlight: function(element) {
        $(element).closest('.form-group').removeClass('has-error');
    },
    errorElement: 'span',
    errorClass: 'help-block',
    errorPlacement: function(error, element) {
        if(element.parent('.input-group').length) {
            error.insertAfter(element.parent());
        } else {
            error.insertAfter(element);
        }
    }
});


// $('input').on('blur keyup', function() {
//     $("#formcliente").valid();
        
   
// });



// ======================================== MODALS EMPRESA =================================

// ======= para validar el modal de empresa ======
var validator = $('#form2').validate({
    focusCleanup: true,
    rules: {
        razon_social: {
           
            required: true
        },
        direccion: {
           
            required: true
        },
        telefono1: {
           
            required: true
        },
        departamento: {
           
            required: true
        },
        municipios: {
           
            required: true
        },
        nro_patronal: {
           
            required: true
        }
    },
    highlight: function(element) {
        $(element).closest('.form-group').addClass('has-error');
    },
    unhighlight: function(element) {
        $(element).closest('.form-group').removeClass('has-error');
    },
    errorElement: 'span',
    errorClass: 'help-block',
    errorPlacement: function(error, element) {
        if(element.parent('.input-group').length) {
            error.insertAfter(element.parent());
        } else {
            error.insertAfter(element);
        }
    }
});


// ==== para la el boton de cancelar del modal empresa 
$(".cancel").click(function() {
    validator.resetForm();
    $("#form2").find(".has-error").removeClass("has-error");
});
    

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


// ===== para guardar los datos del modal empresa en el servidor ======

$('#register').click(function(){
    console.log('am i called');
    if ($("#form2").valid()) {
        $.ajax({
            type: "POST",
            url: "/registrar_emp/",
            dataType: "json",
            data: $("#form2").serialize(),
            success: function(data) {
               console.log(data);
               // para eliminar lo seleccionado en select empresa
               $('#id_empresa option:selected').removeAttr("selected");

               // para agregar la nueva empresa registrada en el select
               $("#id_empresa").append("<option value=\""+data.pk+"\" selected='selected'>"+data.razon_socialemp+"</option>");
               
               // para limpiar los imputs del modal
               $('.modal-body').find('textarea,input').val('');

               // para cerrar el modal
               $('#myModal').modal('hide');
          }
        }); 
    } 

    
});

// ================================= end modals ==================================================0


// ======================================== MODALS CLINICA =================================

// ======= para validar el modal de clinica ======
var validator_clinica = $('#formclinica').validate({
    focusCleanup: true,
    rules: {
        razon_social: {
           
            required: true
        },
        direccion: {
           
            required: true
        },
        telefono1: {
           
            required: true
        }
    },
    highlight: function(element) {
        $(element).closest('.form-group').addClass('has-error');
    },
    unhighlight: function(element) {
        $(element).closest('.form-group').removeClass('has-error');
    },
    errorElement: 'span',
    errorClass: 'help-block',
    errorPlacement: function(error, element) {
        if(element.parent('.input-group').length) {
            error.insertAfter(element.parent());
        } else {
            error.insertAfter(element);
        }
    }
});


// ==== para la el boton de cancelar del modal clinica 
$(".cancel-clinica").click(function() {
    validator_clinica.resetForm();
    $("#formclinica").find(".has-error").removeClass("has-error");
});
    

// ===== para guardar los datos del modal clinica en el servidor ======

$('#register-clinica').click(function(){
    console.log('am i called');
    if ($("#formclinica").valid()) {
        $.ajax({
            type: "POST",
            url: "/registrar_clinic/",
            dataType: "json",
            data: $("#formclinica").serialize(),
            success: function(data) {
               console.log(data);
               // para eliminar lo seleccionado en select clinica
               $('#id_clinica option:selected').removeAttr("selected");

               // para agregar la nueva clinica registrada en el select
               $("#id_clinica").append("<option value=\""+data.pk+"\" selected='selected'>"+data.razon_socialclinica+"</option>");
               
               // para limpiar los imputs del modal
               $('.modal-body').find('textarea,input').val('');

               // para cerrar el modal
               $('#Modalclinica').modal('hide');
          }
        }); 
    } 

    
});

// ================================= end modals ==================================================0

// === creando arrays para los departamentos y sus municipos ====
var Beni = [
    {display: "Baures", value: "Baures" }, 
    {display: "Exaltacion", value: "Exaltacion" }, 
    {display: "Guayaramerin", value: "Guayaramerin" },
    {display: "Huacaraje", value: "Huacaraje" },
    {display: "Loreto", value: "Loreto" },
    {display: "Magdalena", value: "Magdalena" },
    {display: "Puerto Siles", value: "Puerto Siles" },
    {display: "Reyes", value: "Reyes" },
    {display: "Riberalta", value: "Riberalta" },
    {display: "Rurrenabaque", value: "Rurrenabaque" },
    {display: "San Andres", value: "San Andres" },
    {display: "San Borja", value: "Huacaraje" },
    {display: "San Ignacio", value: "San Ignacio" },
    {display: "San Javier", value: "San Javier" },
    {display: "San Joaquin", value: "San Joaquin" },
    {display: "San Ramon", value: "San Ramon" },
    {display: "Santa Ana", value: "Santa Ana" },
    {display: "Santa Rosa", value: "Santa Rosa" },
    {display: "Trinidad", value: "Trinidad" }];

var Chuquisaca = [
    {display: "Camargo", value: "Camargo" }, 
    {display: "Camataqui (Villa Abecia)", value: "Camataqui (Villa Abecia)" }, 
    {display: "Culpina", value: "Culpina" },
    {display: "El Villar", value: "El Villar" }, 
    {display: "Huacareta", value: "Huacareta" }, 
    {display: "Huacaya", value: "Huacaya" },
    {display: "Icla", value: "Icla" }, 
    {display: "Incahuasi", value: "Incahuasi" },
    {display: "Las Carreras", value: "Las Carreras" }, 
    {display: "Machareti", value: "Machareti" }, 
    {display: "Monteagudo", value: "Monteagudo" }, 
    {display: "Padilla", value: "Padilla" },
    {display: "Poroma", value: "Poroma" }, 
    {display: "Presto", value: "Presto" }, 
    {display: "San Lucas", value: "San Lucas" },
    {display: "Sopachuy", value: "Sopachuy" }, 
    {display: "Sucre", value: "Sucre" }, 
    {display: "Tarabuco", value: "Tarabuco" },
    {display: "Tarvita", value: "Tarvita" }, 
    {display: "Tomina", value: "Tomina" }, 
    {display: "Villa Alcala", value: "Villa Alcala" },
    {display: "Villa Azurduy", value: "Villa Azurduy" }, 
    {display: "Villa Charcas", value: "Villa Charcas" }, 
    {display: "Villa Serrano", value: "Villa Serrano" },
    {display: "Villa Vaca Guzman (Muyupampa)", value: "Villa Vaca Guzman (Muyupampa)" }, 
    {display: "Villa Zudañez", value: "Villa Zudañez" },
    {display: "Yamparaez", value: "Yamparaez" }, 
    {display: "Yotala", value: "Yotala" }];

var Cochabamba = [
    {display:"Aiquile", value: "Aiquile"},
    {display:"Alalay", value: "Alalay"},
    {display:"Anzaldo", value: "Anzaldo"},
    {display:"Arani", value: "Arani"},
    {display:"Arbieto", value: "Arbieto"},
    {display:"Arque", value: "Arque"},
    {display:"Bolivar", value: "Bolivar"},
    {display:"Capinota", value: "Capinota"},
    {display:"Chimore", value: "Chimore"},
    {display:"Cliza", value: "Cliza"},
    {display:"Cocapata", value: "Cocapata"},
    {display:"Cochabamba", value: "Cochabamba"},
    {display:"Colcapirhua", value: "Colcapirhua"},
    {display:"Colomi", value: "Colomi"},
    {display:"Cuchumuela (Villa Gualberto Villarroel)", value: "Cuchumuela (Villa Gualberto Villarroel)"},
    {display:"Entre Rios (Bulo Bulo)", value: "Entre Rios (Bulo Bulo)"},
    {display:"Independencia", value: "Independencia"},
    {display:"Mizque", value: "Mizque"},
    {display:"Morochata", value: "Morochata"},
    {display:"Omereque", value: "Omereque"},
    {display:"Pasorapa", value: "Pasorapa"},
    {display:"Pocona", value: "Pocona"},
    {display:"Pojo", value: ""},
    {display:"Puerto Villarroel", value: "Puerto Villarroel"},
    {display:"Punata", value: "Punata"},
    {display:"Quillacollo", value: "Quillacollo"},
    {display:"Sacaba", value: "Sacaba"},
    {display:"Sacabamba", value: "Sacabamba"},
    {display:"San Benito", value: "San Benito"},
    {display:"Santivañez", value: "Santivañez"},
    {display:"Shinahota", value: "Shinahota"},
    {display:"Sicaya", value: "Sicaya"},
    {display:"Sipe Sipe", value: "Sipe Sipe"},
    {display:"Tacachi", value: "Tacachi"},
    {display:"Tacopaya", value: "Tacopaya"},
    {display:"Tapacari", value: "Tapacari"},
    {display:"Tarata", value: "Tarata"},
    {display:"Tiquipaya", value: "Tiquipaya"},
    {display:"Tiraque", value: "Tiraque"},
    {display:"Toco", value: "Toco"},
    {display:"Tolata", value: "Tolata"},
    {display:"Totora", value: "Totora"},
    {display:"Vacas", value: "Vacas"},
    {display:"Vila Vila", value: "Vila Vila"},
    {display:"Villa Rivero", value: "Villa Rivero"},
    {display:"Villa Tunari", value: "Villa Tunari"},
    {display:"Vinto", value: "Vinto"}];

var La_Paz = [
    {display:"Achacachi", value: "Achacachi"},
    {display:"Achocalla", value: "Achocalla"},
    {display:"Alto Beni", value: "Alto Beni"},
    {display:"Ancoraimes", value: "Ancoraimes"},
    {display:"Apolo", value: "Apolo"},
    {display:"Aucapata", value: "Aucapata"},
    {display:"Ayata", value: "Ayata"},
    {display:"Ayo Ayo", value: "Ayo Ayo"},
    {display:"Batallas", value: "Batallas"},
    {display:"Cairoma", value: "Cairoma"},
    {display:"Cajuata", value: "Cajuata"},
    {display:"Calacoto", value: "Calacoto"},
    {display:"Calamarca", value: "Calamarca"},
    {display:"Caquiaviri", value: "Caquiaviri"},
    {display:"Caranavi", value: "Caranavi"},
    {display:"Catacora", value: "Catacora"},
    {display:"Chacarilla", value: "Chacarilla"},
    {display:"Charaña", value: "Charaña"},
    {display:"Chulumani", value: "Chulumani"},
    {display:"Chuma", value: "Chuma"},
    {display:"Collana", value: "Collana"},
    {display:"Colquencha", value: "Colquencha"},
    {display:"Colquiri", value: "Colquiri"},
    {display:"Comanche", value: "Comanche"},
    {display:"Combaya", value: "Combaya"},
    {display:"Copacabana", value: "Copacabana"},
    {display:"Coripata", value: "Coripata"},
    {display:"Coro Coro", value: "Coro Coro"},
    {display:"Coroico", value: "Coroico"},
    {display:"Curva", value: "Curva"},
    {display:"Desaguadero", value: "Desaguadero"},
    {display:"El Alto", value: "El Alto"},
    {display:"Escoma", value: "Escoma"},
    {display:">Gral. Juan Jose Perez (Charazani)", value: "Gral. Juan Jose Perez (Charazani)"},
    {display:"Guanay", value: "Guanay"},
    {display:"Guaqui", value: "Guaqui"},
    {display:"Huarina ", value: "Huarina"},
    {display:"Humanata", value: "Humanata"},
    {display:"Ichoca", value: "Ichoca"},
    {display:"Inquisivi", value: "InquisiviIrupana"},
    {display:"Irupana", value: "Irupana"},
    {display:"Ixiamas", value: "Ixiamas"},
    {display:"Jesus de Machaca", value: "Jesus de Machaca"},
    {display:"La Asunta", value: "La Asunta"},
    {display:"La Paz", value: "La Paz"},
    {display:"Laja", value: "Laja"},
    {display:"Licoma Pampa", value: "Licoma Pampa"},
    {display:"Luribay", value: "Luribay"},
    {display:"Malla", value: "Malla"},
    {display:"Mapiri", value: "Mapiri"},
    {display:"Mecapaca", value: "Mecapaca"},
    {display:"Mocomoco", value: "Mocomoco"},
    {display:"Nazacara de Pacajes", value: "Nazacara de Pacajes"},
    {display:"Palca", value: "Palca"},
    {display:"Palos Blancos", value: "Palos Blancos"},
    {display:"Papel Pampa", value: "Papel Pampa"},
    {display:"Patacamaya", value: "Patacamaya"},
    {display:"Pelechuco", value: "Pelechuco"},
    {display:"Pucarani", value: "Pucarani"},
    {display:"Puerto Acosta", value: "Puerto Acosta"},
    {display:"Puerto Carabuco", value: "Puerto Carabuco"},
    {display:"Puerto Perez", value: "Puerto Perez"},
    {display:"Quiabaya", value: "Quiabaya"},
    {display:"Quime", value: "Quime"},
    {display:"San Andres de Machaca", value: "San Andres de Machaca"},
    {display:"San Buenaventura", value: "San Buenaventura"},
    {display:"San Pedro de Curahuara", value: "San Pedro de Curahuara"},
    {display:"San Pedro de Tiquina", value: "San Pedro de Tiquina"},
    {display:"Santiago de Callapa", value: "Santiago de Callapa"},
    {display:"Santiago de Huata", value: "Santiago de Huata"},
    {display:"Santiago de Machaca", value: "Santiago de Machaca"},
    {display:"Sapahaqui", value: "Sapahaqui"},
    {display:"Sica Sica", value: "Sica Sica"},
    {display:"Sorata", value: "Sorata"},
    {display:"Tacacoma", value: "Tacacoma"},
    {display:"Taraco", value: "Taraco"},
    {display:"Teoponte", value: "Teoponte"},
    {display:"Tiahuanacu", value: "Tiahuanacu"},
    {display:"Tipuani", value: "Tipuani"},
    {display:"Tito Yupanqui", value: "Tito Yupanqui"},
    {display:"Umala", value: "Umala"},
    {display:"Viacha", value: "Viacha"},
    {display:"Waldo Ballivian", value: "Waldo Ballivian"},
    {display:"Yaco", value: "Yaco"},
    {display:"Yanacachi", value: "Yanacachi"}];

var Oruro = [
    {display:"Andamarca", value:"Andamarca"},
    {display:"Antequera", value:"Antequera"},
    {display:"Belen de Andamarca", value:"Belen de Andamarca"},
    {display:"Caracollo", value:"Caracollo"},
    {display:"Carangas", value:"Carangas"},
    {display:"Challapata", value:"Challapata"},
    {display:"Chipaya", value:"Chipaya"},
    {display:"Choquecota", value:"Choquecota"},
    {display:"Coipasa", value:"Coipasa"},
    {display:"Corque", value:"Corque"},
    {display:"Cruz de Machacamarca", value:"Cruz de Machacamarca"},
    {display:"Curahuara de Carangas", value:"Curahuara de Carangas"},
    {display:"El Choro", value:"El Choro"},
    {display:"Escara ", value:"Escara"},
    {display:"Esmeralda", value:"Esmeralda"},
    {display:"Eucaliptus", value:"Eucaliptus"},
    {display:"Huachacalla", value:"Huachacalla"},
    {display:"La Rivera", value:"La Rivera"},
    {display:"Machacamarca", value:"Machacamarca"},
    {display:"Oruro", value:"Oruro"},
    {display:"Pampa Aullagas", value:"Pampa Aullagas"},
    {display:"Pazña", value:"Pazña"},
    {display:"Sabaya", value:"Sabaya"},
    {display:"Salinas de Garci Mendoza", value:"Salinas de Garci Mendoza"},
    {display:"Santiago de Huari", value:"Santiago de Huari"},
    {display:"Santiago de Huayllamarca", value:"Santiago de Huayllamarca"},
    {display:"Santuario de Quillacas", value:"Santuario de Quillacas"},
    {display:"Soracachi (Paria)", value:"Soracachi (Paria)"},
    {display:"Todos Santos", value:"Todos Santos"},
    {display:"Toledo", value:"Toledo"},
    {display:"Totora", value:"Totora"},
    {display:"Turco", value:"Turco"},
    {display:"Villa Huanuni", value:"Villa Huanuni"},
    {display:"Villa Poopo", value:"Villa Poopo"},
    {display:"Yunguyo del Litoral", value:"Yunguyo del Litoral"}];

var Pando = [
  {display: "Bella Flor", value: "Bella Flor"},
  {display: "Blanca Flor (San Lorenzo)", value: "Blanca Flor (San Lorenzo)"},
  {display: "Bolpebra", value: "Bolpebra"},
  {display: "Cobija", value: "Cobija"},
  {display: "El Sena", value: "El Sena"},
  {display: "Filadelfia", value: "Filadelfia"},
  {display: "Humaita (Ingavi)", value: "Humaita (Ingavi)"},
  {display: "Nueva Esperanza", value: "Nueva Esperanza"},
  {display: "Porvenir", value: "Porvenir"},
  {display: "Puerto Gonzalo Moreno", value: "Puerto Gonzalo Moreno"},
  {display: "Puerto Rico", value: "Puerto Rico"},
  {display: "San Pedro", value: "San Pedro"},
  {display: "Santa Rosa del Abuna", value: "Santa Rosa del Abuna"},
  {display: "Santos Mercado (Reserva)", value: "Santos Mercado (Reserva)"},
  {display: "Villa Nueva (Loma Alta)", value: "Villa Nueva (Loma Alta)"}];

var Potosi = [
    {display:"Acasio", value: "Acasio"},
    {display:"Arampampa", value: "Arampampa"},
    {display:"Atocha", value: "Atocha"},
    {display:"Belen de Urmiri", value: "Belen de Urmiri"},
    {display:"Betanzos", value: "Betanzos"},
    {display:"Caiza D", value: "Caiza D"},
    {display:"Caripuyo", value: "Caripuyo"},
    {display:"Chaqui", value: "Chaqui"},
    {display:"Chayanta", value: "Chayanta"},
    {display:"Chuquihuta Ayllu Jucumani", value: "Chuquihuta Ayllu Jucumani"},
    {display:"Ckochas", value: "Ckochas"},
    {display:"Colcha K", value: "Colcha K"},
    {display:"Colquechaca", value: "Colquechaca"},
    {display:"Cotagaita", value: "Cotagaita"},
    {display:"Llallagua", value: "Llallagua"},
    {display:"Llica", value: "Llica"},
    {display:"Mojinete", value: "Mojinete"},
    {display:"Ocuri", value: "Ocuri"},
    {display:"Pocoata", value: "Pocoata"},
    {display:"Porco", value: "Porco"},
    {display:"Potosi", value: "Potosi"},
    {display:"Puna", value: "Puna"},
    {display:"Ravelo", value: "Ravelo"},
    {display:"Sacaca", value: "Sacaca"},
    {display:"San Agustin", value: "San Agustin"},
    {display:"San Antonio de Esmoruco", value: "San Antonio de Esmoruco"},
    {display:"San Pablo de Lipez", value: "San Pablo de Lipez"},
    {display:"San Pedro de Buena Vista", value: "San Pedro de Buena Vista"},
    {display:"San Pedro de Quemes", value: "San Pedro de Quemes"},
    {display:"Tacobamba", value: ""},
    {display:"Tahua", value: "Tahua"},
    {display:"Tinguipaya", value: "Tinguipaya"},
    {display:"Tomave", value: "Tomave"},
    {display:"Toro Toro", value: "Toro Toro"},
    {display:"Tupiza", value: "Tupiza"},
    {display:"Uncia", value: "Uncia"},
    {display:"Uyuni", value: "Uyuni"},
    {display:"Villa de Yocalla", value: "Villa de Yocalla"},
    {display:"Villazon", value: "Villazon"},
    {display:"Vitichi", value: "Vitichi"}];

var Santa_Cruz = [
    {display: "Ascencion de Guarayos", value: "Ascencion de Guarayos"},
    {display: "Boyuibe", value: "Boyuibe"},
    {display: "Buena Vista", value: "Buena Vista"},
    {display: "Cabezas", value: "Cabezas"},
    {display: "Camiri", value: "Camiri"},
    {display: "Carmen Rivero Torres", value: "Carmen Rivero Torres"},
    {display: "Charagua", value: "Charagua"},
    {display: "Colpa Belgica", value: "Colpa Belgica"},
    {display: "Comarapa", value: "Comarapa"},
    {display: "Concepcion", value: "Concepcion"},
    {display: "Cotoca", value: "Cotoca"},
    {display: "Cuatro Cañadas", value: "Cuatro Cañadas"},
    {display: "Cuevo", value: "Cuevo"},
    {display: "El Puente", value: "El Puente"},
    {display: "El Torno", value: "El Torno"},
    {display: "El Trigal", value: "El Trigal"},
    {display: "Fernandez Alonso", value: "Fernandez Alonso"},
    {display: "Gral. Saavedra", value: "Gral. Saavedra"},
    {display: "Gutierrez", value: "Gutierrez"},
    {display: "La Guardia", value: "La Guardia"},
    {display: "Lagunillas", value: "Lagunillas"},
    {display: "Mairana", value: "Mairana"},
    {display: "Mineros", value: "Mineros"},
    {display: "Montero", value: "Montero"},
    {display: "Moro Moro", value: "Moro Moro"},
    {display: "Okinawa", value: "Okinawa"},
    {display: "Pailon", value: "Pailon"},
    {display: "Pampa Grande", value: "Pampa Grande"},
    {display: "Porongo (Ayacucho)", value: "Porongo (Ayacucho)"},
    {display: "Portachuelo", value: "Portachuelo"},
    {display: "Postrervalle", value: "Postrervalle"},
    {display: "Pucara", value: "Pucara"},
    {display: "Puerto Quijarro", value: "Puerto Quijarro"},
    {display: "Puerto Suarez", value: "Puerto Suarez"},
    {display: "Quirusillas", value: "Quirusillas"},
    {display: "Robore", value: "Robore"},
    {display: "Saipina", value: "Saipina"},
    {display: "Samaipata", value: "Samaipata"},
    {display: "San Antonio de Lomerio", value: "San Antonio de Lomerio"},
    {display: "San Carlos", value: "San Carlos"},
    {display: "San Ignacio", value: "San Ignacio"},
    {display: "San Javier", value: "San Javier"},
    {display: "San Jose", value: "San Jose"},
    {display: "San Juan", value: "San Juan"},
    {display: "San Julian", value: "San Julian"},
    {display: "San Matias", value: "San Matias"},
    {display: "San Miguel", value: "San Miguel"},
    {display: "San Pedro", value: "San Pedro"},
    {display: "San Rafael", value: "San Rafael"},
    {display: "San Ramon", value: "San Ramon"},
    {display: "Santa Cruz de la Sierra", value: "Santa Cruz de la Sierra"},
    {display: "Santa Rosa del Sara", value: ""},
    {display: "Urubicha", value: "Urubicha"},
    {display: "Vallegrande", value: "Vallegrande"},
    {display: "Warnes", value: "Warnes"},
    {display: "Yapacani", value: "Yapacani"}];

var Tarija = [
    {display:"Bermejo", value:"Bermejo"},
    {display:"Carapari", value:"Carapari"},
    {display:"El Puente", value:"El Puente"},
    {display:"Padcaya", value:"Padcaya"},
    {display:"San Lorenzo", value:"San Lorenzo"},
    {display:"Tarija", value:"Tarija"},
    {display:"Uriondo (CONCEPCION)", value:"Uriondo (CONCEPCION)"},
    {display:"Villamontes", value:"Villamontes"},
    {display:"Yacuiba", value:"Yacuiba"},
    {display:"Yunchara", value:"Yunchara"}];


// === para accion del departamendo cuando se hace un cambio en el select
$("#parent_selection").change(function() {
        var parent = $(this).val(); //get option value from parent 

        switch(parent){ //using switch compare selected option and populate child
              case 'Beni':
                list(Beni);
                break;
              case 'Chuquisaca':
                list(Chuquisaca);
                break;              
              case 'Cochabamba':
                list(Cochabamba);
                break;  
              case 'La Paz':
                list(La_Paz);
                break;
                case 'Oruro':
                list(Oruro);
                break;
                case 'Pando':
                list(Pando);
                break;
                case 'Potosi':
                list(Potosi);
                break;
                case 'Santa Cruz':
                list(Santa_Cruz);
                break;  
                case 'Tarija':
                list(Tarija);
                break;
            default: //default child option is blank
                $("#child_selection").html('');  
                break;
  }
  });
 
  // funcion para rederizar sus municipos de cada departamendo del array 
  function list(array_list){
       // limpiando municipio
      $("#child_selection").html(""); 
      $(array_list).each(function (i) { //populate child options 
 

      $("#child_selection").append("<option value=\""+array_list[i].value+"\">"+array_list[i].display+"</option>");
      $('#child_selection');

      });
  }