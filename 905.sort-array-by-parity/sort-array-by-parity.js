/**
 * 905. Sort Array By Parity
 * @param {number[]} numbs
 * @return {number[]}
 */
var sortArrayByParity = function (numbs) {
	let result = { even: [], odd: [] };
	numbs.forEach((num, index) => {
		if (num % 2 === 0) result["even"].push(num);
		else result["odd"].push(num);
	});
	return result["even"].concat(result["odd"]);
};
