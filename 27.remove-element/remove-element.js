/**
 * 27. Remove Element
 * @param {number[]} numb
 * @param {number} val
 * @return {number}
 */
var removeElement = function (numb, val) {
	for (let i = numb.length; i--; ) {
		if (numb[i] === val) {
			numb.splice(i, 1);
		}
	}
};
