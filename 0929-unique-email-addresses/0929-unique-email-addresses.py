class Solution:
    def numUniqueEmails(self, emails) -> int:
        hashmap = {}
        for i in emails:
            fixed = i.split("@")
            fixed[0] = fixed[0].replace(".","")
            fixed_str = ""
            for index, j in enumerate(fixed[0]):
                if j=="+":
                    fixed_str = fixed[0][:index]                    
                    break
                else:
                    fixed_str+=j
            fixed[0] = fixed_str
            hashmap['@'.join(fixed)] = 1+hashmap.get('@'.join(fixed),0)
        return len([*hashmap])