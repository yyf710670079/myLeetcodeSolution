# coding = utf-8
__author__ = "Yufeng Yang"

"""
 You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.

Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c. Chain of pairs can be formed in this fashion.

Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs. 
You can select pairs in any order.


Example 1:

Input: [[1,2], [2,3], [3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4]

"""


# method 1
# Time:O(n^2)
def findLongestChain1(pairs):
    """
    :param pairs: List[List[int]]
    :return: int

    dp[i] means the Maximum Length ending with pairs[i]
    """
    pairs.sort(key=lambda x: x[0])
    dp = [1] * len(pairs)

    for i in range(1, len(pairs)):
        for j in range(i - 1, -1, -1):
            # if pairs[i] can connect with any j where 0 <= j < i,
            if pairs[i][0] > pairs[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


# method 2
# Time: O(nlgn)
# have no proof and may be wrong but succeed all the test case
# Greedy
def findLongestChain2(pairs):
    """
    :param pairs: List[List[int]]
    :return int

    # dp[i] means the Maximum Length from pairs[:i]
    # dp_index[i] means the ending pair index of the longest chain from pairs[:i]
    """

    pairs.sort(key=lambda x: x[1])

    dp = [1] * len(pairs)
    dp_index = [i for i in range(len(pairs))]

    for i in range(1, len(pairs)):
        # if pairs[i][0] > pairs[dp_index[i - 1]][1]
        # then pairs[i][0] > pairs[k][1] where  0 <= k <= dp_index[i - 1]

        # two situation:
        # 1) pair[i] can connect the longest chain ending with dp_index[i]
        # 2) pair[i] cannot connect, then dp[i] = dp[i-1] and dp_index[i] = dp_index[i-1]
        if pairs[i][0] > pairs[dp_index[i - 1]][1]:
            dp[i] = dp[i - 1] + 1
            dp_index[i] = i
        else:
            dp[i] = dp[i - 1]
            dp_index[i] = dp_index[i - 1]

    return dp[-1]


# Simplify the last solution
# Time:O(nlgn)
def findLongestChain3(pairs):
    """
    :param pairs: List[List[int]]
    :return int


    """

    pairs.sort(key=lambda x: x[1])

    # index means the index of the end of the longest chain
    # length means the longest chain's length so far
    index, length = 0, 1
    for i in range(1,len(pairs)):
        if pairs[i][0] > pairs[index][1]:
            index, length = i, length+1

    return length


if __name__ == "__main__":
    test_pair = [[912,984],[216,679],[-864,308],[-300,480],[-618,-154],[-780,445],[-289,989],[-958,706],[-844,282],
                 [249,367],[803,867],[567,884],[-792,-170],[-626,629],[663,762],[-739,-717],[-956,979],[596,868],
                 [594,759],[-562,608],[663,986],[-675,115],[-560,583],[-221,250],[897,918],[952,956],[-664,604],
                 [287,727],[933,956],[-133,-23],[-963,683],[745,795],[-511,804],[1,240],[-393,911],[165,597],[993,994],
                 [-957,-192],[-322,53],[-243,628],[-503,-192],[-133,21],[-209,319],[-839,-56],[887,891],[340,433],
                 [-170,355],[18,313],[-37,64],[462,468],[391,506],[219,442],[315,804],[6,700],[223,762],[751,960],
                 [-645,168],[-265,946],[-438,109],[839,926],[185,715],[460,879],[-834,-384],[-902,-364],[264,471],
                 [171,898],[685,1000],[-464,-227],[465,704],[181,592],[-20,148],[-232,842],[450,988],[669,725],
                 [-183,14],[-320,720],[575,965],[-772,-4],[-833,422],[-788,-267],[54,492],[-995,-310],[521,970],
                 [-577,-500],[590,786],[179,715],[-198,588],[770,915],[-804,244],[-106,512],[285,937],[829,833],
                 [-735,40],[103,729],[791,898],[873,993],[441,996],[-839,632],[284,434],[-474,730],[-117,684],[-14,120],
                 [699,805],[442,590],[37,393],[-815,177],[116,325],[384,820],[-537,236],[-7,768],[431,839],[-93,534],
                 [22,104],[298,904],[132,432],[-696,947],[454,615],[-338,643],[344,490],[765,969],[34,224],[25,310],
                 [856,957],[-822,-736],[-148,927],[-499,-70],[-632,-301],[235,776],[156,474],[-558,822],[828,947],
                 [-776,643],[324,398],[-351,479],[601,602],[-780,-487],[-923,-461],[-126,729],[607,760],[-732,91],
                 [48,281],[150,455],[747,880],[42,264],[219,769],[-653,286],[576,771],[-616,-185],[-603,516],[-387,671],
                 [-882,93],[338,515],[337,900],[413,997],[-200,-54],[147,845],[-254,649],[483,789],[362,884],[385,710],
                 [-272,593],[-63,924],[555,984],[435,951],[635,877],[-104,395],[-727,83],[-175,-64],[90,576],[397,672],
                 [585,865],[-887,486],[476,525],[243,330],[561,937],[985,992],[352,737],[398,702],[744,953],[281,811],
                 [103,685],[-57,454],[-116,425],[-944,340],[-26,214],[-237,188],[55,123],[129,133],[-29,653],[673,974],
                 [238,809],[439,763],[-818,-634],[-270,440],[686,959],[-942,-359],[932,947],[-364,589],[-369,-254],
                 [341,381],[-695,103],[895,922],[53,999],[-633,76],[384,424],[-597,198],[-467,201],[778,914],[772,862],
                 [243,798],[-946,-444],[974,994],[917,980],[673,706],[971,998],[477,787],[-641,588],[-212,504],
                 [-659,406],[584,722],[-431,414],[-321,943],[-568,965],[-394,709],[631,791],[-948,851],[-36,415],
                 [-906,10],[-312,704],[-398,379],[544,552],[395,562],[279,900],[552,701],[946,996],[355,537],
                 [-615,-232],[-600,-551],[-454,35],[-900,-658],[172,173],[710,771],[-399,-247],[905,958],[-108,621],
                 [833,902],[600,757],[987,997],[805,926],[652,877],[-75,52],[946,975],[295,567],[-632,-211],[974,988],
                 [579,869],[-218,55],[-901,-399],[-228,743],[627,771],[583,671],[-931,-15],[-413,3],[803,960],[590,913],
                 [405,777],[-611,206],[733,972],[305,672],[661,989],[328,504],[189,586],[89,519],[833,997],[-579,486]]

    assert(findLongestChain1(test_pair) == findLongestChain2(test_pair) == findLongestChain3(test_pair))