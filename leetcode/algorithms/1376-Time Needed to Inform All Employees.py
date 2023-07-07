class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
      ''' The version causes TLE
      ans = [None] * len(manager)
      q = collections.deque([(headID, 0)])
      max = 0

      while q:
        for _ in range(len(q)):
          [emp, total_t] = q.popleft()
          if informTime[emp] == 0:
            ans[emp] = total_t
            if total_t > max:
              max = total_t
            continue
          for i in manager:
            if manager[i] == emp:
              q.append([i, total_t+informTime[emp]])
      return max
      '''
      spent = [-1] * n
      spent[headID] = 0
      q = collections.deque([])
      max_spent = 0
      #for idx ,_ in enumerate(informTime):
      for idx in range(len(informTime)):
          # Backtrace employee that has no subordinates
          if informTime[idx] == 0:
              emp = idx
              while emp != -1 :
                boss = manager[emp]
                # Has recorded, no need to backtrace
                if spent[emp] != -1:
                  q.append((emp, spent[emp]))
                  break  
                q.append((emp, informTime[boss]))
                emp = boss
              
              # Record spent time
              total = 0
              while q:
                emp, inform_t = q.pop()
                total += inform_t
                spent[emp] = total
              if total > max_spent: max_spent = total  
      #print(spent) 
      return max_spent