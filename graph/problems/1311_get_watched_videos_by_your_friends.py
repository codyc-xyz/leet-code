# There are n people, each person has a unique id between 0 and n-1. Given the arrays watchedVideos and friends, where watchedVideos[i] and friends[i] contain the list of watched videos and the list of friends respectively for the person with id = i.

# Level 1 of videos are all watched videos by your friends, level 2 of videos are all watched videos by the friends of your friends and so on. In general, the level k of videos are all watched videos by people with the shortest path exactly equal to k with you. Given your id and the level of videos, return the list of videos ordered by their frequencies (increasing). For videos with the same frequency order them alphabetically from least to greatest. 

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        
        q = deque([(id, 0)])  
        seen = set()
        seen.add(id)
        levelMovies = {}

        while q:
            curr, currLevel = q.popleft()
            for f in friends[curr]:
                if f not in seen and currLevel < level:
                    if currLevel + 1 == level:
                        for v in watchedVideos[f]:
                            if v not in levelMovies:
                                levelMovies[v] = 1
                            else:
                                levelMovies[v] += 1
                    q.append((f, currLevel + 1))
                    seen.add(f)

        ans=sorted(levelMovies,key=lambda x: (levelMovies[x],x))
        return ans
        
