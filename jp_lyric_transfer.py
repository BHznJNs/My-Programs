import pykakasi
from janome.tokenizer import Tokenizer

# pykakasi
kks = pykakasi.kakasi()
convert = kks.convert
# janome
t = Tokenizer()
# 处理日文字符
'''特殊符号'''
symbols = ('、', '。', '’', 
            '”', '｛', '｝',
            '「', '」', 'ー',
            '＝', '_', '+',
            '/', '*', '-',
            '(', ')')
# 日文处理函数
def dealwith(jp):
	# 按行划分
	jp_list = jp.split('\n')

	result_roma = ''

	for jl in jp_list:
		if jp_list.index(jl) % 2 != 0:
			result_roma += jl + '\n'
			for token in t.tokenize(jl):
				string = str(token)
				origin = string.split('\t')[0]

				if string.split(',')[-1] != '*':
					roma = convert(string.split(',')[-1])[0]['hepburn']
				else:
					roma = convert(origin)[0]['hepburn']
				
				result_roma += roma + ' '
		else:
			result_roma += jl
		
		# 行尾换行
		result_roma += '\n'
	return result_roma

print(dealwith('''
幽霊になった僕は、明日遠くの君を見に行くんだ
已是幽灵的我 明天要去见遥远的你
その後はどうしよう
在那之后该怎么办呢
きっと君には言えない
一定无法对你说出口
幽霊になった僕は、夏の終わり方を見に行くんだ
已是幽灵的我 要去见夏日的终末
六畳の地球で 浅い木陰のバス停で
在六叠大的地球 在浅浅树荫下的公交站
夜に涼む君の手 誘蛾灯に沿って石を蹴った
于夜纳凉的你的手 沿着诱蛾灯踢开石子
街の薄明かりが揺れている
街道里薄弱灯火摇摇曳曳
何も見えなくたって
即便什么也不能看见
何も言わなくたって
即便什么也说不出口
誰も気付かなくたって
即便谁也没能察觉到
それでもわかるから
即便如此我也明白的啊
君と座って バス停見上げた空が青いことしかわからずに
与你坐着 只知道公交站仰望的天空是如此湛蓝
雲が遠いね ねえ
云朵很遥远呐 话说
夜の雲が高いこと、本当不思議だよ
夜空云朵的高阔 真的很不可思议呢
だからさ、もういいんだよ
所以啊 已经没关系了啊
幽霊になった僕は、あの頃の景色を見に行くんだ
已是幽灵的我 要去看那时候的景色
遠い街の海辺 子供のとき見た露店街
遥远小镇的海边 孩童时期发现的地摊街
歩き疲れた脚でそこらのベンチでバスを待って
荡着疲惫的双脚在那长椅上等着巴士
その後はどうしよう
在那之后怎么办呢
何で歩いてたんだろう
为什么会一直走着呢
何も知らなくたって
即便什么都无法知道
何も聞けなくたって
即便什么都无法听到
いつか君が忘れても
总有一天你会忘怀
それでも見ているから
即便这样我也会注视着你
夏の陰に座って 入道雲を眺めるだけでどこか苦しくて
坐于夏阴 只是眺望积雨云而已某处便会感到痛苦
空が高いよ ねえ
天空真高呢 呐
このままずっと遠くに行けたらいいのにな
就这样一直朝着远方走下去就好了吗
夜しかもう眠れずに
只有夜晚才可安眠
君と座って バス停見上げた空が青いことしかわからずに
与你坐着 只知道公交站仰望的天空是如此湛蓝
雲が遠いね ねえ
云朵很遥远呐 话说
夜の雲が高いこと、本当不思議だよ
夜空云朵的高阔 真的很不可思议呢
だからさ、だからさ
所以啊 所以啊
君もさ、もういいんだよ
你也是啊 已经没关系了啊
幽霊になった僕は、明日遠くの君を見に行くんだ
已是幽灵的我 明天要去见遥远的你
その後はどうだろう
在那之后会怎样呢
きっと君には見えない
你一定也无法看见
'''))

