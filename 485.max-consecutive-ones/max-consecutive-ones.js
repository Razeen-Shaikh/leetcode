/**
 * 485. Max Consecutive Ones
 * @param {number[]} numbs
 * @return {number}
 */
var findMaxConsecutiveOnes = function (numbs) {
	var arrCounts = [],
		count = 0;
	numbs.forEach((num, index) => {
		if (num === 0) {
			arrCounts.push(count);
			count = 0;
		} else count++;
		if (index === numbs.length - 1) arrCounts.push(count);
	});
	return Math.max(...arrCounts);
};
