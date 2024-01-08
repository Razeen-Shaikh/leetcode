/**
 * 1010. Pairs of Songs With Total Durations Divisible by 60
 * @param {number[]} time
 * @return {number}
 */
var numPairsDivisibleBy60 = function (time) {
	let count = 0;
	for (i = 0; i < time.length; i++) {
		for (j = i + 1; j < time.length; j++) {
			if ((time[i] + time[j]) % 60 === 0) count++;
		}
	}
	return count;
};
