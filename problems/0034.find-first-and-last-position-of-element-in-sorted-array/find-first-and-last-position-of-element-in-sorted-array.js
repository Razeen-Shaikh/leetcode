/**
 * 34. Find First and Last Position of Element in Sorted Array
 * @param {number[]} numbs
 * @param {number} target
 * @return {number[]}
 */
var searchRange = function (numbs, target) {
	if (!numbs.includes(target)) return [-1, -1];
	return [
		numbs.indexOf(target),
		numbs.length - 1 - numbs.reverse().indexOf(target),
	];
};
