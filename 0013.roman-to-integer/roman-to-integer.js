/**
 * 13. Roman to Integer
 * @param {string} s
 * @return {number}
 */
var romanToInt = function (s) {
	const roman_to_int = {
		I: 1,
		V: 5,
		X: 10,
		L: 50,
		C: 100,
		D: 500,
		M: 1000,
	};

	let romans = s.split("");
	let result = roman_to_int[romans[0]];

	romans.forEach((elem, index) => {
		let prev = index > 0 && roman_to_int[romans[index - 1]];
		let curr = roman_to_int[romans[index]];
		if (prev && curr) {
			if (prev >= curr) {
				result += curr;
			} else {
				result = result - prev * 2 + curr;
			}
		}
	});

	return result;
};
