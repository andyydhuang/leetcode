class Solution:
    def frequencySort(self, s: str) -> str:
        ret_str = ''
        for key, cnts in Counter(s).most_common():
            ret_str += (key * cnts)
        return ret_str