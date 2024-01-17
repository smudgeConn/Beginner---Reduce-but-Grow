let x = [1, 2, 3]
function grow(x) {
	let product = 1;
	for (let i = 0; i < x.length; i++) {
		product = product * x[i]
	}
	return product
}

console.log(grow(x))
