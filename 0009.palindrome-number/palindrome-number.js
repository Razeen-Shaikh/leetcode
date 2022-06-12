/**
 * 9. Palindrome Number
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function (x) {
	if (x.toString() === x.toString().split("").reverse().join("")) {
		return true;
	}
	return false;
};
