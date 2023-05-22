class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        N = len(arr)
        visited = [False] * N
        idx = start
        queue = []
        queue.append(idx)      

        while queue:
            idx = queue.pop()

            visited[idx] = True
            if arr[idx] == 0:
                return True
            else:
                k1 = idx - arr[idx]
                k2 = idx + arr[idx]
                if k1 >= 0 and visited[k1] == False:
                    queue.append(k1) 
                if k2 < N and visited[k2] == False:
                    queue.append(k2)
        return False