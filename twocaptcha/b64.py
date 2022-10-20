from base64 import b64encode

file = open("C:/Users/PHI/Downloads/img.png", "rb")
# b64encode(file._result)
print('data:image/jpeg;base64,'+b64encode(file.read()).decode('utf-8'))
