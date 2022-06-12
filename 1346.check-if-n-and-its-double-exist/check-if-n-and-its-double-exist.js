/**
 * 1346. Check If N and Its Double Exist
 * @param {number[]} arr
 * @return {boolean}
 */
var checkIfExist = function (arr) {
	for (let i = 0; i < arr.length; i++) {
		let n = arr[i];
		for (let j = 0; j < arr.length; j++) {
			let m = arr[j];
			if (n === 2 * m && j !== i) {
				return true;
			}
		}
	}
	return false;
};
