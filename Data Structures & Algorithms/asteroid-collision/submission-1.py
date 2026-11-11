class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []

        for a in asteroids:
                while s and s[-1] > 0 and a < 0: #s[-1] to right and a to left, 
                    diff = s[-1] + a
                    if diff < 0: # a bigger 
                        s.pop()
                    elif diff > 0:
                        a = 0
                    else:
                        a = 0
                        s.pop()
                if a:
                    s.append(a)

        return s
        