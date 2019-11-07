main)

1) rev_DecompileME

주어진 apk 파일을 apktool을 사용하여 apktool d DecompileME.apk 커맨드로 디컴파일 한다.

smali/icewall/decompileme 디렉토리에 있는 MainActivity의 smali 코드를 열면 FLAG를 획득할 수 있다. (MainActivity.smali 첨부)



FLAG는 FLAG{Trust_th1s_5tr1ng}



2) crypto_ToT

nc로 접속하여 초콜릿과 캔디를 주면 둘의 sha1 해쉬는 같아야하지만, 둘 자체는 달라야 한다고 한다.

구글이 발표한 sha1 해시 충돌이 일어나는 pdf 파일 2개를 보내주면 되는데 (출처 : https://shattered.io/) , 사이즈가 너무 클 뿐만 아니라 중간에 개행까지 섞여있어 제대로 입력을 넣을 수 없다.

찾아보니 해쉬 충돌을 유발하는 헤더가 중요하므로, 헤더( ~ 0x00000130 )를 포함하여 적절한 크기로 잘라서 초콜릿과 캔디를 보내주면 FLAG를 얻을 수 있다. (nc로 보내는데 사용한 python 코드 첨부)



FLAG는 HCTF{7he_thre4t_if_1_am_n0t_9iven_a_g1ft:)}



3) crypto_CCC



stage1)Gl apwnrmepynfw, y Aycqyp agnfcp, yjqm ilmul yq Aycqyp'q agnfcp, rfc qfgdr agnfcp, Aycqyp'q ambc mp Aycqyp qfgdr, gq mlc md rfc qgknjcqr ylb kmqr ugbcjw ilmul clapwnrgml rcaflgoscq.

카이사르 암호는 알파벳을 일정한 간격만큼 원형으로 밀어서 암호화를 하는 것이므로, 다시 그 간격만큼 당기면 원문을 알 수 있다.

영어문장에서 ` 뒤에 한글자만 오는 것은 소유격 s 일 확률이 높으므로 q에서 s까지 간격인 2글자를 밀어주었더니 원문을 얻었다.

원문은 In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques.



stage2)IJQXGZJTGIQGS4ZAN5XGKIDPMYQHGZLWMVZGC3BAMJQXGZJAGMZCA5DSMFXHGZTFOIQGK3TDN5SGS3THOMXA====

BASE 인코딩에는 16,32,64 등등이 있는데 여기서는 A-Z0-9 범위의 문자들만 사용되었으니 BASE32일 확률이 높아서 python을 통해 b32decode를 해보니 원문을 얻었다.

원문은 Base32 is one of several base 32 transfer encodings.



stage3) kimchi diet & donerts game is gym anyware & anytime!

Null 이라는 게 이 암호에 대한 정보가 없다는 줄 알았다가 검색해보니 Null Cipher 라는 게 있었다. 원문에다 평범한 단어를 섞어서 암호문이라고 인식하기 어렵게 만드는 것이라는 것과

주로 단어의 첫번째, 마지막 단어 또는 일정한 규칙을 가지고 단어나 글자를 선택하면 원문을 볼 수 있다는 것을 알게 되었다.



주어진 암호문에서 특수문자를 제외고 단어의 1,2,3,1,2,3,1,2 번째 글자를 가져와서 붙여보니 원문을 얻었다.

원문은 kingsman



FLAG로 주어진 것은 WFNKVntqeHVodV80aHVfYzRkb19zMXFpaXlzcWJfczFmeHVoaV8xZF9qeHVfbTBoYnR9

아무리 봐도 FLAG 형식은 아니다. 무언가 처리가 되어있다고 판단, 일단 A-Za-z0-9 범위의 문자열이니 BASE64 처리가 되지 않았을까 추측하여 python으로 b64decode를 하니 중간 암호문을 얻었다.



중간 암호문은 XSJV{jxuhu_4hu_c4do_s1qiiysqb_s1fxuhi_1d_jxu_m0hbt}



알파벳 4글자 + 괄호로 쌓인 문자열이 나온 것으로 보아 FLAG 형식은 얼추 맞는 것 같은데 알파벳이 맞지 않다. 이전 암호문이 BASE** 인 stage2와 관련이 있었으니 이번에는 stage1의 카이사르 암호와 관련이 있다고 판단.

대회 FLAG 형식인 HCTF에 맞춰서 X와 H 사이의 간격인 10글자를 밀어보니 진짜 FLAG를 얻을 수 있었다.



진짜 FLAG는 HCTF{there_4re_m4ny_c1assical_c1phers_1n_the_w0rld}





bonus)

1)Loveletter



스테가노그래피인 줄 알고 Hex 에디터로 열어보았으나 파일 끝부분에는 아무것도 적혀있지 않았다.

따라서 사진 자체에 숨겨져 있을 것으로 판단했다.

그림판으로 페인트통을 사용해 배경 부분을 다른 색으로 칠하니 FLAG를 얻을 수 있었다.



FLAG는 HCTF{WILL_YOU_MARRY_ME......???}



2) where_is_he

모자이크 되어있지 않은 간판 중 서초동연가를 검색해서 거리뷰로 비슷한 거리를 찾는 휴리스틱 알고리즘 (노가다) 을 돌리니 사당역 근처의 서초동 연가라는 것을 알 수 있었다.



FLAG는 HCTF{사당역}

