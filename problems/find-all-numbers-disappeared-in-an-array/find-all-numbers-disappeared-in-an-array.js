/**
 * 448. Find All Numbers Disappeared in an Array
 * @param {number[]} numb
 * @return {number[]}
 */
var findDisappearedNumbers = function (numb) {
	var n = numb.length,
		result = [];
	if (n >= 1 && n <= 10 ** 5) {
		numb.forEach((num, index) => {
			if (num >= 1 && num <= n) {
				if (!numb.includes(index + 1)) result.push(index + 1);
			}
		});
	}
	return result;
};
