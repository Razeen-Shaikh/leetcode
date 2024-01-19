/**
 * 941. Valid Mountain Array
 * @param {number[]} arr
 * @return {boolean}
 */
var validMountainArray = function (arr) {
	let isMountain = false;
	if (
		arr.length <= 2 ||
		arr.indexOf(Math.max(...arr)) === arr.length - 1 ||
		arr.indexOf(Math.max(...arr)) === 0
	)
		return false;
	for (let i = 0; i < arr.length; i++) {
		if (i < arr.indexOf(Math.max(...arr))) {
			if (arr[i] < arr[i + 1]) isMountain = true;
			else return false;
		} else if (i > arr.indexOf(Math.max(...arr))) {
			if (arr[i] < arr[i - 1]) isMountain = true;
			else return false;
		}
	}
	return isMountain;
};
