/**
 * 242. Valid Anagram
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
	let str1 = s.split("").sort().join("").toLowerCase();
	let str2 = t.split("").sort().join("").toLowerCase();

	return str1 === str2;
};
