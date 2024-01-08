/**
 * 414. Third Maximum Number
 * @param {number[]} numbs
 * @return {number}
 */
var thirdMax = function (numbs) {
	numbs = numbs.filter((num, index) => numbs.indexOf(num) === index);
	if (numbs.length < 3) return Math.max(...numbs);
	else {
		numbs.sort((a, b) => b - a);
		return numbs[2];
	}
};
