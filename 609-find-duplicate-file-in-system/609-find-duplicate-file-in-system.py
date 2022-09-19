class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hashmap = {}
        ans = []
        for i in paths:
            splits = i.split(" ")
            for j in range(1,len(splits)):
                key = re.findall(r'\((\w+)\)', splits[j])[-1]
                file_name = splits[j].split("(")[0]
                if key in hashmap:
                    hashmap[key].append(splits[0] + "/" + file_name)
                else:
                    hashmap[key] = [splits[0] + "/" + file_name]
        for key, val in hashmap.items():
            if len(val)>1:
                ans.append(val)
        return ans