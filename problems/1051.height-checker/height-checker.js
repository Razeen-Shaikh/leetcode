/**
 * 1051. Height Checker
 * @param {number[]} heights
 * @return {number}
 */
var heightChecker = function (heights) {
	let expected = heights.slice().sort((a, b) => a - b),
		count = 0;
	heights.forEach((height, index) => {
		if (height !== expected[index]) count++;
	});
	return count;
};
