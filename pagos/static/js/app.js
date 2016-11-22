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
function change_button(total) {
	$('#btn-submit').html('Donate $' + total);
}
var form_valid = false;
$('#form-group-card_type').append('<span id="card-label"></span>');
$(document).ready(function () {
	$(".btn-group > .btn").click(function(){
		$(this).blur();
		$('.btn-group > .btn').removeClass("active");
		$(this).addClass("active").siblings().removeClass("active");
	});
	$('#id_card_type').hide();
	$('#btn-submit').prop('disabled', true);
	$('#formulario').on('submit', function (e) {
		$('#btn-submit').prop('disabled', true);
		$('#id_total').val(parseFloat($('#id_total').val()).toFixed(2));
		if(form_valid==false){
			e.preventDefault();
			alert("Captcha error")
			$('#btn-submit').prop('disabled', false);
		}
		if(!$('#id_card_type').val()){
			e.preventDefault();
			alert("Please check your card number. We couldn't find the cartype in our database.")
			$('#btn-submit').prop('disabled', false);
		}
	});
	$('#id_total').on('keyup', function () {
		change_button($(this).val());
	});
});
var onloadCallback = function() {
	grecaptcha.render('captcha-space', {
		'sitekey' : '6LexSAkUAAAAAIYsk4MMEFL_wWJtw-TADuwMxMC1',
		'callback': function () {
			$('#btn-submit').prop('disabled', false);
			form_valid = true;
		}
	});
};