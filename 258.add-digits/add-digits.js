/**
 * 258. Add Digits
 * @param {number} num
 * @return {number}
 */
var addDigits = function (num) {
	return num - 9 * parseInt((num - 1) / 9);
};
