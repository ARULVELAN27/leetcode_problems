class Solution(object):
    def bestClosingTime(self, customers):
        y = customers.count("Y")
        n = 0
        max1 = y
        index = -1

        for x in range(0, len(customers)):
            if customers[x] == "Y":
                y -= 1
            else:
                n += 1

            if max1 > y + n:
        
                max1 = y + n
                index = x

        return index + 1

