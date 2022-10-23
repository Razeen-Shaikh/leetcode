/**
 * 977. Squares of a Sorted Array
 * @param {number[]} numbs
 * @return {number[]}
 */
var sortedSquares = function (numbs) {
	numbs.forEach((num, index) => {
		numbs[index] = num * num;
	});

	return numbs.sort((a, b) => a - b);
};
