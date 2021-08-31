import re
import math

ENG_FREQ = {'A': 0.082, 'B': 0.015, 'C': 0.028, 'D': 0.043, 'E': 0.13, 'F': 0.022, 'G': 0.02, 'H': 0.061, 'I': 0.07,
            'J': 0.0015, 'K': 0.0077, 'L': 0.04, 'M': 0.024, 'N': 0.067, 'O': 0.075, 'P': 0.019, 'Q': 0.00095,
            'R': 0.06, 'S': 0.063, 'T': 0.091, 'U': 0.028, 'V': 0.0098, 'W': 0.024, 'X': 0.0015, 'Y': 0.02,
            'Z': 0.00074}
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
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
STD_COEF = 1
RE = re.compile('[^A-Z\s]')


def calc_hist(text):
    """
    calculate the letters occurrences histogram
    :param text: the text to analyze
    :return: the percentage of occurrences for each letter
    """
    counters = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0,
                'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
    # count the number of occurrencees
    for letter in text:
        counters[letter.upper()] += 1
    text_length = len(text)
    for key in counters:
        counters[key] /= text_length
    return counters


def count_doubles(text, text1):
    """
    counts the number of of identical letters which are in the same offset from the beginning of the text
    :param text: first text
    :param text1: second text
    :return: the number of identical letters
    """
    doubles = 0
    for i in range(len(text)):
        if text[i] == text1[i]:
            doubles += 1
    return doubles


def get_shift(hist):
    """
    find the shift of the letters frequency from the standard english letters frequency.
    The function iterates and finds the shift of the histogram which gives the minimum between thca the sums of the
    square of differences between the shifted histogram and the standard english histogram
    :param hist: the letters frequency histogram
    :return: the histogram shift
    """
    min_diff = 10000
    min_shift = 0
    for i in range(len(hist)):
        diff = 0
        for letter in hist.keys():
            key = chr(((ord(letter) - ord('A') + i) % 26) + ord('A'))
            diff += math.pow((hist[key] - ENG_FREQ[letter]), 2)
        if diff < min_diff:
            min_diff = diff
            min_shift = i
    return min_shift


def get_key_len(doubles):
    """
    finds the key length
    :param doubles: a list of the number of double letters when shifting the cipher
    :return: the key length
    """
    avg = 0
    max_doubles = 1
    for i in range(1, len(doubles)):
        avg += doubles[i]
        if doubles[i] > doubles[max_doubles]:
            max_doubles = i
    avg /= (len(doubles) - 1)
    # find STD
    sum_diff = 0
    for i in range(1, len(doubles)):
        sum_diff += math.pow((doubles[max_doubles] - doubles[i]), 2)
    std = math.sqrt(sum_diff/(len(doubles) - 1))
    key_len = max_doubles
    for i in range(1, len(doubles)):
        if doubles[i] > (doubles[max_doubles] - std * STD_COEF) and (max_doubles % i) == 0:
            key_len = i
            break
    print('key length is ' + str(key_len))
    return key_len


def main():
    doubles = []
    buckets = {}
    cipher = RE.sub('', CIPHER.upper())
    cipher = cipher.replace(" ", "")
    # find the number of doubles when shifting the cipher
    for i in range(len(cipher)):
        doubles.append(count_doubles(cipher, cipher[(-1 * i):] + cipher[:(-1 * i)]))
    # find the key length
    key_len = get_key_len(doubles)
    # find the key by comparing the the letters frequency, in steps of key length, to the true english letters frequency
    for j in range(key_len):
        buckets[j] = cipher[j::key_len]
        shift = get_shift(calc_hist(buckets[j]))
        key = chr(ord('A') + shift)
        print(key, end='')


if __name__ == '__main__':
    main()
