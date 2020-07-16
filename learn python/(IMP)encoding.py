import sys
script,input_encoding,error=sys.argv

def main(language_file,encoding,errors):
    line=language_file.readline()

    if line:
        print_line(line,encoding,errors)
        return main(language_file, encoding, errors)#recursion... this main function in the end will return
                                                    #nothing.And nothing will be returned bu this function.
                                                    #its only job is to call print_line function again and
                                                    #again till if returns false and main returns nothing

def print_line(line,encoding,errors):
    next_lang=line.strip()
    raw_bytes=next_lang.encode(encoding,errors=errors)
    cooked_string=raw_bytes.decode(encoding,errors=errors)

    print(raw_bytes,"<===>",cooked_string)


languages=open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)
# what arguments to give: utf-8 strict
#utf-8 utf-16 and big5 are codec
#letters are mapped to ASCII tables inside a computer. Z is 90 which is 1011010
0b1011010  #90
ord('Z')   #90
chr(90)    #'Z'
#ASCII only encodes English. So other languages are left
#for this reason there is unicode. we use 32 bit to encode a unicode char
#it can encode 2^32 characters. but most of this space is unused
#some of this space is used for emojis
#now 32 bits is 4 bytes so there is a lot of wasted space . We can also use 16 bits
#but still there will be wasted space
#so we have a convention which is sort of a compression encoding and uses 8 bits
#it is called utf-8 which means Unicode Transformation Format 8 Bits
#bytes are decoded to form strings and strings are encoded to form bytes according to the convention
#bytes are written inside b''(byte string) i.e raw_bytes which have no meaning till they are decoded
#cooked_string is from decoding raw_bytes i.e using the utf-8 convention, we get to know what b'' means
# and then that string(made of characters) is formed. BYTES ARE DECODED AND STRINGS ARE ENCODED
