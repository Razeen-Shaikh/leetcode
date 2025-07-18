/**
 * Encodes a URL to a shortened URL.
 *
 * @param {string} longUrl
 * @return {string}
 */
const encode = function (longUrl) {
  return `#${longUrl}`;
};

/**
 * Decodes a shortened URL to its original URL.
 *
 * @param {string} shortUrl
 * @return {string}
 */
const decode = function (shortUrl) {
  return shortUrl.slice(1);
};

/**
 * Your functions will be called as such:
 * decode(encode(url));
 */
