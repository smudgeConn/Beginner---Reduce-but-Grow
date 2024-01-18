let str = "krishan"

function reverseLetter(str) {
	res = '';
	for (let i = 0; i < str.length; i++) {
		if (str.charCodeAt(str[i]) > 96 && str.charCodeAt(str[i]) < 123) {
			res += str[i];
		}
	}
	return res.split("").reverse().join("");
}

console.log(reverseLetter(str))

