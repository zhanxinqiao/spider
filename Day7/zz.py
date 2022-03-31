import re

ss='                                　　一粒尘可填海，一根草斩尽日月星辰，弹指间天翻地覆。'
print(re.findall(r'([\u4e00-\u9fa5].*)',ss))