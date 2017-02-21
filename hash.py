import hashlib


class hashing:
    def enc(self,txt,typehash):
        #txt=txt.encode("utf-8")
        h=hashlib.new(typehash)
        h.update(txt)
        return  h.hexdigest()




__author__ = 'hp'
