# You are given a stream of n videos, each represented by a distinct number from 1 to n that you need to "upload" to a server. You need to implement a data structure that calculates the length of the longest uploaded prefix at various points in the upload process.

# We consider i to be an uploaded prefix if all videos in the range 1 to i (inclusive) have been uploaded to the server. The longest uploaded prefix is the maximum value of i that satisfies this definition.

# Implement the LUPrefix class:

# LUPrefix(int n) Initializes the object for a stream of n videos.
# void upload(int video) Uploads video to the server.
# int longest() Returns the length of the longest uploaded prefix defined above.
