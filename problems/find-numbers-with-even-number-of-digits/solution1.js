/**
 * 1295. Find Numbers with Even Number of Digits
 * @param {number[]} nums
 * @return {number}
 */
var findNumbers = function (nums) {
	var even_count = 0;
	nums.forEach((num) => {
		var temp = num.toString();
		if (temp.length % 2 === 0) {
			even_count++;
		}
	});
	return even_count;
};
