import pygame
import sys
import asyncio
import os

pygame.init()
print("CWD:", os.getcwd())
print("Files:", os.listdir("."))
# Set up window
infoObject = pygame.display.Info()
screen_width = infoObject.current_w
screen_height = infoObject.current_h
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("(not) Undertale")
clock = pygame.time.Clock()

anothervariable = False
taketwo2 = False
previoushp = 99
firstime = False
doattack1p2 = False
holdup = False 
doattack1 = False
first_menu_movement = 0
second_menu_movement = False
positioninfirst_menu = 1
positioninact_menu = 1
positioninitem_menu = 1 # make it fail in some way
positioninspare_menu = 1
goodleftmenupositiony = 0
goodleftmenupositionx = 0
battleattacks = 0
duringbattle = False


illdothislater = "temp"

onetime = False
showthewordscheck = False
in_menu = True
soul_free_move = not in_menu
menu1_move = True
menu2_move = False
onspare = False
placemercyfailontop = False
placemercyfailontop2 = False
oncheck = False
showtheactualcheckwords = False
endcheck = False
anothercheckflag = False
startfight = False
continuefight = False
checkx = False
turnoff = False
menurestart = False
attacknumber = 0
# Player setup
player_size = 16
player_speed = 5
button_width = 100
button_height = 40
player_rect = pygame.Rect(screen_width // 2, screen_height // 2, player_size, player_size)

player_image = pygame.image.load(r"soul.gif").convert_alpha()
player_image = pygame.transform.scale(player_image, (player_size, player_size))
player_visible = True

def make_image(path, width, height):
    path = str(path)
    temp_image = pygame.image.load(path).convert_alpha()
    temp_image = pygame.transform.scale(temp_image, (width, height))
    return temp_image

# Distance from bottom of screen (e.g., 10% from bottom)
vertical_offset = int(screen_height * 0.1)

# Horizontal spacing between buttons as a ratio of screen width
button_spacing = int(screen_width * 0.02)

# Total width of all buttons + spacing
total_width = 4 * button_width + 3 * button_spacing

# Start x so that the whole row is centered horizontally
start_x = (screen_width - total_width) // 2
y_pos = screen_height - vertical_offset - button_height
battlebox_width = screen_width // 3.5
battlebox_height = screen_height // 3.5
battlebox_x = (screen_width - battlebox_width) // 2 + 10
battlebox_y = y_pos - battlebox_height - 40  # 20px gap above buttons
dialoguebox_height = screen_height // 5
dialoguebox_y = screen_height - (dialoguebox_height * 2)


ACT1_image = make_image(r"ACT_image.jpg", button_width, button_height)
ACT2_image = make_image(r"ACT_image.png", button_width, button_height)
FIGHT1_image = make_image(r"FIGHT_image.jpg", button_width, button_height)
FIGHT2_image = make_image(r"FIGHT_image.png", button_width, button_height)
SPARE1_image = make_image(r"MERCY_image.jpg", button_width, button_height)
SPARE2_image = make_image(r"MERCY_image.png", button_width, button_height)
ITEM1_image = make_image(r"ITEM_image.jpg", button_width, button_height)
ITEM2_image = make_image(r"ITEM_image.png", button_width, button_height)
DIALOGUEBOX_image = make_image(r"dialoguebox.png" , (button_width*5), dialoguebox_height)
BATTLEBOX_image = make_image(r"bb.png", battlebox_width, battlebox_height)
BATTLEBAR_image = make_image(r"FIGHTBAR.png", (button_width*4.9), dialoguebox_height)
ATTACK_image = make_image(r"5.png", 28, 68)
BLUEATTACK_image = make_image(r"6.png", 28, 68)
ORANGEATTACK_image = make_image(r"4.png", 28, 68)
opponent_image = make_image(r"idk.png", 192, 263)
player_mask = pygame.mask.from_surface(player_image)



def make_extra_rect(width_position, height_position, npc_width, npc_height):
    return pygame.Rect(width_position, height_position, npc_width, npc_height)
extra_rect = make_extra_rect(screen_width // 2, screen_height // 2 - screen_height // 4, player_size, player_size)



# Define rects
FIGHT_RECT = make_extra_rect(start_x, y_pos, button_width, button_height)
ACT_RECT = make_extra_rect(start_x + (button_width + button_spacing) * 1, y_pos, button_width, button_height)
ITEM_RECT = make_extra_rect(start_x + (button_width + button_spacing) * 2, y_pos, button_width, button_height)
MERCY_RECT = make_extra_rect(start_x + (button_width + button_spacing) * 3, y_pos, button_width, button_height)
BATTLEBOX_RECT = make_extra_rect(battlebox_x, battlebox_y, battlebox_width, battlebox_height)
DIALOGUEBOX_RECT = make_extra_rect(start_x * 0.98, dialoguebox_y, (button_width *5), dialoguebox_height)
BATTLEBAR_RECT = make_extra_rect(start_x * 0.998 - 1, dialoguebox_y, (button_width * 5), dialoguebox_height)
BATTLEBAR_BAR_RECT = make_extra_rect(start_x * 0.998 - 1 -1, dialoguebox_y +5, (button_width // 10 - 4), dialoguebox_height -7)
opponent_RECT = make_extra_rect(BATTLEBOX_RECT.centerx - 100, BATTLEBOX_RECT.top - 200, 193, 268)
ATTACK0_RECT = make_extra_rect(0, 0, 28, 68)
ATTACK_RECT = make_extra_rect(0, 0, 28, 68)
ATTACK2_RECT = make_extra_rect(0, 0, 28, 68)
ATTACK3_RECT = make_extra_rect(0, 0, 28, 68)
ATTACK4_RECT = make_extra_rect(0, 0, 28, 68)
ATTACK5_RECT = make_extra_rect(0, 0, 28, 68)
ATTACK6_RECT = make_extra_rect(0, 0, 28, 68)
ATTACK7_RECT = make_extra_rect(0, 0, 28, 68)
ATTACK8_RECT = make_extra_rect(0, 0, 28, 68)
ATTACK9_RECT = make_extra_rect(0, 0, 28, 68)
ATTACK10_RECT = make_extra_rect(0, 0, 28, 68)
ATTACK11_RECT = make_extra_rect(0, 0, 28, 68)
ATTACK12_RECT = make_extra_rect(0, 0, 28, 68)
ATTACK13_RECT = make_extra_rect(0, 0, 26, 68)
ATTACK14_RECT = make_extra_rect(0, 0, 28, 68)
ATTACK15_RECT = make_extra_rect(0, 0, 28, 68)
ATTACK16_RECT = make_extra_rect(0, 0, 28, 68)
ATTACK_RECTS = [ATTACK_RECT, ATTACK2_RECT, ATTACK3_RECT, ATTACK4_RECT, ATTACK5_RECT]       
BLUEATTACK_RECTS = [ATTACK6_RECT, ATTACK7_RECT, ATTACK8_RECT, ATTACK9_RECT, ATTACK10_RECT]   
ORANGEATTACK_RECTS = [ATTACK11_RECT, ATTACK12_RECT, ATTACK13_RECT, ATTACK14_RECT, ATTACK15_RECT, ATTACK16_RECT]
ATTACK0_image =ATTACK1_image= ATTACK2_image= ATTACK3_image= ATTACK4_image= ATTACK5_image = ATTACK_image
BLUEATTACK6_image = BLUEATTACK7_image = BLUEATTACK8_image = BLUEATTACK9_image = BLUEATTACK10_image  = BLUEATTACK_image
ORANGEATTACK11_image = ORANGEATTACK12_image = ORANGEATTACK13_image = ORANGEATTACK14_image = ORANGEATTACK15_image = ORANGEATTACK16_image = ORANGEATTACK_image


pygame.key.set_repeat(0)  # no repeats, one KEYDOWN per physical press


extra_visible = False
anothernextmove = False
ACT1_visible = True
ACT2_visible = False
FIGHT1_visible = True
FIGHT2_visible = False
SPARE1_visible = True
SPARE2_visible = False
ITEM1_visible = True
ITEM2_visible = False
ITEM_menu_visible = False
FIGHT_menu_visible = False
MERCY_menu_visible = False
ACT_menu_visible = False
DIALOGUE_BOX_visible = True
BATTLE_BOX_visible = False
BATTLEBAR_visible = False
workpls = False
placeopponent = False
startactualattacks = False
LOVE_visible = True
HP_visible = True
HEALTHBAR_visible = True
NAME_visible = True
HP_bar_visible = True
BATTLEBAR_BAR_visible = False
stoppablebar = False
MISSED_visible = False
MISSEDquestionmark_visible = False
battlestart = False
nextmove = False
ATTACK0_visible = False
ATTACK_visible = False
ATTACK2_visible = False
ATTACK3_visible = False
ATTACK4_visible = False
ATTACK5_visible = False
ATTACK6_visible = False
ATTACK7_visible = False
ATTACK8_visible = False
ATTACK9_visible = False
ATTACK10_visible = False
ATTACK11_visible = False
ATTACK12_visible = False
ATTACK13_visible = False
ATTACK14_visible = False
ATTACK15_visible = False
ATTACK16_visible = False
opponent_visible = True
ATTACK_visibles = [ATTACK_visible, ATTACK2_visible, ATTACK3_visible, ATTACK4_visible, ATTACK5_visible]       
BLUEATTACK_visibles = [ATTACK6_visible, ATTACK7_visible, ATTACK8_visible, ATTACK9_visible, ATTACK10_visible, ATTACK11_visible]   
ORANGEATTACK_visibles = [ATTACK11_visible, ATTACK12_visible, ATTACK13_visible, ATTACK14_visible, ATTACK15_visible, ATTACK16_visible]

# timers (seconds) to avoid blocking waits
menu_debounce_timer = 0.0
sparefail_timer = 0.0
missed_timer = 0.0
bar_keep_timer = 0.0  # keep bar visible after stop
check_timer = 0.0     # NEW: timer for Check act display
iframes = 0
# --- configurable durations (seconds) ---
MISS_DISPLAY_TIME = 2.0        # how long MISSED / MISSED? stays
SPAREFAIL_DISPLAY_TIME = 2.0   # how long spare-fail text stays
BAR_KEEP_TIME = 1.5            # how long the bar remains visible after stop
CHECK_DISPLAY_TIME = 2.0       # how long the Check result stays
# --------------------------------------

bar_speed = 400.0                     # pixels per second
bar_x = float(BATTLEBAR_BAR_RECT.x)   # float for smooth movement
# a hit zone centered inside the battle-bar area (tweak width to taste)
hit_zone = pygame.Rect(
    BATTLEBAR_RECT.centerx - 40,
    BATTLEBAR_RECT.y + 5,
    80,
    BATTLEBAR_RECT.height - 10
)
bar_can_be_stopped = False  # prevents same-keypress from instantly stopping after start
# ------------------------------------------------------------

hp = 99

font = pygame.font.Font(r"DeterminationSansWebRegular.ttf", 28) 
MISSEDfont = pygame.font.Font(r"hachicro.TTF", 32)
MISSED_surface = MISSEDfont.render("MISSED", True, (255, 255, 255))
MISSEDquestionmark_surface = MISSEDfont.render("MISSED?", True, (255, 255, 255))
MISSED_RECT = MISSED_surface.get_rect(center=(BATTLEBOX_RECT.left +185, BATTLEBOX_RECT.top - 140))  
MISSEDquestionmark_RECT = MISSEDquestionmark_surface.get_rect(center=(BATTLEBOX_RECT.left+185, BATTLEBOX_RECT.top - 140))  
Opponent_surface = font.render("* Opponent", True, (255, 255, 255))
Opponent_text_RECT = Opponent_surface.get_rect(topleft=(DIALOGUEBOX_RECT.left + 35, DIALOGUEBOX_RECT.top + 13))  
CHECK_surface = font.render("* Check", True, (255, 255, 255))
CHECK_RECT = CHECK_surface.get_rect(topleft=(DIALOGUEBOX_RECT.left + 35, DIALOGUEBOX_RECT.top + 13))  
Spare_surface = font.render("* Spare", True, (255, 255, 255))
Spare_RECT = Spare_surface.get_rect(topleft=(DIALOGUEBOX_RECT.left + 35, DIALOGUEBOX_RECT.top + 13)) 
Sparefail_surface = font.render("A little late for that now ain't it.", True, (255, 255, 255)) 
Sparefail_RECT = Sparefail_surface.get_rect(topleft=(DIALOGUEBOX_RECT.left + 35, DIALOGUEBOX_RECT.top + 13)) 
ITEMfail_surface = font.render("!? Your not holding on to anything", True, (255, 255, 255))
ITEMfail_RECT = ITEMfail_surface.get_rect(topleft=(DIALOGUEBOX_RECT.left + 35, DIALOGUEBOX_RECT.top + 13)) 
CHECKtext_surface = font.render("Insert Check Text", True, (255, 255, 255)) 
CHECKtext_RECT = CHECKtext_surface.get_rect(topleft=(DIALOGUEBOX_RECT.left + 35, DIALOGUEBOX_RECT.top + 13)) 
OTHERACTOPTION_surface = font.render("Insert ACT", True, (255, 255, 255)) 
OTHERACTOPTION_RECT = OTHERACTOPTION_surface.get_rect(topleft=(DIALOGUEBOX_RECT.left + 35, DIALOGUEBOX_RECT.top + 13)) 
LOVE_surface = font.render("LV 20", True, (255, 255, 255))
HP_surface = font.render("HP", True, (255, 255, 255))
HEALTHBAR_surface = font.render(str(hp)+" / 99", True, (255, 255, 255))
LOVE_text_RECT = LOVE_surface.get_rect(topleft=(screen_width * 0.38, screen_height * 0.80))
HP_text_RECT = HP_surface.get_rect(topleft=(screen_width * 0.44, screen_height * 0.80))
HEALTHBAR_text_RECT = HEALTHBAR_surface.get_rect(topleft=(screen_width * 0.57, screen_height * 0.80))
NAME_surface = font.render("YOU", True, (255, 0 ,0))
NAME_RECT = NAME_surface.get_rect(topleft=(screen_width * 0.318, screen_height * 0.80))
HP_bar_width = screen_width * 0.1  # full bar width (adjust to match Undertale look)
HP_bar_height = screen_height * 0.025
HP_bar_x = screen_width * 0.463
HP_bar_y = screen_height * 0.81
HP_bar_color = (255, 255, 0)  # yellow
damagedalr = False
rotate = 0

soul_menu_positions = [
    (FIGHT_RECT.x - player_size + 22, FIGHT_RECT.y + (button_height - player_size) // 2),
    (ACT_RECT.x - player_size + 22, ACT_RECT.y + (button_height - player_size) // 2),
    (ITEM_RECT.x - player_size + 22, ITEM_RECT.y + (button_height - player_size) // 2),
    (MERCY_RECT.x - player_size + 22, MERCY_RECT.y + (button_height - player_size) // 2),
]
player_rect.topleft = soul_menu_positions[0]  # This puts it at FIGHT at the start
async def main():
    global ATTACK1_visible, rotate, check_timer, sparefail_timer, missed_timer, bar_keep_timer
    global ACT1_image, ACT1_visible, ACT2_image, ACT2_visible, ACT_RECT, ACT_menu_visible, ACT1_visible, ACT2_visible, ACT_menu_visible
    global ATTACK0_RECT, ATTACK0_image, ATTACK0_visible, ATTACK1_image, ATTACK10_RECT, ATTACK10_visible, ATTACK11_RECT, ATTACK11_visible
    global ATTACK12_RECT, ATTACK12_visible, ATTACK13_RECT, ATTACK13_visible, ATTACK14_RECT, ATTACK14_visible, ATTACK15_RECT, ATTACK15_visible
    global ATTACK16_RECT, ATTACK16_visible, ATTACK2_RECT, ATTACK2_image, ATTACK2_visible, ATTACK3_RECT, ATTACK3_image, ATTACK3_visible
    global ATTACK4_RECT, ATTACK4_image, ATTACK4_visible, ATTACK5_RECT, ATTACK5_image, ATTACK5_visible, ATTACK6_RECT, ATTACK6_visible
    global ATTACK7_RECT, ATTACK7_visible, ATTACK8_RECT, ATTACK8_visible, ATTACK9_RECT, ATTACK9_visible, ATTACK_RECT, ATTACK_RECTS
    global ATTACK_image, ATTACK_visible, ATTACK_visibles, BAR_KEEP_TIME, BATTLEBAR_BAR_RECT, BATTLEBAR_RECT, BATTLEBAR_image, BATTLEBOX_RECT
    global BATTLEBOX_image, BATTLE_BOX_visible, BATTLEBAR_BAR_visible, BATTLEBAR_visible, BLUEATTACK10_image, BLUEATTACK6_image, BLUEATTACK7_image
    global BLUEATTACK8_image, BLUEATTACK9_image, BLUEATTACK_image, BLUEATTACK_RECTS, BLUEATTACK_visibles, BLUEATTACK6_image, BLUEATTACK7_image
    global BLUEATTACK8_image, BLUEATTACK9_image, BLUEATTACK10_image, BAR_KEEP_TIME, button_height, button_spacing, button_width, bar_speed
    global bar_x, bar_can_be_stopped, bar_center_x, bar_keep_timer, battlebox_height, battlebox_width, battlebox_x, battlebox_y
    global BATTLEBAR_BAR_RECT, BATTLEBAR_RECT, BATTLEBAR_image, BATTLEBOX_RECT, BATTLEBOX_image, BATTLE_BOX_visible, BATTLEBAR_BAR_visible, BATTLEBAR_visible
    global BLUEATTACK_RECTS, BLUEATTACK_visibles, BLUEATTACK_image, BLUEATTACK6_image, BLUEATTACK7_image, BLUEATTACK8_image, BLUEATTACK9_image, BLUEATTACK10_image
    global CHECK_DISPLAY_TIME, CHECK_RECT, CHECK_surface, CHECKtext_RECT, CHECKtext_surface, CHECK_surface, CHECK_RECT, CHECKtext_surface
    global CHECKtext_RECT, CHECKtext_surface, CHECK_surface, CHECK_RECT, CLOCK, clock, damagedalr, dialoguebox_height, dialoguebox_y, DIALOGUEBOX_image
    global DIALOGUEBOX_rect, DIALOGUEBOX_RECT, DIALOGUE_BOX_visible, DO_attack1, doattack1, doattack1p2, doattack1p2, doattack1
    global doattack1p2, dobunch, dobunch2, doattack1, donothing, dontmove, DOUBLE_VAR_PLACEHOLDER, events, EXTRA_VARS_PLACEHOLDER
    global endcheck, err, extra_rect, extra_visible, EXTRA_STUB, extra_visible, anothernextmove, FIGHT1_image, FIGHT1_visible, FIGHT2_image
    global FIGHT2_visible, FIGHT_RECT, FIGHT_menu_visible, first_menu_movement, firstime, firsttime, first_menu_movement, firstime, firsttime
    global FIGHT1_image, FIGHT2_image, FONT_PLACEHOLDER, font, FIGHT1_visible, FIGHT2_visible, final, fight_flag, float_vars_placeholder
    global goodleftmenupositionx, goodleftmenupositiony, hp, HP_bar_color, HP_bar_height, HP_bar_width, HP_bar_x, HP_bar_y
    global HP_surface, HEALTHBAR_surface, HEALTHBAR_text_RECT, HEALTHBAR_surface, HEALTHBAR_visible, HP_text_RECT, HP_visible, HOLDS
    global holdup, hit_zone, illdothislater, in_menu, ITEM1_image, ITEM1_visible, ITEM2_image, ITEM2_visible
    global ITEM_RECT, ITEM_menu_visible, ITEMfail_RECT, ITEMfail_surface, ITEMfail_surface, ITEMfail_RECT, ITEMfail_surface
    global ITEMfail_RECT, ITEMfail_surface, ITEMfail_RECT, love_vars_placeholder, LOVE_surface, LOVE_text_RECT, LOVE_visible, MISC_VARS
    global make_image, make_extra_rect, menu_debounce_timer, menu1_move, menu2_move, menurestart, missed_timer, MISSED_surface
    global MISSEDquestionmark_surface, MISSED_RECT, MISSEDquestionmark_RECT, MISSEDfont, MISSED_visible, MISSEDquestionmark_visible, morevariables
    global name_placeholder, NAME_surface, NAME_RECT, nextmove, notjumpedyet, opponent_IMAGE_PLACEHOLDER, opponent_image, opponent_RECT, opponent_text_RECT
    global opponent_visible, Opponent_surface, Opponent_text_RECT, onspare, oncheck, onetime, orangeattack_images_placeholder, ORANGEATTACK_image
    global ORANGEATTACK11_image, ORANGEATTACK12_image, ORANGEATTACK13_image, ORANGEATTACK14_image, ORANGEATTACK15_image, ORANGEATTACK16_image, ORANGEATTACK_RECTS
    global ORANGEATTACK_visibles, ORANGEATTACK11_image, ORANGEATTACK12_image, ORANGEATTACK13_image, ORANGEATTACK14_image, ORANGEATTACK15_image, ORANGEATTACK16_image
    global onetime, onspare, opponent_image, opponent_RECT, opponent_visible, otheractoption_surface, OTHERACTOPTION_surface, OTHERACTOPTION_RECT
    global ORANGEATTACK_RECTS, ORANGEATTACK_visibles, ORANGEATTACK_image, ORANGEATTACK11_image, ORANGEATTACK12_image, ORANGEATTACK13_image, ORANGEATTACK14_image
    global ORANGEATTACK15_image, ORANGEATTACK16_image, positioninact_menu, positioninfirst_menu, positioninitem_menu, positioninspare_menu, placement_vars_placeholder
    global pipe1, pipe1_visible, pipe2, plat_vars_placeholder, player_image, player_mask, player_rect, player_size, player_speed, player_visible
    global placement_vars_placeholder2, placemercyfailontop, placemercyfailontop2, previoushp, print, proj_vars_placeholder, pys_var_placeholder
    global pulldown_placeholder, random, result, risky_placeholder, screen, screen_height, screen_width, showtheactualcheckwords, showthewordscheck, sidestuff
    global soul_free_move, soul_menu_positions, soul_menu_positions, soul_vars_placeholder, soul_menu_positions, sparefail_timer, Sparefail_RECT, Sparefail_surface
    global Spare_RECT, Spare_surface, SPARE1_image, SPARE1_visible, SPARE2_image, SPARE2_visible, SPARE1_visible, SPARE2_visible, startactualattacks
    global startfight, stoppablebar, str_vars_placeholder, start_x, sys, TAKETWO2_PLACEHOLDER, taketwo2, TAKE_TWO, take_vars_placeholder
    global taketwo2, total_width, turnoff, tut_vars_placeholder, vertical_offset, workpls, window_vars_placeholder, y_pos, year_placeholder, your_placeholder
    global ACT1_image, ACT1_visible, ACT2_image, ACT2_visible, ACT_RECT, ACT_menu_visible, ATTACK0_RECT, ATTACK0_image, ATTACK0_visible, ATTACK10_RECT, ATTACK10_visible, ATTACK11_RECT
    global ATTACK11_visible, ATTACK12_RECT, ATTACK12_visible, ATTACK13_RECT, ATTACK13_visible, ATTACK14_RECT, ATTACK14_visible, ATTACK15_RECT, ATTACK15_visible, ATTACK16_RECT, ATTACK16_visible, ATTACK1_image
    global ATTACK2_RECT, ATTACK2_image, ATTACK2_visible, ATTACK3_RECT, ATTACK3_image, ATTACK3_visible, ATTACK4_RECT, ATTACK4_image, ATTACK4_visible, ATTACK5_RECT, ATTACK5_image, ATTACK5_visible
    global ATTACK6_RECT, ATTACK6_visible, ATTACK7_RECT, ATTACK7_visible, ATTACK8_RECT, ATTACK8_visible, ATTACK9_RECT, ATTACK9_visible, ATTACK_RECT, ATTACK_RECTS, ATTACK_image, ATTACK_visible
    global ATTACK_visibles, BAR_KEEP_TIME, BATTLEBAR_BAR_RECT, BATTLEBAR_RECT, BATTLEBAR_image, BATTLEBOX_RECT, BATTLEBOX_image, BATTLE_BOX_visible, BATTLEBAR_BAR_visible, BATTLEBAR_visible, BLUEATTACK10_image, BLUEATTACK6_image
    global BLUEATTACK7_image, BLUEATTACK8_image, BLUEATTACK9_image, BLUEATTACK_image, BLUEATTACK_RECTS, BLUEATTACK_visibles, BLUEATTACK7_image, BLUEATTACK8_image, BLUEATTACK9_image, BLUEATTACK10_image, BLUEATTACK6_image, BLUEATTACK7_image
    global BLUEATTACK8_image, BLUEATTACK9_image, BLUEATTACK10_image, BLUEATTACK6_image, BLUEATTACK7_image, BLUEATTACK8_image, BLUEATTACK9_image, BLUEATTACK10_image, BLUEATTACK_image, BATTLEBOX_RECT, BATTLEBOX_image, BAR_KEEP_TIME
    global BUTTON_HEIGHT, BATTLEBAR_BAR_RECT, BATTLEBAR_RECT, BATTLEBAR_image, BATTLEBOX_RECT, BATTLEBOX_image, BATTLE_BOX_visible, BAR_KEEP_TIME, BAR_KEEP_TIME, BATTLEBAR_BAR_visible, BAR_KEEP_TIME, BATTLEBAR_visible

    global morevariables, anothervariable, taketwo2, previoushp, firstime, firsttime
    global doattack1p2, holdup, doattack1, first_menu_movement
    global second_menu_movement, positioninfirst_menu, positioninact_menu
    global positioninitem_menu, positioninspare_menu, goodleftmenupositiony
    global goodleftmenupositionx, battleattacks, duringbattle
    global illdothislater, onetime, showthewordscheck, in_menu
    global soul_free_move, menu1_move, menu2_move, onspare
    global placemercyfailontop, placemercyfailontop2, oncheck
    global showtheactualcheckwords, endcheck, anothercheckflag
    global startfight, continuefight, checkx, turnoff, menurestart
    global attacknumber, player_size, player_speed, button_width, button_height
    global player_rect, player_image, player_visible, vertical_offset, button_spacing
    global total_width, start_x, y_pos, battlebox_width, battlebox_height
    global battlebox_x, battlebox_y, dialoguebox_height, dialoguebox_y
    global ACT1_image, ACT2_image, FIGHT1_image, FIGHT2_image
    global SPARE1_image, SPARE2_image, ITEM1_image, ITEM2_image
    global DIALOGUEBOX_image, BATTLEBOX_image, BATTLEBAR_image
    global ATTACK_image, BLUEATTACK_image, ORANGEATTACK_image, opponent_image
    global player_mask, extra_rect, FIGHT_RECT, ACT_RECT, ITEM_RECT, MERCY_RECT
    global BATTLEBOX_RECT, DIALOGUEBOX_RECT, BATTLEBAR_RECT, BATTLEBAR_BAR_RECT
    global opponent_RECT, ATTACK0_RECT, ATTACK_RECT, ATTACK2_RECT, ATTACK3_RECT
    global ATTACK4_RECT, ATTACK5_RECT, ATTACK6_RECT, ATTACK7_RECT, ATTACK8_RECT
    global ATTACK9_RECT, ATTACK10_RECT, ATTACK11_RECT, ATTACK12_RECT, ATTACK13_RECT
    global ATTACK14_RECT, ATTACK15_RECT, ATTACK16_RECT, ATTACK_RECTS
    global BLUEATTACK_RECTS, ORANGEATTACK_RECTS, ATTACK0_image, ATTACK1_image
    global ATTACK2_image, ATTACK3_image, ATTACK4_image, ATTACK5_image
    global BLUEATTACK6_image, BLUEATTACK7_image, BLUEATTACK8_image, BLUEATTACK9_image
    global BLUEATTACK10_image, ORANGEATTACK11_image, ORANGEATTACK12_image
    global ORANGEATTACK13_image, ORANGEATTACK14_image, ORANGEATTACK15_image
    global ORANGEATTACK16_image, extra_visible, anothernextmove, ACT1_visible
    global ACT2_visible, FIGHT1_visible, FIGHT2_visible, SPARE1_visible
    global SPARE2_visible, ITEM1_visible, ITEM2_visible, ITEM_menu_visible
    global FIGHT_menu_visible, MERCY_menu_visible, ACT_menu_visible
    global DIALOGUE_BOX_visible, BATTLE_BOX_visible, BATTLEBAR_visible
    global workpls, placeopponent, startactualattacks, LOVE_visible
    global HP_visible, HEALTHBAR_visible, NAME_visible, HP_bar_visible
    global BATTLEBAR_BAR_visible, stoppablebar, MISSED_visible
    global MISSEDquestionmark_visible, battlestart, nextmove
    global ATTACK0_visible, ATTACK_visible, ATTACK2_visible, ATTACK3_visible
    global ATTACK4_visible, ATTACK5_visible, ATTACK6_visible, ATTACK7_visible
    global ATTACK8_visible, ATTACK9_visible, ATTACK10_visible, ATTACK11_visible
    global ATTACK12_visible, ATTACK13_visible, ATTACK14_visible, ATTACK15_visible
    global ATTACK16_visible, opponent_visible, ATTACK_visibles
    global BLUEATTACK_visibles, ORANGEATTACK_visibles
    global menu_debounce_timer, sparefail_timer, missed_timer, bar_keep_timer
    global check_timer, iframes, MISS_DISPLAY_TIME, SPAREFAIL_DISPLAY_TIME
    global BAR_KEEP_TIME, CHECK_DISPLAY_TIME, bar_speed, bar_x, hit_zone
    global bar_can_be_stopped, hp, font, MISSEDfont, MISSED_surface
    global MISSEDquestionmark_surface, MISSED_RECT, MISSEDquestionmark_RECT
    global Opponent_surface, Opponent_text_RECT, CHECK_surface, CHECK_RECT
    global Spare_surface, Spare_RECT, Sparefail_surface, Sparefail_RECT
    global ITEMfail_surface, ITEMfail_RECT, CHECKtext_surface, CHECKtext_RECT
    global OTHERACTOPTION_surface, OTHERACTOPTION_RECT, LOVE_surface, HP_surface
    global HEALTHBAR_surface, LOVE_text_RECT, HP_text_RECT, HEALTHBAR_text_RECT
    global NAME_surface, NAME_RECT, HP_bar_width, HP_bar_height, HP_bar_x
    global result, events, bar_center_x, HP_bar_y, HP_bar_color, damagedalr
    global soul_menu_positions, ATTACK_mask, ORANGEATTACK_mask, BLUEATTACK_mask
    global morevariables, anothervariable, taketwo2, previoushp, firstime, firsttime
    global doattack1p2, holdup, doattack1, first_menu_movement
    global second_menu_movement, positioninfirst_menu, positioninact_menu
    global positioninitem_menu, positioninspare_menu, goodleftmenupositiony
    global goodleftmenupositionx, battleattacks, duringbattle
    global illdothislater, onetime, showthewordscheck, in_menu
    global soul_free_move, menu1_move, menu2_move, onspare
    global placemercyfailontop, placemercyfailontop2, oncheck
    global showtheactualcheckwords, endcheck, anothercheckflag
    global startfight, continuefight, checkx, turnoff, menurestart
    global attacknumber, player_size, player_speed, button_width, button_height
    global player_rect, player_image, player_visible, vertical_offset, button_spacing
    global total_width, start_x, y_pos, battlebox_width, battlebox_height
    global battlebox_x, battlebox_y, dialoguebox_height, dialoguebox_y
    global ACT1_image, ACT2_image, FIGHT1_image, FIGHT2_image
    global SPARE1_image, SPARE2_image, ITEM1_image, ITEM2_image
    global DIALOGUEBOX_image, BATTLEBOX_image, BATTLEBAR_image
    global ATTACK_image, BLUEATTACK_image, ORANGEATTACK_image, opponent_image
    global player_mask, extra_rect, FIGHT_RECT, ACT_RECT, ITEM_RECT, MERCY_RECT
    global BATTLEBOX_RECT, DIALOGUEBOX_RECT, BATTLEBAR_RECT, BATTLEBAR_BAR_RECT
    global opponent_RECT, ATTACK0_RECT, ATTACK_RECT, ATTACK2_RECT, ATTACK3_RECT
    global ATTACK4_RECT, ATTACK5_RECT, ATTACK6_RECT, ATTACK7_RECT, ATTACK8_RECT
    global ATTACK9_RECT, ATTACK10_RECT, ATTACK11_RECT, ATTACK12_RECT, ATTACK13_RECT
    global ATTACK14_RECT, ATTACK15_RECT, ATTACK16_RECT, ATTACK_RECTS
    global BLUEATTACK_RECTS, ORANGEATTACK_RECTS, ATTACK0_image, ATTACK1_image
    global ATTACK2_image, ATTACK3_image, ATTACK4_image, ATTACK5_image
    global BLUEATTACK6_image, BLUEATTACK7_image, BLUEATTACK8_image, BLUEATTACK9_image
    global BLUEATTACK10_image, ORANGEATTACK11_image, ORANGEATTACK12_image
    global ORANGEATTACK13_image, ORANGEATTACK14_image, ORANGEATTACK15_image
    global ORANGEATTACK16_image, extra_visible, anothernextmove, ACT1_visible
    global ACT2_visible, FIGHT1_visible, FIGHT2_visible, SPARE1_visible
    global SPARE2_visible, ITEM1_visible, ITEM2_visible, ITEM_menu_visible
    global FIGHT_menu_visible, MERCY_menu_visible, ACT_menu_visible
    global DIALOGUE_BOX_visible, BATTLE_BOX_visible, BATTLEBAR_visible
    global workpls, placeopponent, startactualattacks, LOVE_visible
    global HP_visible, HEALTHBAR_visible, NAME_visible, HP_bar_visible
    global BATTLEBAR_BAR_visible, stoppablebar, MISSED_visible
    global MISSEDquestionmark_visible, battlestart, nextmove
    global ATTACK0_visible, ATTACK_visible, ATTACK2_visible, ATTACK3_visible
    global ATTACK4_visible, ATTACK5_visible, ATTACK6_visible, ATTACK7_visible
    global ATTACK8_visible, ATTACK9_visible, ATTACK10_visible, ATTACK11_visible
    global ATTACK12_visible, ATTACK13_visible, ATTACK14_visible, ATTACK15_visible
    global ATTACK16_visible, opponent_visible, ATTACK_visibles
    global BLUEATTACK_visibles, ORANGEATTACK_visibles
    global menu_debounce_timer, sparefail_timer, missed_timer, bar_keep_timer
    global check_timer, iframes, MISS_DISPLAY_TIME, SPAREFAIL_DISPLAY_TIME
    global BAR_KEEP_TIME, CHECK_DISPLAY_TIME, bar_speed, bar_x, hit_zone
    global bar_can_be_stopped, hp, font, MISSEDfont, MISSED_surface
    global MISSEDquestionmark_surface, MISSED_RECT, MISSEDquestionmark_RECT
    global Opponent_surface, Opponent_text_RECT, CHECK_surface, CHECK_RECT
    global Spare_surface, Spare_RECT, Sparefail_surface, Sparefail_RECT
    global ITEMfail_surface, ITEMfail_RECT, CHECKtext_surface, CHECKtext_RECT
    global OTHERACTOPTION_surface, OTHERACTOPTION_RECT, LOVE_surface, HP_surface
    global HEALTHBAR_surface, LOVE_text_RECT, HP_text_RECT, HEALTHBAR_text_RECT
    global NAME_surface, NAME_RECT, HP_bar_width, HP_bar_height, HP_bar_x
    global result, events, bar_center_x, HP_bar_y, HP_bar_color, damagedalr, soul_menu_positions, ATTACK_mask, ORANGEATTACK_mask, BLUEATTACK_mask
    global anothervariable, anothernextmove, anothercheckflag, attack_delay, attack_start_time, attacknumber, ATTACK_masks
    global ATTACK_RECTS, ATTACK_RECT, ATTACK0_RECT, ATTACK2_RECT, ATTACK3_RECT, ATTACK4_RECT, ATTACK5_RECT, ATTACK6_RECT, ATTACK7_RECT
    global ATTACK8_RECT, ATTACK9_RECT, ATTACK10_RECT, ATTACK11_RECT, ATTACK12_RECT, ATTACK13_RECT, ATTACK14_RECT, ATTACK15_RECT, ATTACK16_RECT
    global ATTACK_image, ATTACK0_image, ATTACK1_image, ATTACK2_image, ATTACK3_image, ATTACK4_image, ATTACK5_image
    global ATTACK_visible, ATTACK0_visible, ATTACK2_visible, ATTACK3_visible, ATTACK4_visible, ATTACK5_visible, ATTACK6_visible, ATTACK7_visible
    global ATTACK8_visible, ATTACK9_visible, ATTACK10_visible, ATTACK11_visible, ATTACK12_visible, ATTACK13_visible, ATTACK14_visible, ATTACK15_visible, ATTACK16_visible
    global ATTACK_visibles, ATTACK_RECTS, ATTACK_images
    global BAR_KEEP_TIME, bar_keep_timer, bar_speed, bar_x, bar_center_x, bar_can_be_stopped, bar_speed
    global BATTLEBAR_BAR_RECT, BATTLEBAR_BAR_visible, BATTLEBAR_RECT, BATTLEBAR_image, BATTLEBAR_visible
    global BATTLEBOX_RECT, BATTLEBOX_image, BATTLE_BOX_visible, battlebox_height, battlebox_width, battlebox_x, battlebox_y
    global BLUEATTACK_image, BLUEATTACK6_image, BLUEATTACK7_image, BLUEATTACK8_image, BLUEATTACK9_image, BLUEATTACK10_image
    global BLUEATTACK_RECTS, BLUEATTACK_visibles, BLUEATTACK_masks, BLUEATTACK_images
    global CHECK_DISPLAY_TIME, CHECK_RECT, CHECK_surface, CHECKtext_RECT, CHECKtext_surface, check_timer
    global CLOCK, clock, damagedalr, DIALOGUEBOX_image, DIALOGUEBOX_RECT, DIALOGUE_BOX_visible, dialoguebox_height, dialoguebox_y
    global doattack1, doattack1p2, dobunch, dontmove, doattack1p2
    global doattack1, doattack1p2, dobunch2, doattack1p2  # (duplicates harmless)
    global doattack1, doattack1p2
    global endcheck, events, extra_rect, extra_visible, EXTRA_STUB  # EXTRA_STUB placeholder harmless
    global FIGHT1_image, FIGHT1_visible, FIGHT2_image, FIGHT2_visible, FIGHT_RECT, FIGHT_menu_visible, first_menu_movement
    global firstime, firsttime, first_menu_movement, font, FIGHT1_image, FIGHT2_image
    global goodleftmenupositionx, goodleftmenupositiony, hp, HP_bar_color, HP_bar_height, HP_bar_width, HP_bar_x, HP_bar_y
    global HP_surface, HEALTHBAR_surface, HEALTHBAR_text_RECT, HEALTHBAR_visible, HP_text_RECT, HP_visible
    global holdup, holding_dir, hit_zone, illdothislater, in_menu, ITEM1_image, ITEM1_visible, ITEM2_image, ITEM2_visible
    global ITEM_RECT, ITEM_menu_visible, ITEMfail_RECT, ITEMfail_surface
    global menu_debounce_timer, menu1_move, menu2_move, menurestart, missed_timer, MISSED_surface, MISSEDquestionmark_surface
    global MISSED_RECT, MISSEDquestionmark_RECT, MISSEDfont, MISSED_visible, MISSEDquestionmark_visible
    global morevariables, mkdir_stub  # mkdir_stub harmless placeholder
    global MOVE_VARS_PLACEHOLDER  # harmless placeholder
    global name_placeholder, NAME_surface, NAME_RECT, nextmove, notjumpedyet, now, ORANGEATTACK_image
    global ORANGEATTACK11_image, ORANGEATTACK12_image, ORANGEATTACK13_image, ORANGEATTACK14_image, ORANGEATTACK15_image, ORANGEATTACK16_image
    global ORANGEATTACK_RECTS, ORANGEATTACK_visibles, ORANGEATTACK_masks, ORANGEATTACK_images
    global onetime, onspare, oncheck, opponent_image, opponent_RECT, opponent_visible, Opponent_surface, Opponent_text_RECT
    global otheractoption_surface, OTHERACTOPTION_surface, OTHERACTOPTION_RECT, option_placeholders
    global pack_vars_placeholder  # harmless placeholder
    global player_image, player_mask, player_rect, player_size, player_speed, player_visible, placemercyfailontop, placemercyfailontop2
    global placeopponent, positioninact_menu, positioninfirst_menu, positioninitem_menu, positioninspare_menu, positioninfirst_menu
    global print_stub, PROJ_PLACEHOLDER  # harmless placeholders
    global previoushp, pulldown_placeholder, random, result, risky_placeholder, run_stub
    global screen, screen_height, screen_width, showtheactualcheckwords, showthewordscheck, sidestuff
    global soul_free_move, soul_menu_positions, start_x, startfight, startactualattacks, start_x
    global SPARE1_image, SPARE1_visible, SPARE2_image, SPARE2_visible, Spare_surface, Spare_RECT, Sparefail_surface, Sparefail_RECT, SPAREFAIL_DISPLAY_TIME, sparefail_timer
    global SPARE_FAIL_VARS_PLACEHOLDER  # harmless placeholder
    global soul_menu_positions, soul_vars_placeholder
    global soul_free_move, soul_menu_positions
    global stoppablebar, start_x, TAKETWO2_PLACEHOLDER, taketwo, taketwo2, TAKETWO_PLACEHOLDER
    global TAKETWO_PLACEHOLDER2  # harmless placeholder
    global TAKETWO2_PLACEHOLDER  # harmless placeholder
    global TAKETWO_PLACEHOLDER3  # harmless placeholder
    global taketwo2, taketwo
    global take_vars_placeholder  # harmless placeholder
    global taketwo, taketwo2
    global TAKE_TWO  # harmless placeholder
    global TAKETWO  # harmless placeholder
    global TAKETWO2  # harmless placeholder
    global TAP_VARS_PLACEHOLDER  # harmless placeholder
    global TAP_VAR2  # harmless placeholder
    global TAP_VAR3  # harmless placeholder
    global TAKETWO_PLACEHOLDER4  # harmless placeholder
    global TAKETWO_PLACEHOLDER5  # harmless placeholder
    global TAKETWO_PLACEHOLDER6  # harmless placeholder
    global TAKETWO_PLACEHOLDER7  # harmless placeholder
    global TAKETWO_PLACEHOLDER8  # harmless placeholder
    global TAKE_TWO_PLACEHOLDER9  # harmless placeholder
    global TAKETWO_PLACEHOLDER10  # harmless placeholder
    global turnoff, total_width, tut_vars_placeholder, vertical_offset, workpls, window_vars_placeholder, y_pos
    global weapon_placeholders  # harmless placeholder
    global YEAR_PLACEHOLDER  # harmless placeholder
    global result, events, bar_center_x, HP_bar_y, HP_bar_color, damagedalr, soul_menu_positions
    global ATTACK_mask, ORANGEATTACK_mask, BLUEATTACK_mask, iframes, running, delta_time, keys
    # end globals
    running = True
    while running:
        await asyncio.sleep(0)
        ATTACK_visibles = [ATTACK0_visible, ATTACK_visible, ATTACK2_visible, ATTACK3_visible, ATTACK4_visible, ATTACK5_visible]
        BLUEATTACK_visibles = [ATTACK6_visible, ATTACK7_visible, ATTACK8_visible, ATTACK9_visible, ATTACK10_visible]
        ORANGEATTACK_visibles = [ATTACK11_visible, ATTACK12_visible, ATTACK13_visible, ATTACK14_visible, ATTACK15_visible, ATTACK16_visible]

        ATTACK_images = [ATTACK0_image, ATTACK1_image, ATTACK2_image, ATTACK3_image, ATTACK4_image, ATTACK5_image]
        BLUEATTACK_images = [BLUEATTACK6_image, BLUEATTACK7_image, BLUEATTACK8_image, BLUEATTACK9_image, BLUEATTACK10_image]
        ORANGEATTACK_images = [ORANGEATTACK11_image, ORANGEATTACK12_image, ORANGEATTACK13_image, ORANGEATTACK14_image, ORANGEATTACK15_image, ORANGEATTACK16_image]

        ATTACK_RECTS = [ATTACK0_RECT, ATTACK_RECT, ATTACK2_RECT, ATTACK3_RECT, ATTACK4_RECT, ATTACK5_RECT]
        BLUEATTACK_RECTS = [ATTACK6_RECT, ATTACK7_RECT, ATTACK8_RECT, ATTACK9_RECT, ATTACK10_RECT]
        ORANGEATTACK_RECTS = [ATTACK11_RECT, ATTACK12_RECT, ATTACK13_RECT, ATTACK14_RECT, ATTACK15_RECT, ATTACK16_RECT]

        # Build masks in sync
        ATTACK_masks = [pygame.mask.from_surface(img) for img in ATTACK_images]
        BLUEATTACK_masks = [pygame.mask.from_surface(img) for img in BLUEATTACK_images]
        ORANGEATTACK_masks = [pygame.mask.from_surface(img) for img in ORANGEATTACK_images]


        ATTACK_mask = pygame.mask.from_surface(ATTACK_image)
        BLUEATTACK_mask = pygame.mask.from_surface(BLUEATTACK_image)
        ORANGEATTACK_mask = pygame.mask.from_surface(ORANGEATTACK_image)
        # Clear screen once per frame
        screen.fill((0, 0, 0))
        HEALTHBAR_surface = font.render(f"{hp} / 99", True, (255, 255, 255))
        delta_time = clock.tick(60) / 1000
        for event in pygame.event.get():
            events = event
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if ACT1_visible and FIGHT1_visible and ITEM1_visible and SPARE1_visible and menu1_move and in_menu == True:
                first_menu_movement = True
                positioninfirst_menu = 1
            if first_menu_movement:
                player_visible = True
                if event.type == pygame.KEYDOWN:
                    # debounce arrow input using menu_debounce_timer
                    if event.key == pygame.K_RIGHT and positioninfirst_menu < 4 and menu_debounce_timer <= 0.0:
                        positioninfirst_menu += 1
                        menu_debounce_timer = 0.3  # non-blocking debounce
                    elif event.key == pygame.K_LEFT and positioninfirst_menu > 1 and menu_debounce_timer <= 0.0:
                        positioninfirst_menu -= 1
                        menu_debounce_timer = 0.3
                    if event.key == pygame.K_z:
                        if positioninfirst_menu == 1:
                            FIGHT_menu_visible = True
                            menu1_move = False
                            first_menu_movement = False
                            menu2_move = True
                            second_menu_movement = True
                        elif positioninfirst_menu == 2:
                            ACT_menu_visible = True
                            menu1_move = False
                            first_menu_movement = False
                            menu2_move = True
                            second_menu_movement = True
                        elif positioninfirst_menu == 3:
                            ITEM_menu_visible = True
                            menu1_move = False
                            first_menu_movement = False
                            menu2_move = True
                            second_menu_movement = True
                        elif positioninfirst_menu == 4:
                            MERCY_menu_visible = True
                            menu1_move = False
                            first_menu_movement = False
                            menu2_move = True
                            second_menu_movement = True
                    # Update player (soul) position based on selection
                    player_rect.topleft = soul_menu_positions[positioninfirst_menu - 1]
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    if not startactualattacks:
                    # Cancel any sub-menu and reset related flags
                        if ACT_menu_visible or ITEM_menu_visible or FIGHT_menu_visible or MERCY_menu_visible or turnoff: #make sure to add one to fix pressing x while on the words "Check"
                            # Close menus
                            ACT_menu_visible = ITEM_menu_visible = FIGHT_menu_visible = MERCY_menu_visible = False
                            
                            # Reset ACT-related flags
                            showthewordscheck = False
                            showtheactualcheckwords = False
                            anothercheckflag = False
                            endcheck = False
                            oncheck = False
                            placeopponent = False

                            # Reset MERCY-related flags
                            placemercyfailontop = False
                            placemercyfailontop2 = False
                            onspare = False

                            # Reset FIGHT-related flags
                            startfight = False
                            continuefight = False
                            BATTLEBAR_visible = False
                            player_visible = True  # Soul becomes visible again

                            # Return to main menu movement
                            menu1_move = True
                            first_menu_movement = True
                            menu2_move = False
                            second_menu_movement = False

                            # Keep the same position in main menu
                            player_rect.topleft = soul_menu_positions[positioninfirst_menu - 1]


            if event.type == pygame.KEYDOWN:
                if MERCY_menu_visible and onspare and event.key == pygame.K_z:
                    onspare = False
                    MERCY_menu_visible = False
                    placemercyfailontop = True
                    sparefail_timer = SPAREFAIL_DISPLAY_TIME  # start non-blocking display timer (seconds)
            if event.type == pygame.KEYDOWN:
                if FIGHT_menu_visible and startfight and event.key == pygame.K_z:
                    player_visible = False
                    BATTLEBAR_visible = True
                    continuefight = True
                    FIGHT_menu_visible = False
                    if event.key == pygame.K_x:
                        startfight = False
                        player_visible = True
                        BATTLEBAR_visible = False
                        FIGHT_menu_visible = True
                        continuefight = False
                        menu1_move = True
                if startfight and continuefight:
                    startfight = False
                    BATTLEBAR_BAR_visible = True
                    stoppablebar = True
                    BATTLEBAR_BAR_RECT.x = start_x * 0.98 + 2
                    # ----- ADDED: reset float position and ensure same-Z doesn't stop immediately -----
                    bar_x = float(BATTLEBAR_BAR_RECT.x)
                    bar_can_be_stopped = False
                    # -------------------------------------------------------------------------------

                # (other code below in this KEYDOWN branch remains unchanged)

            # NEW: stop the moving bar if player presses Z while the bar is actively moving
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z and stoppablebar and bar_can_be_stopped:
                    # stop the bar
                    stoppablebar = False

                    # evaluate hit using the bar center (we're not using hit_zone now for MISS/MISSED?)
                    bar_center_x = BATTLEBAR_BAR_RECT.centerx
                    # keep the bar visible for BAR_KEEP_TIME
                    bar_keep_timer = BAR_KEEP_TIME
                    BATTLEBAR_BAR_visible = True
                    if DIALOGUEBOX_RECT.left < BATTLEBAR_BAR_RECT.left and BATTLEBAR_BAR_RECT.right < DIALOGUEBOX_RECT.right:
                        result = "MISSED?"
                        MISSEDquestionmark_visible = True
                        missed_timer = MISS_DISPLAY_TIME
                        battlestart = True
                        
                    else:
                        result = "MISSED"
                        MISSED_visible = True
                        missed_timer = MISS_DISPLAY_TIME
                        battlestart = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z and oncheck: #maybe add positioninsecondmenu flag if needed
                    workpls = True
                    ACT_menu_visible = False
                    oncheck = False

                if workpls and event.key == pygame.K_z:
                    showthewordscheck = True

                # pressing Z again when "anothercheckflag" True shows the actual check text:
                if anothercheckflag and event.key == pygame.K_z:
                    showthewordscheck = False
                    showtheactualcheckwords = True
                    check_timer = CHECK_DISPLAY_TIME  # start the check display timer
                    if event.key== pygame.K_z:
                        endcheck = False  # allow manual dismissal with Z if player presses it


            if event.type == pygame.KEYDOWN:
                if placemercyfailontop2 and event.key == pygame.K_z:
                    placemercyfailontop = False
                    placemercyfailontop2 = False
                elif endcheck and event.key == pygame.K_z:
                    # manual dismiss of Check text
                    showtheactualcheckwords = False
                    check_timer = 0.0
                    endcheck = False


        # update timers non-blocking
        if menu_debounce_timer > 0.0:
            menu_debounce_timer -= delta_time
            if menu_debounce_timer < 0.0:
                menu_debounce_timer = 0.0

        if sparefail_timer > 0.0:
            sparefail_timer -= delta_time
            if sparefail_timer <= 0.0:
                # when sparefail timer ends, move to the second phase
                sparefail_timer = 0.0
                if placemercyfailontop:
                    placemercyfailontop = False
                    placemercyfailontop2 = True
                    battlestart = True

        if missed_timer > 0.0:
            missed_timer -= delta_time
            if missed_timer <= 0.0:
                missed_timer = 0.0
                MISSED_visible = False
                MISSEDquestionmark_visible = False

        # update bar_keep_timer: keep bar visible  short time after stopping
        if bar_keep_timer > 0.0:
            bar_keep_timer -= delta_time
            if bar_keep_timer <= 0.0:
                bar_keep_timer = 0.0
                BATTLEBAR_BAR_visible = False

        # update check_timer (for Check act display)
        if check_timer > 0.0:
            check_timer -= delta_time
            if check_timer <= 0.0:
                check_timer = 0.0
                showtheactualcheckwords = False
                endcheck = False
                battlestart = True

        keys = pygame.key.get_pressed()
        if soul_free_move == True:
            # removed set_repeat call here (don't set repeat every frame)
            if keys[pygame.K_UP]: player_rect.y -= player_speed
            if keys[pygame.K_DOWN]: player_rect.y += player_speed
            if keys[pygame.K_LEFT]: player_rect.x -= player_speed
            if keys[pygame.K_RIGHT]: player_rect.x += player_speed
        if menu1_move and not first_menu_movement:
            if keys[pygame.K_LEFT]: player_rect.x -= player_speed
            if keys[pygame.K_RIGHT]: player_rect.x += player_speed
        if keys[pygame.K_LSHIFT]:
            player_speed = 2.5
        else:
            player_speed = 5
        if menu2_move:
            if goodleftmenupositiony == 0 or goodleftmenupositionx == 0:
                if player_rect.y > screen_height - (dialoguebox_height * 2) + 22:
                    player_visible = False
                    player_rect.y -= 14
                elif player_rect.x > start_x * 0.98 + 25:
                    player_visible = False
                    player_rect.x -= 14
                else: 
                    player_visible = True
                    menu2_move = False
                    goodleftmenupositiony = player_rect.y
                    goodleftmenupositionx = player_rect.x
            else:
                player_rect.y = goodleftmenupositiony
                player_rect.x = goodleftmenupositionx

        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()


        if ACT1_visible:
            screen.blit(ACT1_image, ACT_RECT.topleft)
        if ACT2_visible:
            screen.blit(ACT2_image, ACT_RECT.topleft)
        if FIGHT1_visible:
            screen.blit(FIGHT1_image, FIGHT_RECT.topleft)
        if FIGHT2_visible:
            screen.blit(FIGHT2_image, FIGHT_RECT.topleft)
        if SPARE1_visible:
            screen.blit(SPARE1_image, MERCY_RECT.topleft)
        if SPARE2_visible:
            screen.blit(SPARE2_image, MERCY_RECT.topleft)
        if ITEM1_visible:
            screen.blit(ITEM1_image, ITEM_RECT.topleft)
        if ITEM2_visible:
            screen.blit(ITEM2_image, ITEM_RECT.topleft)
        if DIALOGUE_BOX_visible:
            screen.blit(DIALOGUEBOX_image, DIALOGUEBOX_RECT.topleft)
        if BATTLE_BOX_visible:
            screen.blit(BATTLEBOX_image, BATTLEBOX_RECT.topleft)
            player_rect.x = max(BATTLEBOX_RECT.left + player_size +5, min(player_rect.x, BATTLEBOX_RECT.right - player_rect.width - player_size - 5))
            player_rect.y = max(BATTLEBOX_RECT.top + player_size - 5, min(player_rect.y, BATTLEBOX_RECT.bottom - player_rect.height - player_size + 5))
        if ACT_menu_visible == True:
            screen.blit(Opponent_surface, Opponent_text_RECT)
            oncheck = True
        if FIGHT_menu_visible:
            screen.blit(Opponent_surface, Opponent_text_RECT)
            startfight = True
        if ITEM_menu_visible == True:
            screen.blit(ITEMfail_surface, ITEMfail_RECT)
        if MERCY_menu_visible:
            screen.blit(Spare_surface, Spare_RECT)
            onspare = True
        if HP_visible:
            screen.blit(HP_surface, HP_text_RECT)
        if LOVE_visible:
            screen.blit(LOVE_surface, LOVE_text_RECT)
        if HEALTHBAR_visible:
            screen.blit(HEALTHBAR_surface, HEALTHBAR_text_RECT)
        if NAME_visible:
            screen.blit(NAME_surface, NAME_RECT)
        if HP_bar_visible:
            # Calculate proportional width based on current HP
            current_bar_width = HP_bar_width * (hp / 99)  

            # Draw background bar (empty part) — dark red/gray
            pygame.draw.rect(screen, (128, 0, 0), (HP_bar_x, HP_bar_y, HP_bar_width, HP_bar_height))

            # Draw filled HP bar (yellow)
            pygame.draw.rect(screen, HP_bar_color, (HP_bar_x, HP_bar_y, current_bar_width, HP_bar_height))



        if ATTACK0_visible:
            screen.blit(ATTACK0_image, ATTACK0_RECT)
        if ATTACK_visible:
            screen.blit(ATTACK1_image, ATTACK_RECT)
        if ATTACK2_visible:
            screen.blit(ATTACK2_image, ATTACK2_RECT)
        if ATTACK3_visible:
            screen.blit(ATTACK3_image, ATTACK3_RECT)
        if ATTACK4_visible:
            screen.blit(ATTACK4_image, ATTACK4_RECT)
        if ATTACK5_visible:
            screen.blit(ATTACK5_image, ATTACK5_RECT)
        if ATTACK6_visible:
            screen.blit(BLUEATTACK6_image, ATTACK6_RECT)
        if ATTACK7_visible:
            screen.blit(BLUEATTACK7_image, ATTACK7_RECT)
        if ATTACK8_visible:
            screen.blit(BLUEATTACK8_image, ATTACK8_RECT)
        if ATTACK9_visible:
            screen.blit(BLUEATTACK9_image, ATTACK9_RECT)
        if ATTACK10_visible:
            screen.blit(BLUEATTACK10_image, ATTACK10_RECT)
        if ATTACK11_visible:
            screen.blit(ORANGEATTACK11_image, ATTACK11_RECT)
        if ATTACK12_visible:
            screen.blit(ORANGEATTACK12_image, ATTACK12_RECT)
        if ATTACK13_visible:
            screen.blit(ORANGEATTACK13_image, ATTACK13_RECT)
        if ATTACK14_visible:
            screen.blit(ORANGEATTACK14_image, ATTACK14_RECT)
        if ATTACK15_visible:
            screen.blit(ORANGEATTACK15_image, ATTACK15_RECT)
        if ATTACK16_visible:
            screen.blit(ORANGEATTACK16_image, ATTACK16_RECT)

        





        if pygame.Rect.colliderect(player_rect, FIGHT_RECT):
            FIGHT1_visible = False
            FIGHT2_visible = True
        elif not pygame.Rect.colliderect(player_rect, FIGHT_RECT) and first_menu_movement == True:
            FIGHT1_visible = True
            FIGHT2_visible = False
        if pygame.Rect.colliderect(player_rect, ACT_RECT):
            ACT1_visible = False
            ACT2_visible = True
        elif not pygame.Rect.colliderect(player_rect, ACT_RECT) and first_menu_movement == True:
            ACT1_visible = True
            ACT2_visible = False
        if pygame.Rect.colliderect(player_rect, MERCY_RECT):
            SPARE1_visible = False
            SPARE2_visible = True
        elif not pygame.Rect.colliderect(player_rect, MERCY_RECT) and first_menu_movement == True:
            SPARE1_visible = True
            SPARE2_visible = False
        if pygame.Rect.colliderect(player_rect, ITEM_RECT):
            ITEM1_visible = False
            ITEM2_visible = True
        elif not pygame.Rect.colliderect(player_rect, ITEM_RECT) and first_menu_movement == True:
            ITEM1_visible = True
            ITEM2_visible = False
        
        if opponent_visible:
            screen.blit(opponent_image, opponent_RECT.topleft)
        


        if player_visible:
            screen.blit(player_image, player_rect.topleft)
            # Update screen
        if placemercyfailontop:
            # now handled non-blocking via sparefail_timer
            if sparefail_timer > 0.0:
                screen.blit(Sparefail_surface, Sparefail_RECT)
        if showthewordscheck:
            screen.blit(CHECK_surface, CHECK_RECT)
            anothercheckflag = True
        # draw Check text only while check_timer is > 0 (this makes the timer the source of truth)
        if showtheactualcheckwords:
            screen.blit(CHECKtext_surface, CHECKtext_RECT)
        if BATTLEBAR_visible:
            screen.blit(BATTLEBAR_image, BATTLEBAR_RECT.topleft)
            player_visible = False
        if placeopponent:
            screen.blit(Opponent_surface, Opponent_text_RECT)
            workpls = True

        if BATTLEBAR_BAR_visible:
            pygame.draw.rect(screen, (255, 255, 255), (BATTLEBAR_BAR_RECT))
        
    
        if BATTLEBAR_BAR_visible and stoppablebar:
            bar_can_be_stopped = True

        if stoppablebar:
            bar_x += bar_speed * delta_time
            BATTLEBAR_BAR_RECT.x = int(bar_x)
            # stop if it reaches the right boundary (auto-miss)
            if BATTLEBAR_BAR_RECT.right >= BATTLEBAR_RECT.right:
                stoppablebar = False
                # keep the bar visible for BAR_KEEP_TIME and show MISSED
                BATTLEBAR_BAR_visible = True
                bar_keep_timer = BAR_KEEP_TIME
                result = "MISSED"
                MISSED_visible = True
                missed_timer = MISS_DISPLAY_TIME
                battlestart = True

        if MISSEDquestionmark_visible:
            # show non-blocking
            if missed_timer > 0.0:
                screen.blit(MISSEDquestionmark_surface, MISSEDquestionmark_RECT)
        if MISSED_visible:
            if missed_timer > 0.0:
                screen.blit(MISSED_surface, MISSED_RECT)        

        if battlestart:
            player_rect.x = BATTLEBOX_RECT.centerx
            player_rect.y = BATTLEBOX_RECT.centery
            soul_free_move = True
            menu1_move = False
            menu2_move = False
            second_menu_movement = False
            first_menu_movement = False
            FIGHT_menu_visible = False
            ACT_menu_visible = False
            BATTLE_BOX_visible = True
            ITEM_menu_visible = False
            MERCY_menu_visible = False
            DIALOGUE_BOX_visible = False
            BATTLEBAR_visible = False
            BATTLEBAR_BAR_visible = False
            ACT_menu_visible = ITEM_menu_visible = FIGHT_menu_visible = MERCY_menu_visible = False             
            # Reset ACT-related flags
            showthewordscheck = False
            showtheactualcheckwords = False
            anothercheckflag = False
            endcheck = False
            oncheck = False
            placeopponent = False

            # Reset MERCY-related flags
            placemercyfailontop = False
            placemercyfailontop2 = False
            onspare = False

            # Reset FIGHT-related flags
            startfight = False
            continuefight = False
            BATTLEBAR_visible = False
            player_visible = True
            battlestart = False
            battleattacks = True


        if battleattacks:
            attacknumber += 1
            doattack1 = False
            battleattacks = False
            duringbattle = True
            morevariables = False
            attack_start_time = pygame.time.get_ticks()

        if duringbattle:
            if attacknumber == 1:
                ATTACK_visible = True 
                ATTACK2_visible = True
                ATTACK3_visible = True
                ATTACK4_visible = True

                if not doattack1:

                    ATTACK1_image = pygame.transform.rotate(ATTACK1_image, -135)
                    ATTACK2_image = pygame.transform.rotate(ATTACK2_image, 135)
                    ATTACK3_image = pygame.transform.rotate(ATTACK3_image, -45)
                    ATTACK4_image = pygame.transform.rotate(ATTACK4_image, 45)

                    ATTACK_RECT = ATTACK1_image.get_rect(center=BATTLEBOX_RECT.topleft)
                    ATTACK2_RECT = ATTACK2_image.get_rect(center=BATTLEBOX_RECT.topright)
                    ATTACK3_RECT = ATTACK3_image.get_rect(center=BATTLEBOX_RECT.bottomleft)
                    ATTACK4_RECT = ATTACK4_image.get_rect(center=BATTLEBOX_RECT.bottomright)
                    # offset so they start outside
                    ATTACK_RECT.move_ip(-50, -50)
                    ATTACK2_RECT.move_ip(50, -50)
                    ATTACK3_RECT.move_ip(-50, 50)
                    ATTACK4_RECT.move_ip(50, 50)

                    doattack1 = True  
                    turnoff = []
                attack_delay = 500  # ms

                # inside game loop
                now = pygame.time.get_ticks()
                if now - attack_start_time > attack_delay:
                    if ATTACK_RECT.left < BATTLEBOX_RECT.right and not firstime:
                        ATTACK_RECT.x += 7
                    else:
                        turnoff.append("wtv")

                    if ATTACK_RECT.top < BATTLEBOX_RECT.bottom and not firstime:
                        ATTACK_RECT.y += 4
                    else:
                        turnoff.append("wtv")


                    # top-right attack -> slides left/down
                    if ATTACK2_RECT.right > BATTLEBOX_RECT.left and not firstime:
                        ATTACK2_RECT.x -= 7
                    else:
                        turnoff.append("wtv")

                    if ATTACK2_RECT.top < BATTLEBOX_RECT.bottom and not firstime:
                        ATTACK2_RECT.y += 4
                    else:
                        turnoff.append("wtv")

                    # bottom-left attack -> slides right/up
                    if ATTACK3_RECT.left < BATTLEBOX_RECT.right and not firstime:
                        ATTACK3_RECT.x += 7
                    else:
                        turnoff.append("wtv")
        
                    if ATTACK3_RECT.bottom > BATTLEBOX_RECT.top and not firstime:
                        ATTACK3_RECT.y -= 4
                    else:
                        turnoff.append("wtv")

                    # bottom-right attack -> slides left/up
                    if ATTACK4_RECT.right > BATTLEBOX_RECT.left and not firstime:
                        ATTACK4_RECT.x -= 7
                    else:
                        turnoff.append("wtv")

                    if ATTACK4_RECT.bottom > BATTLEBOX_RECT.top and not firstime:
                        ATTACK4_RECT.y -= 4
                    else:
                        turnoff.append("wtv")
                    if len(turnoff) >= 8:
                        firstime = True
                if len(turnoff) >= 8:
                    firsttime = True
                    doattack1 = True
                    if not doattack1p2:
                            doattack1p2 = True
                            attack_start_time = pygame.time.get_ticks()
                            ATTACK1_image = pygame.transform.rotate(ATTACK1_image, 135)
                            ATTACK2_image = pygame.transform.rotate(ATTACK2_image, -135)
                            ATTACK3_image = pygame.transform.rotate(ATTACK3_image, 45)
                            ATTACK4_image = pygame.transform.rotate(ATTACK4_image, -45)
                            ATTACK1_image = pygame.transform.rotate(ATTACK1_image, 180)
                            ATTACK2_image = pygame.transform.rotate(ATTACK2_image, 180)
                            ATTACK3_image = pygame.transform.rotate(ATTACK3_image, 180)
                            ATTACK4_image = pygame.transform.rotate(ATTACK4_image, 90)

                            ATTACK_RECT = ATTACK1_image.get_rect(center=BATTLEBOX_RECT.topleft)
                            ATTACK2_RECT = ATTACK2_image.get_rect(center=BATTLEBOX_RECT.topright)
                            ATTACK3_RECT = ATTACK3_image.get_rect(center=BATTLEBOX_RECT.midtop)
                            ATTACK4_RECT = ATTACK4_image.get_rect(center=BATTLEBOX_RECT.midright)
                            ATTACK_RECT.x += 30
                            ATTACK2_RECT.x -= 30
                            ATTACK3_RECT.x += 0
                            ATTACK_visible = ATTACK2_visible = ATTACK3_visible = ATTACK4_visible = True
                    if ATTACK_RECT.top < BATTLEBOX_RECT.bottom and  now - attack_start_time > attack_delay - 200:
                        ATTACK_RECT.y += 10
                        ATTACK2_RECT.y += 10
                        ATTACK3_RECT.y += 10
                        now = pygame.time.get_ticks()
                    if ATTACK4_RECT.x > BATTLEBOX_RECT.x - 150 and  now - attack_start_time > attack_delay - 200:
                        ATTACK4_RECT.x -= 15
                    elif not ATTACK_RECT.top < BATTLEBOX_RECT.bottom and now - attack_start_time > attack_delay + 200:
                        ATTACK_visible = ATTACK2_visible = ATTACK3_visible = False
                        menurestart = True
                        duringbattle = False
            elif attacknumber == 2:
                if not doattack1:
                    ATTACK1_image = ATTACK2_image = ATTACK3_image = ATTACK4_image = ATTACK_image            
                    ATTACK_visible = ATTACK2_visible = ATTACK3_visible = ATTACK4_visible = True
                    ATTACK3_visible = ATTACK4_visible= False
                    ATTACK2_image = pygame.transform.rotate(ATTACK2_image, 90)
                    ATTACK2_RECT = ATTACK2_image.get_rect(center=BATTLEBOX_RECT.midright) 
                    ATTACK2_RECT.x +=50
                    ATTACK2_RECT.y += 50
                    ATTACK3_image = pygame.transform.rotate(ATTACK3_image, -90)
                    ATTACK3_RECT = ATTACK3_image.get_rect(center=BATTLEBOX_RECT.midleft) 
                    ATTACK3_RECT.x -=50
                    ATTACK3_RECT.y +=50
                    ATTACK4_image = pygame.transform.rotate(ATTACK4_image, 90)
                    ATTACK4_RECT = ATTACK4_image.get_rect(center=BATTLEBOX_RECT.midright) 
                    ATTACK4_RECT.x +=50
                    ATTACK4_RECT.y -=50
                    ATTACK1_image = pygame.transform.rotate(ATTACK1_image, -90)
                    ATTACK_RECT = ATTACK1_image.get_rect(center=BATTLEBOX_RECT.midleft) 
                    ATTACK_RECT.x -=50
                    ATTACK_RECT.y -=50
                    doattack1 = True
                    taketwo = False
                now = pygame.time.get_ticks()
                if ATTACK_RECT.y > player_rect.y + 5 and not taketwo:
                    ATTACK_RECT.y -= 5
                elif ATTACK_RECT.y < player_rect.y - 5 and not taketwo:
                    ATTACK_RECT.y += 5
                if ATTACK2_RECT.y > player_rect.y + 5 and not taketwo:
                    ATTACK2_RECT.y -= 5
                elif ATTACK2_RECT.y < player_rect.y - 5 and not taketwo:
                    ATTACK2_RECT.y += 5
                if now - attack_start_time > attack_delay + 1000:
                    taketwo = True
                if taketwo and ATTACK_RECT.x < BATTLEBOX_RECT.right + 50:
                    ATTACK_RECT.x += 10
                    ATTACK2_RECT.x -= 10
                elif ATTACK_RECT.x > BATTLEBOX_RECT.right + 50 and ATTACK_visible:
                    ATTACK_visible = False
                    ATTACK2_visible = False
                    ATTACK3_visible = ATTACK4_visible = True
                    anothervariable = True
                    attack_start_time = pygame.time.get_ticks()
                if ATTACK3_RECT.y > player_rect.y + 5 and  taketwo and anothervariable and not taketwo2:
                    ATTACK3_RECT.y -= 5
                elif ATTACK3_RECT.y < player_rect.y - 5 and  taketwo and anothervariable and not taketwo2:
                    ATTACK3_RECT.y += 5
                if ATTACK4_RECT.y > player_rect.y + 5 and  taketwo and anothervariable and not taketwo2:
                    ATTACK4_RECT.y -= 5
                elif ATTACK4_RECT.y < player_rect.y - 5 and  taketwo and anothervariable and not taketwo2:
                    ATTACK4_RECT.y += 5
                if now - attack_start_time > attack_delay + 1000 and taketwo and anothervariable and not taketwo2:
                    taketwo2 = True
                if taketwo2 and not ATTACK3_RECT.x > BATTLEBOX_RECT.right + 50:
                    ATTACK3_RECT.x += 10
                    ATTACK4_RECT.x -= 10
                elif ATTACK3_RECT.x > BATTLEBOX_RECT.right + 50:
                    ATTACK_visible = False
                    ATTACK2_visible = False
                    ATTACK3_visible = ATTACK4_visible = False
                    menurestart = True
            elif attacknumber == 4:
                # Spawn first attack
                if not doattack1:
                    ATTACK10_visible = True
                    BLUEATTACK10_image = pygame.transform.scale(
                        BLUEATTACK10_image,
                        (560, 1360)
                    )
                    ATTACK10_RECT = BLUEATTACK10_image.get_rect()
                    ATTACK10_RECT.top = BATTLEBOX_RECT.top - 30
                    ATTACK10_RECT.left = BATTLEBOX_RECT.right
                    doattack1 = True

                # Move first attack
                if ATTACK10_visible:
                    ATTACK10_RECT.x -= 3

                    # When it's off screen, spawn orange attack
                    if ATTACK10_RECT.right < BATTLEBOX_RECT.left - 500:
                        ATTACK10_visible = False
                        ATTACK13_visible = True
                        ORANGEATTACK13_image = pygame.transform.scale(
                            ORANGEATTACK13_image,
                            (560, 1360)
                        )
                        ATTACK13_RECT = ORANGEATTACK13_image.get_rect()
                        ATTACK13_RECT.top = BATTLEBOX_RECT.top - 30
                        ATTACK13_RECT.left = BATTLEBOX_RECT.right

                # Move orange attack
                if ATTACK13_visible:
                    ATTACK13_RECT.x -= 3

                    # Reset cycle when it's offscreen
                    if ATTACK13_RECT.right < BATTLEBOX_RECT.left - 500:
                        ATTACK13_visible = False
                        doattack1 = False  # allows spawning blue again
                now = pygame.time.get_ticks()
                if now > attack_start_time + 50000:
                    ATTACK10_visible = ATTACK13_visible = False
                    ORANGEATTACK13_image = pygame.transform.scale(
                            ORANGEATTACK13_image,
                            (28, 68)
                        )
                    BLUEATTACK10_image = pygame.transform.scale(
                            BLUEATTACK10_image,
                            (28, 68)
                        )
                    menurestart = True
            elif attacknumber == 3:
                if not firstime:
                    ATTACK0_visible = ATTACK_visible = ATTACK2_visible = ATTACK3_visible = ATTACK4_visible = ATTACK9_visible = True
                    ATTACK0_RECT.bottomleft = BATTLEBOX_RECT.topleft
                    ATTACK0_RECT.x -= 150
                    ATTACK0_RECT.y += 75
                    ATTACK0_image = pygame.transform.rotate(ATTACK0_image, -90)
                    ATTACK1_image = pygame.transform.rotate(ATTACK1_image, 180)
                    ATTACK3_image = pygame.transform.rotate(ATTACK3_image, 180)
                    BLUEATTACK9_image = pygame.transform.rotate(BLUEATTACK9_image, 90)
                    ATTACK1_image = pygame.transform.rotate(ATTACK1_image, 180)
                    ATTACK3_image = pygame.transform.rotate(ATTACK3_image, 180)
                    ATTACK2_image = pygame.transform.rotate(ATTACK2_image, 180)
                    ATTACK4_image = pygame.transform.rotate(ATTACK4_image, 180)
                    BLUEATTACK9_image = pygame.transform.rotate(BLUEATTACK9_image, 180)


                    ATTACK2_RECT.x = BATTLEBOX_RECT.left - 150
                    ATTACK4_RECT.x = BATTLEBOX_RECT.left - 150
                    ATTACK2_RECT.y += 75
                    ATTACK4_RECT.y += 75
                    ATTACK_RECT.x = BATTLEBOX_RECT.left - 150
                    ATTACK3_RECT.x = BATTLEBOX_RECT.left - 150
                    ATTACK2_RECT.y = ATTACK0_RECT.y + 35
                    ATTACK3_RECT.y = ATTACK2_RECT.y + 35
                    ATTACK4_RECT.y = ATTACK3_RECT.y + 35
                    ATTACK9_RECT.y = ATTACK4_RECT.y + 35
                    ATTACK_RECT.y = ATTACK9_RECT.y + 35

                    ATTACK9_RECT.x = BATTLEBOX_RECT.left - 150
                    firstime = True
                if firstime and not nextmove:
                    now = pygame.time.get_ticks()
                    if now - attack_start_time > 300:
                        ATTACK_RECT.x += 9
                        ATTACK0_RECT.x += 9
                        ATTACK2_RECT.x += 9
                        ATTACK3_RECT.x += 9
                        ATTACK4_RECT.x += 9
                        ATTACK9_RECT.x += 9

                    if ATTACK_RECT.x > BATTLEBOX_RECT.right + 200 and not nextmove:
                        ATTACK2_RECT.x = BATTLEBOX_RECT.left - 150
                        ATTACK4_RECT.x = BATTLEBOX_RECT.left - 150
                        ATTACK2_RECT.y += 75
                        ATTACK4_RECT.y += 75
                        ATTACK_RECT.x = BATTLEBOX_RECT.left - 150
                        ATTACK3_RECT.x = BATTLEBOX_RECT.left - 150
                        ATTACK2_RECT.y = ATTACK0_RECT.y + 35
                        ATTACK9_RECT.y = ATTACK2_RECT.y + 35
                        ATTACK3_RECT.y = ATTACK9_RECT.y + 35
                        ATTACK4_RECT.y = ATTACK3_RECT.y + 35
                        ATTACK_RECT.y = ATTACK4_RECT.y + 35
                        ATTACK9_RECT.x = BATTLEBOX_RECT.left - 150
                        ATTACK_RECT.x = BATTLEBOX_RECT.left - 150
                        ATTACK0_RECT.x = BATTLEBOX_RECT.left - 150

                        nextmove = True
                if nextmove and not anothernextmove:
                        ATTACK_RECT.x += 9
                        ATTACK0_RECT.x += 9
                        ATTACK2_RECT.x += 9
                        ATTACK3_RECT.x += 9
                        ATTACK4_RECT.x += 9
                        ATTACK9_RECT.x += 9
                if ATTACK_RECT.x > BATTLEBOX_RECT.right + 200 and nextmove and not anothernextmove:
                    ATTACK2_RECT.x = BATTLEBOX_RECT.left - 150
                    ATTACK4_RECT.x = BATTLEBOX_RECT.left - 150
                    ATTACK2_RECT.y += 75
                    ATTACK4_RECT.y += 75
                    ATTACK_RECT.x = BATTLEBOX_RECT.left - 150
                    ATTACK3_RECT.x = BATTLEBOX_RECT.left - 150
                    ATTACK9_RECT.y = ATTACK0_RECT.y + 35
                    ATTACK3_RECT.y = ATTACK9_RECT.y + 35
                    ATTACK4_RECT.y = ATTACK3_RECT.y + 35
                    ATTACK_RECT.y = ATTACK4_RECT.y + 35
                    ATTACK2_RECT.y = ATTACK_RECT.y + 35
                    ATTACK9_RECT.x = BATTLEBOX_RECT.left - 150
                    ATTACK_RECT.x = BATTLEBOX_RECT.left - 150
                    ATTACK0_RECT.x = BATTLEBOX_RECT.left - 150
                    anothernextmove = True
                if anothernextmove:
                        ATTACK_RECT.x += 9
                        ATTACK0_RECT.x += 9
                        ATTACK2_RECT.x += 9
                        ATTACK3_RECT.x += 9
                        ATTACK4_RECT.x += 9
                        ATTACK9_RECT.x += 9
                if anothernextmove and ATTACK_RECT.x > BATTLEBOX_RECT.right + 200:
                    menurestart = True
                    
            elif attacknumber == 6:
                screen.fill((0, 0, 0))  # black background
                done_surface = font.render("You win! Thank you for playing this small demo.  Keep an eye out for when the game is finished!", True, (255, 255, 255)) 
                done_rect = done_surface.get_rect(center=screen.get_rect().center) 
                screen.blit(done_surface, done_rect)
                soul_free_move = False
            elif attacknumber == 5:
                ATTACK1_visible = True
                ATTACK_visible = True
                ATTACK_RECT.center = BATTLEBOX_RECT.center
                if not firstime:
                    player_rect.bottomleft = BATTLEBOX_RECT.topleft
                    firstime = True
                now = pygame.time.get_ticks()
                if now - attack_start_time > 800:
                    rotate += 3

                ATTACK05_image = pygame.transform.scale(ATTACK_image, (112, 272))

                ATTACK1_image = pygame.transform.rotate(ATTACK05_image, int(rotate))

                ATTACK_RECT = ATTACK1_image.get_rect(center=ATTACK_RECT.center)


                # Get the rectangle for positioning
                if now - attack_start_time > 20200:
                    menurestart = True
                    ATTACK_RECT.x += 500
                    ATTACK_visible = False


                
            ATTACK_masks = [pygame.mask.from_surface(img) for img in ATTACK_images]
            BLUEATTACK_masks = [pygame.mask.from_surface(img) for img in BLUEATTACK_images]
            ORANGEATTACK_masks = [pygame.mask.from_surface(img) for img in ORANGEATTACK_images]
            now = pygame.time.get_ticks()
            # === Collision check ===
            for rect, mask in zip(ATTACK_RECTS, ATTACK_masks):
                if player_mask.overlap(mask, (rect.x - player_rect.x, rect.y - player_rect.y)):
                # Collision happened, apply damage
                    previoushp = hp
                    damagedalr = not damagedalr
                    if now - iframes > 300:
                        hp -= 8
                        iframes = now  # mark the time of the hit
                        

            holding_dir = keys[pygame.K_DOWN] or keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_UP]
            for rect, mask in zip(BLUEATTACK_RECTS, BLUEATTACK_masks):
                if player_mask.overlap(mask, (rect.x - player_rect.x, rect.y - player_rect.y)):
                        if holding_dir:
                            previoushp = hp
                            damagedalr = not damagedalr
                            if now - iframes > 300:
                                previoushp = hp
                                hp -= 10
                                iframes = now

            for rect, mask in zip(ORANGEATTACK_RECTS, ORANGEATTACK_masks):
                if player_mask.overlap(mask, (rect.x - player_rect.x, rect.y - player_rect.y)):
                        if not holding_dir:
                            previoushp = hp
                            damagedalr = not damagedalr
                            if now - iframes > 300:
                                previoushp = hp
                                hp -= 10
                                iframes = now

        if hp <= 0:
            screen.fill((0, 0, 0))
            gameoverimage = pygame.image.load(r"gameover_ut.png").convert_alpha()
            gameoverimage = pygame.transform.scale(gameoverimage, (240, 120))
            gameover_rect = gameoverimage.get_rect(center=screen.get_rect().center) 

            player_visible = False
            soul_free_move = False
            screen.blit(gameoverimage, gameover_rect)
            done_surface = font.render("You lose. Thank you for playing this small demo.  Reload the tab to try again", True, (255, 255, 255)) 
            done_rect = done_surface.get_rect(center=screen.get_rect().center) 
            done_rect.y += 150
            screen.blit(done_surface, done_rect)
            #play video / multiple images thats js the death animation maybe force the soul to the middle before it cracks so no menu attacks 


        if doattack1:
            hp = hp #move the attacks
        
        if BATTLE_BOX_visible:
            opponent_RECT.y = BATTLEBOX_RECT.top - 270
        else:
            opponent_RECT.y = BATTLEBOX_RECT.top - 200


        if menurestart:
            firstime = False
            firsttime = False
            first_menu_movement = 0
            second_menu_movement = False
            positioninfirst_menu = 1
            positioninact_menu = 1
            positioninitem_menu = 1 # make it fail in some way
            positioninspare_menu = 1
            goodleftmenupositiony = 0
            goodleftmenupositionx = 0
            doattack1 = False


            illdothislater = "temp"

            showthewordscheck = False
            in_menu = True
            soul_free_move = not in_menu
            menu1_move = True
            menu2_move = False
            onspare = False
            placemercyfailontop = False
            placemercyfailontop2 = False
            oncheck = False
            showtheactualcheckwords = False
            endcheck = False
            anothercheckflag = False
            startfight = False
            continuefight = False
            checkx = False
            turnoff = False
            duringbattle = False
            #stuff
            menurestart = False
            pygame.key.set_repeat(0)  # no repeats, one KEYDOWN per physical press


            extra_visible = False

            ACT1_visible = True
            ACT2_visible = False
            FIGHT1_visible = True
            FIGHT2_visible = False
            SPARE1_visible = True
            SPARE2_visible = False
            ITEM1_visible = True
            ITEM2_visible = False
            ITEM_menu_visible = False
            FIGHT_menu_visible = False
            MERCY_menu_visible = False
            ACT_menu_visible = False
            DIALOGUE_BOX_visible = True
            BATTLE_BOX_visible = False
            BATTLEBAR_visible = False
            workpls = False
            placeopponent = False
            startactualattacks = False
            LOVE_visible = True
            HP_visible = True
            HEALTHBAR_visible = True
            NAME_visible = True
            HP_bar_visible = True
            BATTLEBAR_BAR_visible = False
            stoppablebar = False
            MISSED_visible = False
            MISSEDquestionmark_visible = False
            battlestart = False
            ATTACK0_visible = False
            ATTACK_visible = False
            ATTACK2_visible = False
            ATTACK3_visible = False
            ATTACK4_visible = False
            ATTACK5_visible = False
            ATTACK6_visible = False
            ATTACK7_visible = False
            ATTACK8_visible = False
            ATTACK9_visible = False
            ATTACK10_visible = False
            ATTACK11_visible = False
            ATTACK12_visible = False
            ATTACK13_visible = False
            ATTACK14_visible = False
            ATTACK15_visible = False
            ATTACK16_visible = False
        now = pygame.time.get_ticks()
        if player_visible:
            screen.blit(player_image, player_rect.topleft)
        if now - iframes <= 46:
            player_visible = True
        elif now - iframes <= 100 and now - iframes > 47:
            player_visible = False
        elif now - iframes <= 146 and now - iframes > 100:
            player_visible = True
        elif now - iframes <= 200 and now - iframes > 146:
            player_visible = False
        elif now - iframes <= 246 and now - iframes > 200:
            player_visible = True
        else:
            player_visible = True



            # Update screen
    

        pygame.display.flip()
        await asyncio.sleep(0)
asyncio.run(main())
