class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
            box_list=[]
            unit_list=[]
            box_total=0
            total_unit=0
            boxTypes.sort(key=lambda x:x[1], reverse=True)
            for box, unit in boxTypes:
                box_list.append(box)
                unit_list.append(unit)
                box_total+=box
            if box_total>truckSize:
                for i in range(len(unit_list)):
                    if truckSize>box_list[i]:
                        truckSize-=box_list[i]
                        total_unit+=(unit_list[i]*box_list[i])
                    else:
                        total_unit+=(unit_list[i]*truckSize)
                        truckSize=0
                        break
            else:
                for i in range(len(unit_list)):
                    total_unit+=(unit_list[i]*box_list[i])
            return total_unit


