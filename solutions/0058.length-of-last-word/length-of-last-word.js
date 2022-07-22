/**
 * 58. Length of Last Word
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function (s) {
	let str = s.trim().split(" ");
	str.forEach((st, index) => {
		if (st === "") {
			str.splice(index, 1);
		}
	});
	return str[str.length - 1].length;
};
