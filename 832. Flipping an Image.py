class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        result = []
        for each_img in image:
            each_img = each_img[::-1]
            ele = []
            for i in range(len(each_img)):
                if each_img[i] == 0:
                    each_img[i] = 1
                    ele.append(each_img[i])
                else:
                    each_img[i] = 0
                    ele.append(each_img[i])
            result.append(ele)
        return result

