class DNA:
    def __init__(self, strand, direction):
        self.name = 'Unnamed DNA'
        self.strand = strand.upper()
        self.start = direction[0] + '\''
        self.stop = direction[3] + '\''
        self.a, self.t, self.c, self.g, self.non_base = self.count_each()

    def show_all(self):
        print(self.name)
        print('{}{}{}'.format(self.start, ' ' * len(self.strand), self.stop))
        print('{}{}{}'.format(' '*len(self.start), self.strand, ' '*len(self.stop)))
        print('{}{}{}'.format(self.start, ' ' * len(self.strand), self.stop))

    def rename(self, name):
        self.name = name

    def show_length(self):
        print('Length of {!r} = {}'.format(self.name, len(self.strand)))

    def count_each(self):
        a, t, c, g = 0, 0, 0, 0
        non_base = 0
        for base in self.strand:
            if base == 'A':
                a += 1
            elif base == 'T':
                t += 1
            elif base == 'C':
                c += 1
            elif base == 'G':
                g += 1
            else:
                non_base += 1
        return a, t, c, g, non_base
    
    def cut(self, enzyme):
        pass


class Enzyme(DNA):
    def __init__(self, strand, direction, delimiter):
        super().__init__(strand, direction)
        self.delimiter = delimiter
        self.strand, self.cut_position = self.enzyme_setting()
        # ตัวสุดท้ายของสายที่โดนตัดคือ ตัวที่ self.cut_position (เริ่มนับตัวแรกจาก1)

    def enzyme_setting(self):
        pure_dna = ''
        cnt = 0  # cnt = index ของ
        pos = None
        for base in self.strand:
            if base not in ('A', 'T', 'C', 'G'):
                pos = cnt
            else:
                pure_dna += base
                cnt += 1
        if pos is None:
            return pure_dna, 'Not found'
        else:
            return pure_dna, pos

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
    # DNA
    test_dna = DNA('gattgctatgcattagc', '3to5')
    test_dna.rename('Test DNA')
    test_dna.show_all()
    print(test_dna.a)
    test_dna.show_length()
    print('='*60)

    # Enzyme
    test_enzyme = Enzyme('cctag|g', '3to5', '|')
    test_enzyme.rename('Test Enzyme')
    test_enzyme.show_all()
    print(test_enzyme.a)
    test_enzyme.show_length()
    print('Cut Positon = {}'.format(test_enzyme.cut_position))

