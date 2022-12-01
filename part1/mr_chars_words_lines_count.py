from mrjob.job import MRJob


class MRCharsWordsLinesCount(MRJob):

    def mapper(self, _, line):
        # Your code starts here.

        # Your code ends here.

    def reducer(self, key, values):
        # Your code starts here.

        # Your code ends here.


if __name__ == '__main__':
    MRCharsWordsLinesCount.run()
