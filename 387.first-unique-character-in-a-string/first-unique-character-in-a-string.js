/**
 * 387. First Unique Character in a String
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function (s) {
	let t = s.split("");
	var elms = t.filter((c, index) => t.indexOf(c) !== index);

	return t.indexOf(t.filter((c) => !elms.includes(c))[0]);
};
