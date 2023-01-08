# TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk. Design a class to encode a URL and decode a tiny URL.

# There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

# Implement the Solution class:
# Solution() Initializes the object of the system.
# String encode(String longUrl) Returns a tiny URL for the given longUrl.
# String decode(String shortUrl) Returns the original long URL for the given shortUrl. It is guaranteed that the given shortUrl was encoded by the same object.

class Codec:

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.hm = {}
        split = longUrl.split('/')
        i = 0
        for s in split:
            if i == 0:
                self.hm[i] = s
            else:
                self.hm[i] = '/' + s
            i += 1
        encoded = ""
        for i in range(i):
            encoded += str(i)
        return encoded 
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        decoded = ""
        i = 0
        for c in shortUrl:
            decoded += self.hm[i]
            i += 1
        return decoded