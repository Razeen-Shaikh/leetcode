/**
 * 136. Single Number
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function (nums) {
	let arr = nums.filter((num, index) => nums.indexOf(num) !== index),
		sig = 0;
	nums.forEach((num) => {
		if (!arr.includes(num)) sig = num;
	});
	return sig;
};
