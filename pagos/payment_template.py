credit_card ={
    "type": "visa",
    "number": "",
    "expire_month": "",
    "expire_year": "",
    "cvv2": "",
    "first_name": "",
    "last_name": ""
}

def form_parametros(tarjeta, cantidad):
	parametros = {
	  "intent": "sale",
	  "payer": {
	    "payment_method": "credit_card",
	    "funding_instruments": [{
	      "credit_card": tarjeta }]},
	  "transactions": [{
	    "amount": {
	      "total": cantidad,
	      "currency": "USD" },
	    "description": "This is the payment transaction description." }
	    ]}
	return parametros