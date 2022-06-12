/**
 * 1089. Duplicate Zeros
 * @param {number[]} arr
 * @return {void} Do not return anything, modify arr in-place instead.
 */
var duplicateZeros = function (arr) {
	for (let i = 0; i < arr.length - 1; i++) {
		if (arr[i] === 0) {
			let prev = arr[i + 1];
			for (let j = i + 2; j < arr.length; j++) {
				let temp = arr[j];
				arr[j] = prev;
				prev = temp;
			}
			arr[++i] = 0;
		}
	}
};
