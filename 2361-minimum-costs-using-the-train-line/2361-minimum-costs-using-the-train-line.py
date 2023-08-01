class Solution:
	def minimumCosts(self, regular: List[int], express: List[int], ec: int) -> List[int]:

		ans = []

		regc = regular[0]

		expc = express[0] + ec

		ans.append(min(regc,expc))

		for i in range(1,len(regular)):

			newregc = min(regc + regular[i], expc + regular[i])

			newexpc = min(regc + ec + express[i], expc + express[i])

			regc = newregc
			expc = newexpc

			ans.append(min(regc,expc))

		return ans