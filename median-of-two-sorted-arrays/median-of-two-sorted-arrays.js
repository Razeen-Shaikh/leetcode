/**
 * 4. Median of Two Sorted Arrays
 * @param {number[]} numb1
 * @param {number[]} numb2
 * @return {number}
 */
var findMedianSortedArrays = function (numb1, numb2) {
	var merged = numb1.concat(numb2).sort((a, b) => a - b);
	var median = 0;

	if (merged.length % 2 === 0) {
		median =
			(merged[parseInt(merged.length / 2) - 1] +
				merged[parseInt(merged.length / 2)]) /
			2;
	} else {
		median = merged[parseInt(merged.length / 2)];
	}

	return median;
};
