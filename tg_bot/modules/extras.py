import random, re
from random import randint
from telegram import Message, Update, Bot, User
from telegram import MessageEntity
from telegram.ext import Filters, MessageHandler, run_async

from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler

ABUSE_STRINGS = (
    "Me gali nhi dunga ye ban kardenge",
    "Chup! Machar",
    "me kuch nhi bolunge muje ban kardenge",
    "Hurrr nikl pehli fursat me",
    "Lol Nikl",
    "Nigga",
    "Ur granny tranny",
    "you noob",
	"Relax your Rear,ders nothing to fear,The LOL train is finally here",
	"wo h kya",
	"LOL papa ko gali do jakr",
	"sad"
    "CUnt",
    " LOL is here",
    "Ur dad LoL nikl"
)

EYES = [
    ['⌐■', '■'],
    [' ͠°', ' °'],
    ['⇀', '↼'],
    ['´• ', ' •`'],
    ['´', '`'],
    ['`', '´'],
    ['ó', 'ò'],
    ['ò', 'ó'],
    ['⸌', '⸍'],
    ['>', '<'],
    ['Ƹ̵̡', 'Ʒ'],
    ['ᗒ', 'ᗕ'],
    ['⟃', '⟄'],
    ['⪧', '⪦'],
    ['⪦', '⪧'],
    ['⪩', '⪨'],
    ['⪨', '⪩'],
    ['⪰', '⪯'],
    ['⫑', '⫒'],
    ['⨴', '⨵'],
    ['⩿', '⪀'],
    ['⩾', '⩽'],
    ['⩺', '⩹'],
    ['⩹', '⩺'],
    ['◥▶', '◀◤'],
    ['◍', '◎'],
    ['/͠-', '┐͡-\\'],
    ['⌣', '⌣”'],
    [' ͡⎚', ' ͡⎚'],
    ['≋'],
    ['૦ઁ'],
    ['  ͯ'],
    ['  ͌'],
    ['ළ'],
    ['◉'],
    ['☉'],
    ['・'],
    ['▰'],
    ['ᵔ'],
    [' ﾟ'],
    ['□'],
    ['☼'],
    ['*'],
    ['`'],
    ['⚆'],
    ['⊜'],
    ['>'],
    ['❍'],
    ['￣'],
    ['─'],
    ['✿'],
    ['•'],
    ['T'],
    ['^'],
    ['ⱺ'],
    ['@'],
    ['ȍ'],
    ['  '],
    ['  '],
    ['x'],
    ['-'],
    ['$'],
    ['Ȍ'],
    ['ʘ'],
    ['Ꝋ'],
    [''],
    ['⸟'],
    ['๏'],
    ['ⴲ'],
    ['◕'],
    ['◔'],
    ['✧'],
    ['■'],
    ['♥'],
    [' ͡°'],
    ['¬'],
    [' º '],
    ['⨶'],
    ['⨱'],
    ['⏓'],
    ['⏒'],
    ['⍜'],
    ['⍤'],
    ['ᚖ'],
    ['ᴗ'],
    ['ಠ'],
    ['σ'],
    ['☯']
]

MOUTHS = [
    ['v'],
    ['ᴥ'],
    ['ᗝ'],
    ['Ѡ'],
    ['ᗜ'],
    ['Ꮂ'],
    ['ᨓ'],
    ['ᨎ'],
    ['ヮ'],
    ['╭͜ʖ╮'],
    [' ͟ل͜'],
    [' ͜ʖ'],
    [' ͟ʖ'],
    [' ʖ̯'],
    ['ω'],
    [' ³'],
    [' ε '],
    ['﹏'],
    ['□'],
    ['ل͜'],
    ['‿'],
    ['╭╮'],
    ['‿‿'],
    ['▾'],
    ['‸'],
    ['Д'],
    ['∀'],
    ['!'],
    ['人'],
    ['.'],
    ['ロ'],
    ['_'],
    ['෴'],
    ['ѽ'],
    ['ഌ'],
    ['⏠'],
    ['⏏'],
    ['⍊'],
    ['⍘'],
    ['ツ'],
    ['益'],
    ['╭∩╮'],
    ['Ĺ̯'],
    ['◡'],
    [' ͜つ']
]

EARS = [
    ['q', 'p'],
    ['ʢ', 'ʡ'],
    ['⸮', '?'],
    ['ʕ', 'ʔ'],
    ['ᖗ', 'ᖘ'],
    ['ᕦ', 'ᕥ'],
    ['ᕦ(', ')ᕥ'],
    ['ᕙ(', ')ᕗ'],
    ['ᘳ', 'ᘰ'],
    ['ᕮ', 'ᕭ'],
    ['ᕳ', 'ᕲ'],
    ['(', ')'],
    ['[', ']'],
    ['¯\\_', '_/¯'],
    ['୧', '୨'],
    ['୨', '୧'],
    ['⤜(', ')⤏'],
    ['☞', '☞'],
    ['ᑫ', 'ᑷ'],
    ['ᑴ', 'ᑷ'],
    ['ヽ(', ')ﾉ'],
    ['\\(', ')/'],
    ['乁(', ')ㄏ'],
    ['└[', ']┘'],
    ['(づ', ')づ'],
    ['(ง', ')ง'],
    ['⎝', '⎠'],
    ['ლ(', 'ლ)'],
    ['ᕕ(', ')ᕗ'],
    ['(∩', ')⊃━☆ﾟ.*'],
]

