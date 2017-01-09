var form_valid = false;

// Escribe la cantidad en el campo de donación
function pick_total(total) {
	if(total){
		$('#id_total').val(total);
		change_button(total);
	}
	else{
		$('#id_total').val('');
		change_button('');
	}
}

// Agrega la cantidad de donación al botón submit
function change_button(total) {
	$('#btn-submit').html('Donate $' + total);
}

$('#form-group-card_type').append('<span id="card-label"></span>');

var onloadCallback = function() {
	grecaptcha.render('captcha-space', {
		'sitekey' : '6LexSAkUAAAAAIYsk4MMEFL_wWJtw-TADuwMxMC1',
		'callback': function () {
			$('#btn-submit').prop('disabled', false);
			form_valid = true;
		}
	});
};

$(document).ready(function () {
	$('#id_card_type').hide();
	
	// Deshabilita el botón para enviar
	$('#btn-submit').prop('disabled', true);
	
	// Para que los botones de donación funcionen como radios
	$(".btn-group > .btn").click(function(){
		$(this).blur();
		$('.btn-group > .btn').removeClass("active");
		$(this).addClass("active").siblings().removeClass("active");
	});
	
	$('#id_total').on('keyup', function () {
		change_button($(this).val());
	});
	
	$('#formulario').on('submit', function (e) {
		$('#btn-submit').prop('disabled', true);
		$('#id_total').val(parseFloat($('#id_total').val()).toFixed(2));
		
		if(form_valid==false){
			e.preventDefault();
			alert("Captcha error")
			$('#btn-submit').prop('disabled', false);
		}
		// Cuando no se encuentra el tipo de tarjeta
		if(!$('#id_card_type').val()){
			e.preventDefault();
			alert("Please check your card number. We couldn't find the cartype in our database.")
			$('#btn-submit').prop('disabled', false);
		}
	});
});
