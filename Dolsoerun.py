import discord
import asyncio
import random
import os
import pickle
import random
from overwatch import *
# 가위바위보 전적

client = discord.Client()
@client.event
async def onn_ready():
    print("돌쇠 인사 오지게 박습니다.")
    print(client.user.name)
    print(clint.user.id)
    print('------')

money_horse = 1000 # 경마 기본 돈
i = 5
@client.event
async def on_message(message):
    global i
    x = random.randrange(1,101)
    z = random.randrange(0,3) # 러시안 룰렛 4가 데스
    n = ramdom.randrange(1,5) # 경마 말 숫자
    v = message.content
    if message.content.startswith('!명령어'):
        await client.send_message(message.channel, '#은 빼 주세요.') 
        await client.send_message(message.channel, '#79식, #버전, #명령어') 
        await client.send_message(message.channel, '#보이루, #방구리, #안냥, #ㅋㅋㅋㅋ')
        await client.send_message(message.channel, '#끝말잇기, #춤추는애벌레, #코그모따까리')
        await client.send_message(message.channel, '#위키[검색], #구글,#!돌쇠,#짜잔')
        await client.send_message(message.channel, '#깐뜨롤, #!가위,#!바위,#!보')
        await client.send_message(message.channel, '#경마, #경마_현재돈')
    elif message.content.startswith('................ㅠㅗㅓㅓㄴ언엊벼ㅡㄴ월ㅇㅗ너ㅣ로ㅠㅂㅈㄷ,ㅡㅈㅂㅜㅁㅇㄴㄹㄻㄴㅁㄹㅀㅁㅇ'):
        await client.send_message(message.channel, '......')
    elif message.content.startswith('버전'):
        await client.send_message(message.channel, '돌쇠봇 4호기.')
    elif message.content.startswith('보이루'):
        await client.send_message(message.channel, '가조쿠이시군요.')
    elif message.content.startswith('방가방가'):
        await client.send_message(message.channel, '대감님 안녕하십니까.')
    elif message.content.startswith('반갑다냥'):
        await client.send_message(message.channel, '서새봄 방송봅시다.')
    elif message.content.startswith('안냥'):
        await client.send_message(message.channel, '대감님 안녕하십니까.')
    elif message.content.startswith('ㅋㅋㅋㅋ'):
        await client.send_message(message.channel, 'ㅋㅋㅋ')
    elif message.content.startswith('79식'):
        await client.send_message(message.channel, '최고!')
    elif message.content.startswith('방구리'):
        await client.send_message(message.channel, '중2병 호구 새퀴 + 리퍼 장인(?)')
    elif message.content.startswith('춤추는애벌레'):
        await client.send_message(message.channel, 'http://www.op.gg/summoner/userName=춤추는애벌레')
    elif message.content.startswith('방스터'):
        await client.send_message(message.channel, 'http://www.op.gg/summoner/userName=방스터')
    elif message.content.startswith('남은챔피언'):
        await client.send_message(message.channel, 'http://www.op.gg/summoner/userName=남은챔피언')
    elif message.content.startswith('코그모따까리'):
        await client.send_message(message.channel, '중2병 호구새퀴 저격수')
    elif message.content.startswith('깐뜨롤'):
        await client.send_message(message.channel, '보도우 장인')
    elif message.content.startswith('!돌쇠'):
        await client.send_message(message.channel, '돌쇠봇의 대감이')
    elif message.content.startswith('쩝쩝'):
        await client.send_message(message.channel, '쩝쩝쩝쩝....')
    elif message.content.startswith('그래 그리 쉽지는 않겠지'):
        await client.send_message(message.channel, '불편;;')
    elif message.content.startswith('그런데'):
        await client.send_message(message.channel, '짜잔! 절대란건 없군요')
    elif message.content.startswith('가즈아'):
        await client.send_message(message.channel, '가즈아ㅏㅏㅏ')
    elif message.content.startswith('옵치전적'):
        hero_time = Overwatch(battletag = v[4:], mode = 'play_time')
        results = hero_time()
        await client.send_message(message.channel, str(results))
    elif message.content.startswith('수정요청'):
        await client.send_message(message.channel, 'https://github.com/eogkswkd/DolsoeBot/blob/master/Dolsoerun.py')
    elif message.content.startswith('위키'):
        while v.find(' ') != -1:
            v = v.replace(' ','%20')
        await client.send_message(message.channel, 'https://namu.wiki/w/' + v[2:])
    elif message.content.startswith('구글'):
        while v.find(' ') != -1:
            v = v.replace(' ','%20')
        await client.send_message(message.channel, 'https://www.google.co.kr/search?q=' + v[2:])
    elif message.content.startswith('!주사위'):
        if x == 100:
            await client.send_message(message.channel, '돌쇠봇이 무조건 확실히 정확하게 보증합니다. 주사위가 ' + str(x) + '나왔습니다!!')
        elif x == 80:
            await client.send_message(message.channel, '돌쇠봇이 보증합니다. 주사위가' + str(x) + '나왔습니다!!')
        elif x >= 60:
            await client.send_message(message.channel, '축하드립니다! 폭풍같은 결과입니다. ' + str(x) + '입니다!')
        elif x >= 40:
            await client.send_message(message.channel, '컴퓨터를 던져 주사위를 굴렸으나 ' + str(x) + '나왔습니다...')
        elif x >= 20:
            await client.send_message(message.channel, '주사위는 별로 잘못이 없습니다. 유감스럽게도 ' + str(x) + '입니다...')
        else:
            await client.send_message(message.channel, '재미없이 망이네요. 주사위가 ' + str(x) + '나왔습니다...')
