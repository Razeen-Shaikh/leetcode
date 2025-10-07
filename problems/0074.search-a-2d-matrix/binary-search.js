/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function(matrix, target) {
    let m = matrix.length;
    let n = matrix[0].length;
    let low = 0, high = m * n - 1;

    while (low <= high) {
        let mid = Math.floor((low + high) / 2);
        let row = Math.floor(mid / n);
        let col = mid % n;
        let midVal = matrix[row][col];

        if (midVal === target) return true;
        else if (midVal < target) low = mid + 1;
        else high = mid - 1;
    }

    return false;
};