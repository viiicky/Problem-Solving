	# Add your code here
    def computeDifference(self):
        self.maximumDifference = float('-Infinity')
        for index, a in enumerate(self.__elements):
            for b in self.__elements[index+1:]:
                absoluteDifference = abs(a-b)
                if absoluteDifference > self.maximumDifference:
                    self.maximumDifference = absoluteDifference
