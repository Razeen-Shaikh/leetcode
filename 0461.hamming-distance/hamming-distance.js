/**
 * 461. Hamming Distance
 * @param {number} x
 * @param {number} y
 * @return {number}
 */
var pad = function (str, max) {
	return str.length < max ? pad("0" + str, max) : str;
};

var hammingDistance = function (x, y) {
	var [xb, yb] = [x.toString(2), y.toString(2)];
	[xb, yb] = [
		"00000000".substr(xb.length) + xb,
		"00000000".substr(yb.length) + yb,
	];
	var hamDist = 0;

	if (xb.length < yb.length) {
		xb = pad(xb, yb.length);
	} else if (xb.length > yb.length) {
		yb = pad(yb, xb.length);
	}

	[xb, yb] = [xb.split(""), yb.split("")];

	xb.forEach((b, index) => {
		if (b !== yb[index]) hamDist++;
	});

	return hamDist;
};
