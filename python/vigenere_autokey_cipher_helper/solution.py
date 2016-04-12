import sys,os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
sys.path.insert(0,parentdir) 
from testtool.testtool import test

class VigenereAutokeyCipher(object):
    def __init__(self, key, abc):
        self.key = key        
        self.abc =abc
        self.dict_len = len(self.abc)
        idxs = range(self.dict_len)        
        self.alphabet = {a:i for a,i in zip(self.abc, idxs) }
        self.reverse_alphabet = {i:a for a,i in zip(abc, idxs) }


    def encode(self, plaintext):
        return self.dealcode(plaintext)


    def dealcode(self, srctext, encode = True):
        use_key = self.key
        dsttext = [None]*len(srctext)
        use_key_idx = 0
        for i, c in enumerate(srctext):
            cur_pos = self.alphabet.get(c, -1)
            if cur_pos == -1:
                dsttext[i] = c
                continue
            shift_pos = self.alphabet.get(use_key[use_key_idx], -1)
            while shift_pos == -1:
                use_key_idx += 1
                shift_pos = self.alphabet.get(use_key[use_key_idx], -1)
            nextpos = (cur_pos + shift_pos) if encode else (cur_pos - shift_pos)
            dsttext[i] = self.reverse_alphabet.get(nextpos % self.dict_len)
            use_key_idx += 1
            if use_key_idx == len(use_key):
                use_key = srctext if encode else dsttext
                use_key_idx = 0
        return ''.join(dsttext)        

    def decode(self, encoded):
        return self.dealcode(encoded, False)        

    def __str__(self):
        return "key:" + str(self.key) +", abc:" + str(self.abc)

if __name__ == '__main__':
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key = 'password'
    c = VigenereAutokeyCipher(key, alphabet)

    test.assert_equals(c.encode('codewars'), 'rovwsoiv')
    test.assert_equals(c.decode('laxxhsj'), 'waffles')

    test.assert_equals(c.encode('amazingly few discotheques provide jukeboxes')
, 'pmsrebxoy rev lvynmylatcwu dkvzyxi bjbswwaib')
    test.assert_equals(c.decode('pmsrebxoy rev lvynmylatcwu dkvzyxi bjbswwaib')
, 'amazingly few discotheques provide jukeboxes')

    test.run_test()


    