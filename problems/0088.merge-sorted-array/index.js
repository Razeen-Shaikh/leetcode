/**
 * 88. Merge Sorted Array
 * @param {number[]} numb1
 * @param {number} m
 * @param {number[]} numb2
 * @param {number} n
 * @return {void} Do not return anything, modify numb1 in-place instead.
 */
var merge = function (numb1, m, numb2, n) {
	numb1.splice(m, n, ...numb2);
	numb1.sort((a, b) => a - b);
};
