class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Running total
        total = 0
        # every value in array should be less than this
        valley = 9999999
        # largest peak
        peak = valley
        
        for i in range(0, len(prices)):
            if prices[i] < peak:
                total += peak - valley

                valley = prices[i]
                # set them to current day
                peak = valley
            else:
                # new peak has been found
                 peak = prices[i]

        # if the last value is a peak
        total += peak - valley

        return total;

        # Time Complexity = O(n) since we traverse the array only once
        # Space Complexity = O(1) since we only keep track of 3 values
    
    def MaxProfitSinglePass(self, prices):
        total = 0
        
        # Start in the second elemnt for comparison to first day
        for i in range(1, len(prices)):
            # As long as the day we are on has a larger price than the previous day
            if prices[i] > prices [i - 1]:
                # add the positive difference to our total
                total += prices[i] - prices[i - 1]

        return total;
        
        # Time complexity is O(n) since we went thru array only once
        # Space complexity is O(1) since we only hold the total

def main() -> None:
    # Initialize class
    temp = Solution();
    prices = [7,1,5,3,6,4]
    print("Total Profit is", temp.maxProfit(prices));
    print("Total profit easy is", temp.MaxProfitSinglePass(prices))

if __name__ == "__main__":
    main()