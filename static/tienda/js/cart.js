var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
		var productId = this.dataset.product
		var action = this.dataset.action
		console.log('productId:', productId, 'Action:', action)
		console.log('USER:', user)

		if (user == 'AnonymousUser'){
			addCookieItem(productId, action)			
		}else{
			updateUserOrder(productId, action)
		}
	})
}


var csrftoken_2 = document.getElementsByTagName("input")[0].value

function updateUserOrder(productId, action){
	console.log('El usuario está registrado, cargando datos...')
	console.log(csrftoken_2)

	// url donde se enviara al backend la info del producto
	var url = 'actualizado'

	// data que se enviará al backend
	fetch(url, {
				method:'POST',
				headers: {
					'Content-Type':'application/json',
					'X-CSRFToken':csrftoken_2,
				}, 
				body:JSON.stringify({
					'productId':productId, 
					'action':action
				}
			)
		}
	)
	.then((response) => {
			return response.json();
		}
	)
	.then((data) => {
			location.reload()
			console.log(data)
		}
	);
}

function addCookieItem(productId, action){
	console.log('User is not authenticated')

	if (action == 'add'){
		if (cart[productId] == undefined){
		cart[productId] = {'quantity':1}

		}else{
			cart[productId]['quantity'] += 1
		}
	}

	if (action == 'remove'){
		cart[productId]['quantity'] -= 1

		if (cart[productId]['quantity'] <= 0){
			console.log('Item should be deleted')
			delete cart[productId];
		}
	}
	console.log('CART:', cart)
	document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
	
	location.reload()
}