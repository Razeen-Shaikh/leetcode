/**
 * 74. Search a 2D Matrix
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function (matrix, target) {
	return matrix.some((m) => m.includes(target));
};
