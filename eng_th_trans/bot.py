from enchant import Dict
from pythainlp.spell import correct
from pythainlp.tokenize import syllable_tokenize
from pythainlp.util import isthai,thai_to_eng,eng_to_thai

class TranslateBot:
    
    def __init__(self,msg,ignorer=".0123456789"):
        """
        msg : ข้อความที่ต้องการตรวจสอบเเละเเก้ไข
        ignorer : ตัว regex ที่อนุญาตให้มี
        """

        self.msg = msg
        self.ignorer = ignorer
        self.d = Dict("en_us")
        # print(self.d.check("English"))

    def getMsg(self):
        arr = syllable_tokenize(self.msg) ## เเยก text ออกมาเป็น word ตรวจสอบทีละ word ว่าถูกต้องหรือไม่
        # arr = word_tokenize(self.msg)
        for index,item in enumerate(arr):
            if item in "๐๑๒๓๔๕๖๗๘๙":
                continue
            if (isthai(item,self.ignorer)): ## เช็คว่าเป็นภาษาไทยหรือเปล่า
                arr[index] = self.check(item)
            else:
                arr[index] = self.check(item,lang="en")
        # print(arr)
        return "".join(arr)

    def check(self,word,lang="th"):
        """
        ตรวจสอบว่าคำภาษาไทย สะกดถูกหรือไม่ => ถ้าถูกให้เเก้เป็นภาษาอังกฤษ
        word : คำที่ต้องการตรวจสอบ
        lang : ภาษาที่ทำการตรวจสอบ (th,en)
        """
        if lang =="th" and word == correct(word):
            word = thai_to_eng(word) 
            # print("อยู่นี่จ้า")
            # return word
        # print(word)
        # print(word == self.d.check(word))
        if lang == "en" and self.d.check(word):
            word = eng_to_thai(word)
            # print("hi2")
        
        return word 
