class Multiples3or5:
    def sumMultiples(self, max):
        sum = 0;

        for i in range (0, max):
            if (i % 3 == 0) or (i % 5 == 0):
                sum += i

        print(sum)
        return sum
