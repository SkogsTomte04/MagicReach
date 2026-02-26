import easyocr
import torch

# helpfunc
def printresult(res):
    for r in res:
        print(r)


print(torch.cuda.is_available()) ## need to enable cuda to make it faster


reader = easyocr.Reader(['en'], gpu=True)

result = reader.readtext('magic_cards/AvatarAang.jpg')

printresult(result)




