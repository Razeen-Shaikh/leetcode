/**
 * 26. Remove Duplicates from Sorted Array
 * @param {number[]} numb
 * @return {number}
 */
var removeDuplicates = function (numb) {
	for (let i = numb.length; i--; ) {
		if (numb.indexOf(numb[i]) !== i) {
			numb.splice(i, 1);
		}
	}
};
