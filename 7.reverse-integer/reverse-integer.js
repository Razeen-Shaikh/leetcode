/**
 * 7. Reverse Integer
 * @param {number} x
 * @return {number}
 */
var reverse = function (x) {
	let temp = x,
		rev = 0;
	while (temp !== 0) {
		rev = rev * 10 + (temp % 10);
		temp = parseInt(temp / 10);
	}
	if (rev >= -Math.pow(2, 31) && rev <= Math.pow(2, 31) - 1) return rev;
	else return 0;
};
