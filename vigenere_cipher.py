LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
CIPHER = 'UEKQG VFVMF ODMFT KIMIM YRLQM XCQFF RVOUD RNPAI GJTAH KUJKQ BVZKA TVETA RFWWQ JRBTQ XSCFY UJBAR GCTNK NVZSD' \
         ' GELYA ZYMDM TUBTQ XVEME TFBTU TXBTM ZJPQI ULTPZ UKPMH KXQHQ TKWFT KTPUX JFVOQ YYMSM BVPQD GCQFF RVZUP ' \
         'OEOTA UUWRD KUDQX BVBIT OTPEG OKMPT KIAAI KCTFT GKATQ CFCXP TVDQD CVIDM TPBTU TXMXE KJWET KNIEM RNIKE IRTXQ' \
         ' JCQFF RVZQP XZLUZ MYWAP UEMPM EYMDY UKPQD YRQPF UYMDO UDMXU ZKTQD KUZUP OEOTA UUPQD KZAMB OVKQA LTIWQ ' \
         'GELMN UKBXQ UWEUZ KKIWQ ZYMYF UPWGD MIIZP SFBTQ XJPQU YZTXM TUEQM QRVPF NVGIU RCLAT KIOAA JJMFA AKJQR UIMUF' \
         ' MVBET UKIZP CYMZK ULIDQ MFQZS CRTWZ OTMXK GELCG OVBXK GELPA TFBDG TFNRF NVXMF NFZKA ADIKR GCTMZ JSZQM ' \
         'QKPQN UKBXQ GELFT KEGAG XXZMZ JDWFT KIEUX RXMFZ UKPUZ MRVPI NVVKA AXWUZ ZFPQD XFWYP UEBRA XXMFF UJIKS UFLYA' \
         ' XEQZS GELPA TKXQQ VZVFA KMMDK IFZZQ XSMRA XVGAG JFQFU CZTXF GBMSD KRBOM XVAMU JCQFF RVZQP XZLUZ MYWAP ' \
         'ZFPQD SFBTQ XRVPS GMMTQ XYIZP UEQFF NVODM TUUAF NVZXU BVLAG ZZVFT KNWAP NRTRM RVISG KWZAY ZYMHU RCISQ GELVG' \
         ' YKIEX OKBXQ XVLDU JZVST UFLQZ ZVZQP ZYMIA UUIIA RWUQF NVZDQ JIQPU TXPAA JUQPZ UKSZA CNPMF GNQOW KUKDQ ' \
         'GKCDQ NVEME GELIM YEWFM ZRTXM LIIUP UWPUY MFWPP GPTUF ZCMDQ JIQPU TXPAA JJIUP NVBTM TBGAG QZVPX ENWXR CYQFT' \
         ' KIIIM EJWQM XCGXU ZKTQD KUZUP OEOTA UUBAY EXZMZ JDWFT KIAIT GKPMH KPWGS UKQZK ULZMB XFVOM QVIZP CZVQK ' \
         'KJBQD JRGIM YSIWU TXLMK YFXAA XJQOW MIIZP SFBTQ XZAFA NRDQE UDMFT OEOSA UUBAY GBMTQ XJBDA TXMDI NVZQP UVAKA' \
         ' AIODM TUUAF NVZXU BVTUF ZCMDQ JIQPU TXPAA JROAA JHCMD ZVZAR GCMMS AVNMD ZYMDA TZVFT KNWAP NVZTA AJMEF ' \
         'GELEG TUMDF NVBTD KVTMD MVWMW ZIMQE ZYMZG ZKZQQ YRZQV AJBNQ RFEKA AJCDQ RPUGE ZBVAI OKZQB RZMPX OKBXQ XVLDU' \
         ' JZVST UFL'


def main():
    msg = CIPHER# 'qfdtdts'
    # msg = 'prosper'
    key = 'GRIMM' # 'BOP'
    mode = 'decrypt'
    # mode = 'encrypt'

    if mode == 'encrypt':
        trans = encrypt_msg(key, msg)
    else:
        trans = decrypt_msg(key, msg)

    print('using key %s' % key )
    print('the msg is: %s' % msg)
    print(trans)


def encrypt_msg(key, msg):
    return trans_msg(key, msg, 'encrypt')


def decrypt_msg(key, msg):
    return trans_msg(key, msg, 'decrypt')


def trans_msg(key, msg, param):
    trans = ''
    key_index = 0

    for symbol in msg:
        if symbol.upper() in LETTERS:
            letter_key = ord(key[key_index % len(key)]) - ord('A')
            if symbol.isupper():
                start_char = ord('A')
            else:
                start_char = ord('a')
            letter_num = ord(symbol) - start_char
            if param == 'decrypt':
                trans += chr((letter_num - letter_key) % len(LETTERS) + start_char)
            else:
                trans += chr((letter_num + letter_key) % len(LETTERS) + start_char)
            key_index += 1
        else:
            trans += symbol
    return trans

main()