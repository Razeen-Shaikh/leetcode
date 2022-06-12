/**
 * 1. Two Sum
 * @param {number[]} numbs
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (numbs, target) {
	let indices = [];
	numbs.forEach((num, index) => {
		for (let i = 0; i < numbs.length; i++) {
			if (!(i === index)) {
				if (num + numbs[i] === target) {
					indices = [i, index];
				}
			}
		}
	});
	return indices;
};
