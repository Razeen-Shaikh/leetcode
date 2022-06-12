/**
 * 350. Intersection of Two Arrays II
 * @param {number[]} numb1
 * @param {number[]} numb2
 * @return {number[]}
 */
var intersect = function (numb1, numb2) {
	return numb2.filter((num, index) => {
		if (numb1.includes(num)) {
			numb1.splice(numb1.indexOf(num), 1);
			return [num];
		}
	});
};