TOSS = (
    "Heads",
    "Tails",
)--

TDS = (
    "1",
    "2",
    "3",
    "4",
    "5",
)

@run_async
def roll(bot: Bot, update: Update):
    update.message.reply_text(random.choice(range(1, 7)))

    
 #TDS idar se start hoga  
@run_async
def tds2(bot: Bot, update: Update):
    update.message.reply_text(random.choice(range(1, 2)))

@run_async
def tds3(bot: Bot, update: Update):
    update.message.reply_text(random.choice(range(1, 3)))

@run_async
def tds4(bot: Bot, update: Update):
    update.message.reply_text(random.choice(range(1, 4)))

@run_async
def tds5(bot: Bot, update: Update):
    update.message.reply_text(random.choice(range(1, 5)))        
	
def toss(bot: Bot, update: Update):
    update.message.reply_text(random.choice(TOSS))

@run_async
def abuse(bot: Bot, update: Update):
    # reply to correct message
    reply_text = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_text(random.choice(ABUSE_STRINGS))
	
@run_async
def shrug(bot: Bot, update: Update):
    # reply to correct message
    reply_text = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_text("¯\_(ツ)_/¯")	
	
@run_async
def bluetext(bot: Bot, update: Update):
    # reply to correct message
    reply_text = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_text("BLUE TEXT\n MUST CLICK\n I AM A STUPID ANIMAL THAT IS ATTRACTED TO COLORS")		

@run_async
def rlg(bot: Bot, update: Update):
    # reply to correct message
    eyes = random.choice(EYES)
    mouth = random.choice(MOUTHS)
    ears = random.choice(EARS)
    repl = format(ears + eyes + mouth + eyes + ears)
    update.message.reply_text(repl)

@run_async
def doom(bot: Bot, update: Update):
    # reply to correct message
    reply_text = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_text("Doom\n Vishali...\n Aur Nilam ki ma ka EX...")		


@run_async
def sam(bot: Bot, update: Update):
    # idhar se response jayega
    reply_text = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_text("@AmateurChatter\n Sam...\n Choti.....")		


@run_async
def bhagwan(bot: Bot, update: Update):
    # reply to correct message
    reply_text = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_text("@devil0707\n Shanti wale...\n ye bhagwan h...")		



@run_async
def bossraja(bot: Bot, update: Update):
    # reply to correct message
    reply_text = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_text("Boss Raja\n Ye pata nhi kon h \n all i know is that he is A GOOD PERSON...")		



@run_async
def nilam(bot: Bot, update: Update):
    # idhar se response jayega
    reply_text = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_text("Vishali😘😘 ka bhai\n DOOM iski ma ka EX...\n ye 5th gender h...")		



@run_async
def mmiska(bot: Bot, update: Update):
    # idhar se response jayega
    reply_text = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_text("Miska\n choti behen ...\n No abuse wale...")		



@run_async
def cool(bot: Bot, update: Update):
    # idhar se response jayega
    reply_text = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_text("Rahul Cool\n chota bhai ...\n paisey wale bhaiya...")		



@run_async
def smoke(bot: Bot, update: Update):
    # idhar se response jayega
    reply_text = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_text("Dhua lol\n chota bhai ...\n isko GF dila do🥺...")		



@run_async
def rudhra(bot: Bot, update: Update):
    # idhar se response jayega
    reply_text = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_text("Rudhra😛 \n Chota bhai ...\n isko tu tadak nhu pasand😁😁...")		



@run_async
def hardik(bot: Bot, update: Update):
    # idhar se response jayega
    reply_text = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_text("RAHUL GHANDI LOL😛 \n Ghanti bolta h ye muje lol ...\n Isko thapado se marna h ek din😁😁...")

		

@run_async
def lonelyloki(bot: Bot, update: Update):
    # idhar se response jayega
    reply_text = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_text("Is lawde ka name hi kyu lete ho yaar \n ye wo h jo apne pita ji ke ASHLEELTA ke nakshey kadam pe chal rha h ...\n iski VISHALI😍😍😘😘...")



def decide(bot: Bot, update: Update):
        r = randint(1, 100)
        if r <= 65:
            update.message.reply_text("Yes.")
        elif r <= 90:
            update.message.reply_text("NoU.")
        else:
            update.message.reply_text("Maybe.")


            
