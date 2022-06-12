/**
 * 283. Move Zeroes
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function (nums) {
	let i = 0;
	while (nums.includes(0) && i < nums.length) {
		nums.splice(nums.indexOf(0), 1);
		nums[nums.length] = 0;
		i++;
	}
};
