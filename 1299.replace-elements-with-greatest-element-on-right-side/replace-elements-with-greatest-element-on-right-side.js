/**
 * 1299. Replace Elements with Greatest Element on Right Side
 * @param {number[]} arr
 * @return {number[]}
 */
var replaceElements = function (arr) {
	let maxValue = arr[arr.length - 1];
	for (let i = arr.length - 1; i >= 0; i--) {
		if (arr[i] > maxValue) {
			let temp = arr[i];
			arr[i] = maxValue;
			maxValue = temp;
		} else {
			arr[i] = maxValue;
		}
	}
	arr[arr.length - 1] = -1;
	return arr;
};
