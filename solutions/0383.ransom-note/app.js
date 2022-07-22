/**
 * 383. Ransom Note
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function (ransomNote, magazine) {
	if (ransomNote === magazine) return true;
	let ransome = ransomNote.split("").sort();
	let mag = magazine.split("").sort();
	return ransome.every((ran, index) => {
		if (mag.includes(ran)) {
			mag.splice(mag.indexOf(ran), 1);
			return true;
		}
	});
};
