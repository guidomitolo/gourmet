var form = document.getElementById('form')


// var csrftoken_2 = document.getElementsByTagName("input")[0].value
// var total = '{{orden.total_orden_precio}}'

form.addEventListener('submit', function(e){
	// prevent submition of the form but hide button
	e.preventDefault()
	document.getElementById('form-button').classList.add("hidden");
	document.getElementById('payment-info').classList.remove("hidden");
})

document.getElementById('make-payment').addEventListener('click', function(e){
		submitFormData()
})

function submitFormData(){
	console.log('Payment button clicked')

	var userFormData = {
		'nombre':null,
		'apellido': null,
		'email':null,
		'total': total,
	}

	var despachoInfo = {
		'calle':null,
		'altura':null,
		'municipio':null,
		'localidad':null,
	}

	despachoInfo.calle = form.calle.value
	despachoInfo.altura = form.altura.value
	despachoInfo.municipio = form.municipio.value
	despachoInfo.localidad = form.localidad.value

	if (user == 'AnonymousUser'){
		userFormData.nombre = form.first_name.value
		userFormData.apellido = form.last_name.value
		userFormData.email = form.email.value
	}

	console.log(user)
	console.log('Despacho Info:', despachoInfo)
	console.log('Usuario Info:', userFormData)

	var url = "procesando"
	fetch(url, {
		method:'POST',
		headers:{
			'Content-Type':'applicaiton/json',
			'X-CSRFToken':csrftoken,
		}, 
		body:JSON.stringify({
			'form': userFormData,
			'despacho':despachoInfo
		}
		),
	})
	.then((response) => response.json())
	.then((data) => {
		console.log('¡Éxito!', data);
		alert('¡Transacción Completada!');  

		cart = {}
		document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"

		window.location.href = volver

		})
}

// hide user info form if user is not logged in
// if (user != "AnonymousUser"){
// 	document.getElementById("user-info").innerHTML = ""
// }