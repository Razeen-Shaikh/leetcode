/**
 * 540. Single Element in a Sorted Array
 * @param {number[]} numbs
 * @return {number}
 */
var singleNonDuplicate = function (numbs) {
	var elms = numbs.filter((num, index) => numbs.indexOf(num) !== index);

	return numbs.filter((num) => !elms.includes(num));
};