# 가위 바위 보        
    elif message.content.startswith('!가위'):
        rate = random.randrange(0,3) # 0 가위     1 주먹      2 보
        if rate == 0:
            await client.send_message(message.channel, "비겼습니다. 저도 '가위'입니다.")
        elif rate == 1:
                await client.send_message(message.channel, '''하하 제가 이겼습니다. '바위'거든요.''')
        else:
            await client.send_message(message.channel, '''오 제가 졌습니다. '보'거든요''')
    elif message.content.startswith('!바위'):
        rate = random.randrange(0,3) # 0 가위     1 주먹      2 보
        if rate == 0:
            await client.send_message(message.channel, '''졌습니다. 저는 '가위'입니다.''')
        elif rate == 1:
                await client.send_message(message.channel, '''하하 제가 이겼습니다. '보'거든요.''')
        else:
            await client.send_message(message.channel, '''오 제가 이겼습니다. '보'거든요''')
    elif message.content.startswith('!보'):
        rate = random.randrange(0,3) # 0 가위     1 주먹      2 보
        if rate == 0:
            await client.send_message(message.channel, '''비겼습니다. 저도 '보'입니다.''')
        elif rate == 1:
                await client.send_message(message.channel, '''하하 제가 이겼습니다. '가위'거든요.''')
        else:
            await client.send_message(message.channel, '''오 제가 졌습니다. '바위'거든요''')

#러시안 룰렛
    elif message.content.startswith('러시안룰렛'):
        if z == 2:
            await client.send_message(message.channel, '당신은 사망했습니다.')
            i = 5
        elif i == 1:
            await client.send_message(message.channel, '당신은 사망했습니다.')
            i = 5
        elif i == 2:
            await client.send_message(message.channel, '아직 한 발 남았다.')
        else:
            await client.send_message(message.channel, '당신은 생존했습니다.')
            i -= 1
            await client.send_message(message.channel, '총은 ' + str(i) + '발 남았습니다.')
 
