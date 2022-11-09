class Solution:
    def reformatDate(self, date: str) -> str:
        date_str = date.split(" ")
        hashmap = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}
        return "{}-{}-{}".format(date_str[-1], hashmap[date_str[-2]], date_str[-3][:-2] if len(date_str[-3][:-2])==2 else "0"+date_str[-3][:-2])