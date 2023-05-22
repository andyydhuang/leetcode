import logging, sys

class Allocator:
    def __init__(self, n: int):
        self.used_dic = collections.defaultdict(list)
        self.free_spaces = [[0, n-1]]

        logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
        self.logger = logging.getLogger(__name__)
        if self.logger.isEnabledFor(logging.DEBUG):
            self.memory_array = [-1] * n

    def print_memory_array(self):
        if self.logger.isEnabledFor(logging.DEBUG) == False:
            return

        for free_space in self.free_spaces:
            for k in range(free_space[0] , free_space[1]+1):
                self.memory_array[k] = 0

        for key in self.used_dic.keys():
            for li in self.used_dic[key]:
                for v in range(li[0], li[1]+1):
                    self.memory_array[v] = key
        print('{}'.format(self.memory_array))

    def allocate(self, size: int, mID: int) -> int:
        logging.debug('Allocate    mID %d size %d', mID, size)

        ret = -1
        for free_space in self.free_spaces:
            length = free_space[1] - free_space[0] +1
            #Less Than, do nothing
            #Equal
            if length == size:
                ret = free_space[0]
                self.used_dic[mID].append([free_space[0], free_space[0]+size-1])
                self.free_spaces.remove(free_space)
                break
            #Greater
            elif length > size:
                ret = free_space[0]
                self.used_dic[mID].append([free_space[0], free_space[0]+size-1])
                free_space[0] += size
                break
        self.print_memory_array()
        return ret

    def free(self, mID: int) -> int:
        logging.debug('Free  mID %d', mID)

        ans = 0
        lis = self.used_dic.get(mID)
        if lis is None:
            return ans

        for li in lis:
            ans += (li[1] - li[0] + 1)
            #Adjust free_spaces
            self.free_spaces = self.merge(self.free_spaces, li)

        self.used_dic.pop(mID)

        self.print_memory_array()
        return ans

    def merge(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        k = 0
        for k in range(0, len(intervals)):
            interval = intervals[k]

            if newInterval[0]-1 > interval[1]:
                ans.append(interval)
            elif newInterval[1] < interval[0]-1:
                break
            else:
                newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1]) ]

            if k == len(intervals)-1:
                k+=1
        return ans + [newInterval] + intervals[k:]

# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)