def table(bot: Bot, update: Update):
            r = randint(1, 100)
            if r <= 45:
                update.message.reply_text("(╯°□°）╯彡 ┻━┻")
            elif r <= 90:
                update.message.reply_text("LOL NIKL pehli fursat me")
            else:
                update.message.reply_text("Go do some work instead of flippin tables you helpless fagit.")
		
__help__ = """
 - /shrug : get shrug XD.
 - /table : get flip/unflip :v.
 - /decide : Randomly answers yes/no/maybe
 - /toss : Tosses A coin
 - /abuse : Abuses the cunt
 - /tts <any text> : Converts text to speech
 - /bluetext : check urself :V
 - /roll : Roll a dice.
 - /rlg : Join ears,nose,mouth and create an emo ;-;
 - /zal <any text> : zalgofy! your text
 - /doom : will return information 'bout the boss
 - /sam : will return information 'bout SAM
 - /bhagwan : will return information 'bout BHAGWAN
 - /nilam : will return information 'bout madrchod Nilam (lonely loki)
 - /bossraja : will return information about boss raja 
 - /mmiska : will return information about Miska
 - /cool : will return information about rahul cool
 - /smoke : wil return information about smoke 
 - /rudhra : will return information about rudhra
 - /hardik : will return infirmation about Hardik chaudhary
 - /lonelyloki : will return information 'bout Nilam lonelyloki
 Lyrics pluggin bhi arha h boht jald GENUIS ke API se.
"""

__mod_name__ = "Extras"

ROLL_HANDLER = DisableAbleCommandHandler("roll", roll)
TOSS_HANDLER = DisableAbleCommandHandler("toss", toss)
SHRUG_HANDLER = DisableAbleCommandHandler("shrug", shrug)
BLUETEXT_HANDLER = DisableAbleCommandHandler("bluetext", bluetext)
RLG_HANDLER = DisableAbleCommandHandler("rlg", rlg)
DECIDE_HANDLER = DisableAbleCommandHandler("decide", decide)
TABLE_HANDLER = DisableAbleCommandHandler("table", table)
DOOM_HANDLER = DisableAbleCommandHandler("doom", doom)
ABUSE_HANDLER = DisableAbleCommandHandler("abuse", abuse)
SAM_HANDLER = DisableAbleCommandHandler("sam", sam)
BHAGWAN_HANDLER = DisableAbleCommandHandler("bhagwan", bhagwan)
NILAM_HANDLER = DisableAbleCommandHandler("nilam", nilam)
BOSSRAJA_HANDLER = DisableAbleCommandHandler("bossraja", bossraja)
MMISKA_HANDLER = DisableAbleCommandHandler("mmiska", mmiska)
COOL_HANDLER = DisableAbleCommandHandler("cool", cool)
SMOKE_HANDLER = DisableAbleCommandHandler("smoke", smoke)
RUDHRA_HANDLER = DisableAbleCommandHandler("rudhra", rudhra)
HARDIK_HANDLER = DisableAbleCommandHandler("hardik", hardik)
LONELYLOKI_HANDLER = DisableAbleCommandHandler("lonelyloki", lonelyloki)
TDS2_HANDLER = DisableAbleCommandHandler("tds2", tds2)
TDS3_HANDLER = DisableAbleCommandHandler("tds3", tds3)
TDS4_HANDLER = DisableAbleCommandHandler("tds4", tds4)
TDS5_HANDLER = DisableAbleCommandHandler("tds5", tds5)




dispatcher.add_handler(ROLL_HANDLER)
dispatcher.add_handler(TOSS_HANDLER)
dispatcher.add_handler(SHRUG_HANDLER)
dispatcher.add_handler(BLUETEXT_HANDLER)
dispatcher.add_handler(RLG_HANDLER)
dispatcher.add_handler(DECIDE_HANDLER)
dispatcher.add_handler(TABLE_HANDLER)
dispatcher.add_handler(DOOM_HANDLER)
dispatcher.add_handler(ABUSE_HANDLER)
dispatcher.add_handler(SAM_HANDLER)
dispatcher.add_handler(BHAGWAN_HANDLER)
dispatcher.add_handler(NILAM_HANDLER)
dispatcher.add_handler(BOSSRAJA_HANDLER)
dispatcher.add_handler(MMISKA_HANDLER)
dispatcher.add_handler(COOL_HANDLER)
dispatcher.add_handler(SMOKE_HANDLER)
dispatcher.add_handler(RUDHRA_HANDLER)
dispatcher.add_handler(HARDIK_HANDLER)
dispatcher.add_handler(LONELYLOKI_HANDLER)
dispatcher.add_handler(TDS2_HANDLER)
dispatcher.add_handler(TDS3_HANDLER)
dispatcher.add_handler(TDS4_HANDLER)
dispatcher.add_handler(TDS5_HANDLER)







