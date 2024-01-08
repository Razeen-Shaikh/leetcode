/**
 * 217. Contains Duplicate
 * @param {number[]} numb
 * @return {boolean}
 */
var containsDuplicate = function (numb) {
	return numb.some((num, index) => numb.indexOf(num) !== index);
};
