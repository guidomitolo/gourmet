var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
		var productId = this.dataset.product
		var action = this.dataset.action
		console.log('productId:', productId, 'Action:', action)
		console.log('USER:', user)

		if (user == 'AnonymousUser'){
			console.log('User is not authenticated')
			
		}else{
			updateUserOrder(productId, action)
		}
	})
}


var csrftoken_2 = document.getElementsByTagName("input")[0].value

function updateUserOrder(productId, action){
	console.log('User is authenticated, sending data...')
	console.log(csrftoken_2)

	var url = 'actualizado'

	fetch(url, {
		method:'POST',
		headers:{
			'Content-Type':'application/json',
			'X-CSRFToken':csrftoken_2,
		}, 
		body:JSON.stringify({'productId':productId, 'action':action})
	})
	.then((response) => {
		return response.json();
	})
	.then((data) => {
		location.reload()
	});
}