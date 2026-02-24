
def base64_decode(encoded):
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

    # Padding sayısını bul
    padding = encoded.count("=")
    encoded = encoded.rstrip("=")

    binary_string = ""

    # Her karakteri 6 bit binary'ye çevir
    for char in encoded:
        index = base64_chars.index(char)
        binary_string += format(index, "06b")

    # Padding'e göre sondaki fazla bitleri sil
    if padding:
        binary_string = binary_string[:-(padding * 2)]
    # 1 tane = işareti varsa bu sonda 2 bit padding var demektir
    # yani 2 bit sıfır (0) eklenmiş demektir

    decoded = ""

    # 8 bitlik parçalara böl
    for i in range(0, len(binary_string), 8):
        byte = binary_string[i:i + 8]
        if len(byte) == 8:
            decoded += chr(int(byte, 2))

    return decoded

def base64_encode(decoded):
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    binary_string=""
    padding=0


    for harf in decoded:
        binary_string += format(ord(harf),"08b")

    # print(len(binary_string)) # -> sonuç 120 çıkar çünkü 15 karakter var 8 bit -> 120

    if len(binary_string)%6==2:
        binary_string += "0000"
        padding=2
    elif len(binary_string)%6==4:
        binary_string += "00"
        padding = 1

    encoded=""

    for i in range(0, len(binary_string), 6):
        byte = binary_string[i:i + 6]
        if len(byte) == 6:
            encoded += base64_chars[int(byte, 2)]

    if padding==1:
        encoded += "="
    elif padding==2:
        encoded += "=="

    return encoded


encoded_text="TW9uYUxpc2FEYVZpbmNp"

print(base64_decode(encoded_text))
print(base64_encode(base64_decode(encoded_text)))
