class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = collections.defaultdict(list)
        
        #Example
        #Input: strs = ["tan","nat"]
        #str_dict: {"['a', 'n', 't']": ['tan', 'nat']}
        for word in strs:
            sorted_word = sorted(word)
            #Comment following code because of slower performance
            #turn list back into a string
            #sorted_word = ''.join(sorted_word)
            #str_dict[sorted_word].append(word)
            str_dict[str(sorted_word)].append(word)
        return list(str_dict.values())