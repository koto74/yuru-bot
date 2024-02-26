import random

orochi_famous_saying_list = [
            'どっから見ても、誰とやっても、敗ける要素が一切見つからねぇ。　完成したんだよ、愚地流が',
            '俺の空手は後退のネジをはずしてあるんだよ…',
            'オレの空手は、ピストルの10倍スリリングだぞ',
            '矢でも鉄砲でも火炎放射器でも持ってこいやァ…',
            '美意識だ。たとえ一握りの砂、一本の鉛筆であろうとも、闘う以前に手にしたなら、武道家の誇りは崩れ去る。',
            '人間生きてりゃ飯も喰えば酒も飲むんだ。ケガもするし病気もするだろうよ。　ベストコンディションなんて望むべくもねぇ……それがこっちの世界だぜ。',
            ]

async def handle_orochi(message):
    await message.channel.send(random.choice(orochi_famous_saying_list))