#경마
    elif message.contwnt.startswith('경마'):
    	await client.send_message(message.channel, '경마게임이 시작됩니다.  배팅 금액은 100원입니다. 승리시 500원을 얻습니다. 말을 선택해 주세요. ex.1번말')
   	 elif message.content.startswith('1번말'):
   	 	money_horse = money_horse - 100
   	 	horse = randrange(1,5)
   	 	if horse == 1: #{0} 이런거 써서 단축시킬 수 있을거 같은데 까먹었다.
   	 		await client.send_message(message.channel, '1번말이 1등으로 들어왔습니다!')
   	 		money_horse = money_horse + 600
   	 	elif horse == 2:
   	 		await client.send_message(message.channel, '2번말이 1등으로 들어왔네요.')
   	 	elif horse == 3:
   	 		await client.send_message(message.channel, '3번말이 1등으로 들어왔네요.')
   	 	elif horse == 4:
   	 		await client.send_message(message.channel, '4번말이 1등으로 들어왔네요.')
   	 	elif horse == 4:
   	 		await client.send_message(message.channel, '5번말이 1등으로 들어왔네요.')

   	  elif message.content.startswith('2번말'):
   	 	horse = randrange(1,5)
   	 	money_horse = money_horse - 100
   	 	if horse == 1: 
   	 		await client.send_message(message.channel, '1번말이 1등으로 들어왔네요')
   	 	elif horse == 2:
   	 		await client.send_message(message.channel, '2번말이 1등으로 들어왔습니다!')
   	 		money_horse = money_horse + 600
   	 	elif horse == 3:
   	 		await client.send_message(message.channel, '3번말이 1등으로 들어왔네요.')
   	 	elif horse == 4:
   	 		await client.send_message(message.channel, '4번말이 1등으로 들어왔네요.')
   	 	elif horse == 4:
   	 		await client.send_message(message.channel, '5번말이 1등으로 들어왔네요.')

   	  elif message.content.startswith('2번말'):
   	 	horse = randrange(1,5)
   	 	money_horse = money_horse - 100
   	 	if horse == 1: 
   	 		await client.send_message(message.channel, '1번말이 1등으로 들어왔습니다!')
   	 	elif horse == 2:
   	 		await client.send_message(message.channel, '2번말이 1등으로 들어왔네요.')
   	 		money_horse = money_horse + 600
   	 	elif horse == 3:
   	 		await client.send_message(message.channel, '3번말이 1등으로 들어왔네요.')
   	 	elif horse == 4:
   	 		await client.send_message(message.channel, '4번말이 1등으로 들어왔네요.')
   	 	elif horse == 4:
   	 		await client.send_message(message.channel, '5번말이 1등으로 들어왔네요.')
   	 			

   	 elif message.content.startswith('3번말'):
   	 	horse = randrange(1,5)
   	 	money_horse = money_horse - 100
   	 	if horse == 1: 
   	 		await client.send_message(message.channel, '1번말이 1등으로 들어왔네요.')
   	 	elif horse == 2:
   	 		await client.send_message(message.channel, '2번말이 1등으로 들어왔네요.')
   	 		money_horse = money_horse + 600
   	 	elif horse == 3:
   	 		await client.send_message(message.channel, '3번말이 1등으로 들어왔습니다!')
   	 	elif horse == 4:
   	 		await client.send_message(message.channel, '4번말이 1등으로 들어왔네요.')
   	 	elif horse == 4:
   	 		await client.send_message(message.channel, '5번말이 1등으로 들어왔네요.')

   	  elif message.content.startswith('4번말'):
   	 	horse = randrange(1,5)
   	 	money_horse = money_horse - 100
   	 	if horse == 1: 
   	 		await client.send_message(message.channel, '1번말이 1등으로 들어왔네요.')
   	 	elif horse == 2:
   	 		await client.send_message(message.channel, '2번말이 1등으로 들어왔네요.')
   	 		money_horse = money_horse + 600
   	 	elif horse == 3:
   	 		await client.send_message(message.channel, '3번말이 1등으로 들어왔네요.')
   	 	elif horse == 4:
   	 		await client.send_message(message.channel, '4번말이 1등으로 들어왔습니다!')
   	 	elif horse == 4:
   	 		await client.send_message(message.channel, '5번말이 1등으로 들어왔네요.')

   	  elif message.content.startswith('5번말'):
   	 	horse = randrange(1,5)
   	 	money_horse = money_horse - 100
   	 	if horse == 1: 
   	 		await client.send_message(message.channel, '1번말이 1등으로 들어왔네요.')
   	 	elif horse == 2:
   	 		await client.send_message(message.channel, '2번말이 1등으로 들어왔네요.')
   	 		money_horse = money_horse + 600
   	 	elif horse == 3:
   	 		await client.send_message(message.channel, '3번말이 1등으로 들어왔네요.')
   	 	elif horse == 4:
   	 		await client.send_message(message.channel, '4번말이 1등으로 들어왔네요.')
   	 	elif horse == 4:
   	 		await client.send_message(message.channel, '5번말이 1등으로 들어왔습니다!')

    elif message.startswith('경마_현재돈'):
    	await client.send_message(message.channel, '현재 돈은 '+ str(money_horse) +' 원입니다.')
    elif message.startswith('경마_돈추가'):
    	money_horse = money_horse + 1000


    if message.content.startswith('그만 쪼개'):
        await client.send_message(message.channel, '네;;;')
        await asyncio.sleep(5)
        await client.send_message(message.channel, '이제 사용하실 수 있습니다.')
client.run('Mzk1NDgzNDEyMzAwODI0NTc2.DSTi2w.S7rxqzwuu_356ieRqW3TK9EsB4s')
