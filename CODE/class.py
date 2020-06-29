class DNA:
    def __init__(self, strand, direction):
        self.name = 'Unnamed DNA'
        self.strand = strand.upper()
        self.start = direction[0] + '\''
        self.stop = direction[3] + '\''

    def show_all(self):
        print(self.name)
        print('{}{}{}'.format(self.start, ' ' * len(self.strand), self.stop))
        print('{}{}{}'.format(' '*len(self.start), self.strand, ' '*len(self.stop)))
        print('{}{}{}'.format(self.start, ' ' * len(self.strand), self.stop))

    def rename(self, name):
        self.name = name

    def show_length(self):
        print(len(self.strand))

    def cut(self, enzyme):
        for base in range(len(self.strand)-len(enzyme.strand)):
            for


class Enzyme(DNA):
    def __init__(self):
        super().__init__(strand, direction)
            self.strand, self.cut_position = self.cut_position

'''
    def show_base(self):
        self.count_base()
        for _ in range(4):
            print('{} Base: {:0>5}'.format())

    def count_base(self):
        n_a, n_t, n_c, n_g = 0, 0, 0, 0
        for base in self.strand:
            if base == 'A':
                n_a += 1
            elif base == 'G':
                n_g += 1
'''
'''
    @staticmethod
    def cut_position(strand, delim):
        delim_position = 0
        for base in strand:
            if base != delim:
                delim_position += 1
            elif base == delim:
                if delim_position != 0:
                    return delim_position+1, strand.replace(delim, '').upper()
                else:
                    return 'Not Found', strand.replace(delim, '').upper()
'''

# tester
if __name__ == '__main__':
    test_dna = DNA('gattgctatgcattagc', '3to5')
    test_dna.rename('Test DNA')
    test_dna.show_all()

