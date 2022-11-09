class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        set_source = set()
        set_destination = set()
        for i in paths:
            set_source.add(i[0])
            set_destination.add(i[1])
        return next(iter(set_destination-set_source))
        