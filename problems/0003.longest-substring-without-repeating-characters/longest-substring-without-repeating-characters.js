/**
 * Given a string `s`, find the length of the longest substring
 * without repeating characters.
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
	if (!s) {
		return 0;
	}
	let start = 0;
	let end = 0;
	let max = 0;
	let uniques = new Set();
	while (end < s.length) {
		if (!uniques.has(s[end])) {
			uniques.add(s[end]);
			end++;
			max = Math.max(max, uniques.size);
		} else {
			uniques.delete(s[start]);
			start++;
		}
	}
	return max;
};
