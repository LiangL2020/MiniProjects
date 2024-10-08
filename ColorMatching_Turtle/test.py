# this is the original copy 
import pygame
import random
from button import Button

# TODO: 
#  1. make scenes different classes for organization [CHECK]
#  2. make color blocks turtles (or something else)

# initialize pygame 
pygame.init() 

# constants 
WIDTH, HEIGHT = 800, 600
ROWS, COLS = 3, 3
SQUARE_SIZE = WIDTH // (COLS+2) 
turtle_left = 15 
score = 0 
scene_manager = None 
color_wish = None 

# colors 
WHITE = (255, 255, 255)
GRAY = (158, 158, 158)
BLACK = (0, 0, 0)
COLORS = [(198, 138, 138), (150, 84, 84), (198, 149, 117), (188, 165, 117), (217, 209, 156), (150, 185, 153), (128, 137, 122), (155, 174, 218), (108, 126, 166), (127, 115, 132), (201, 192, 211)]
#          dark pink,       red,           orange,          orange yellow,   yellow,          light green,     dark green,      light blue,      dark blue,       purple,          light purple 

# display score board  
def update_screen(block_size): 
    global turtle_left
    col_pos = 490 

    font_l = pygame.font.SysFont('sfnsmono', 18) 
    text_title = font_l.render("Score Board", True, WHITE)
    text_rect = text_title.get_rect() 
    text_rect.center = (650, 300)
    screen.blit(text_title, text_rect)
    pygame.draw.line(screen, WHITE, (600, 315), (705, 315), 2)

    pygame.draw.rect(screen, BLACK, (580, 320, 160, 60))
    font_s = pygame.font.SysFont('sfnsmono', 15) 
    text_tur = font_s.render("Turtle Left: " + str(turtle_left), True, WHITE)
    text_sco = font_s.render("Score: " + str(score), True, WHITE)
    text_rect_tur = text_tur.get_rect() 
    text_rect_sco = text_sco.get_rect() 
    text_rect_tur.center = (650, 335)
    text_rect_sco.center = (650, 360)
    screen.blit(text_tur, text_rect_tur)
    screen.blit(text_sco, text_rect_sco)

    text_wis = font_s.render("Color Wished: ", True, WHITE)
    text_rect_wis = text_wis.get_rect() 
    text_rect_wis.center = (600, 550)
    screen.blit(text_wis, text_rect_wis)
    pygame.draw.rect(screen, color_wish, (660, 525, 50, 50))

    for i, color in enumerate(COLORS): 
        pygame.draw.rect(screen, color, (col_pos + block_size + i*block_size, block_size, block_size, block_size))

    pygame.display.flip() 

# display available colors to make color wish 
def display_color_for_wish(block_size): 
    global color_wish 
    col_pos = 95 

    font_l = pygame.font.SysFont('sfnsmono', 20) 
    text_wish_dis = font_l.render("Make a color wish!", True, WHITE)
    text_rect_wish_dis = text_wish_dis.get_rect() 
    text_rect_wish_dis.center = (400, 300)
    screen.blit(text_wish_dis, text_rect_wish_dis)

    font_s = pygame.font.SysFont('sfnsmono', 16) 
    text_wish = font_s.render("Color Wished: ", True, WHITE)
    text_rect_wish = text_wish.get_rect() 
    text_rect_wish.center = (200, 160)
    screen.blit(text_wish, text_rect_wish)
    pygame.draw.rect(screen, color_wish, (275, 140, block_size, block_size))

    for i, color in enumerate(COLORS): 
        if i < 5:
            pygame.draw.rect(screen, color, (col_pos + block_size + block_size/2 + i*block_size, block_size + col_pos*3, block_size, block_size))
        else: 
            pygame.draw.rect(screen, color, (col_pos + block_size + (i-5)*block_size, block_size*2 + col_pos*3, block_size, block_size))

    pygame.display.flip() 

def handle_color_wish(x, y, block_size): 
    global color_wish 

    col_pos = 95 
    index = -99 
    if block_size + col_pos*3 <= y <= block_size*2 + col_pos*3: 
        index = (x - col_pos - block_size - block_size/2) // block_size 
        index = int(index) if 0.0 <= index <= 4.0 else -99
        if 0 <= index <= 4: 
            color_wish = COLORS[index]
    elif block_size*2 + col_pos*3 <= y <= block_size*3 + col_pos*3: 
        index = 3 + (x - col_pos + block_size) // block_size
        index = int(index) if 5.0 <= index <= 10.0 else -99
        if 5 <= index <= 10: 
            color_wish = COLORS[index]

# button to add turtle 
def button_turtle(): 
    # TODO: if color_wish make "ding~" 
    global turtle_left, score 
    color = random.choice(COLORS) 
    action_done = False
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] is None:
                board[row][col] = color
                turtle_left -= 1
                if color == color_wish: 
                    score += 1 
                    turtle_left += 1
                action_done = True
                break
        if action_done:
            break

def button_start(): 
    global scene_manager
    scene_manager = "GAME"
    screen.fill(BLACK)

# create screen and initialization 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TURTLE Color Matching')
board = [[None for _ in range(COLS)] for _ in range(ROWS)] 
add_tur = Button(600, 100, 100, 50, WHITE, GRAY, 'add turtle', BLACK, button_turtle)
start_game = Button(550, 150, 100, 40, WHITE, GRAY, "START", BLACK, button_start)

def board_full(board): 
    for row in range(ROWS):
        for col in range(COLS): 
            if board[row][col] == None: 
                return False 
    return True 

# update board 
def update_board(block_size):
    for row in range(ROWS):
        for col in range(COLS):
            color = board[row][col] if board[row][col] else WHITE
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE + block_size, row * SQUARE_SIZE + block_size, SQUARE_SIZE, SQUARE_SIZE))
    for col in range(COLS + 1):
        pygame.draw.line(screen, BLACK, (col * SQUARE_SIZE + block_size, block_size), (col * SQUARE_SIZE + block_size, 3 * SQUARE_SIZE + block_size))
    for row in range(ROWS + 1):
        pygame.draw.line(screen, BLACK, (block_size, row * SQUARE_SIZE + block_size), (3 * SQUARE_SIZE + block_size, row * SQUARE_SIZE + block_size))
    pygame.display.flip() 
    
def contains_pair(pairs, target_pair):
    reversed_pair = (target_pair[1], target_pair[0])
    return target_pair in pairs or reversed_pair in pairs

def check_duplicates(board): 
    global score
    triples = [] 
    pairs = []
    included_coords = set()

    # triples 
    if board[0][0] == board[1][1] == board[2][2]: 
        included_coords.add((0, 0))
        included_coords.add((1, 1))
        included_coords.add((2, 2))
        triples.append(((0, 0), (1, 1), (2, 2)))
    if board[0][2] == board[1][1] == board[2][0]: 
        included_coords.add((0, 2))
        included_coords.add((1, 1))
        included_coords.add((2, 0))
        triples.append(((0, 2), (1, 1), (2, 0)))
    for i in range(ROWS): 
        if board[i][0] == board[i][1] == board[i][2]: 
            included_coords.add((i, 0))
            included_coords.add((i, 1))
            included_coords.add((i, 2))
            triples.append(((i, 0), (i, 1), (i, 2)))
        if board[0][i] == board[1][i] == board[2][i]: 
            included_coords.add((0, i))
            included_coords.add((1, i))
            included_coords.add((2, i))
            triples.append(((0, i), (1, i), (2, i)))
    
    # pairs 
    for row in range(ROWS): 
        for col in range(COLS): 
            color = board[row][col] 
            if color is not None: 
                for row_match in range(ROWS): 
                    for col_match in range(COLS): 
                        if board[row_match][col_match] == color and not (row == row_match and col == col_match): 
                            new_pair = ((row, col), (row_match, col_match))
                            if not contains_pair(pairs, new_pair):
                                if (row, col) not in included_coords and (row_match, col_match) not in included_coords:
                                    pairs.append(new_pair)
                                    included_coords.add((row, col))
                                    included_coords.add((row_match, col_match))
    return triples, pairs

def wait(wait_ms):
    start_time = pygame.time.get_ticks()
    while pygame.time.get_ticks() - start_time < wait_ms:
        # handle events to keep the application responsive
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

def check_empty(board): 
    for row in range(ROWS):
        for col in range(COLS): 
            if board[row][col] != None: 
                return False 
    return True  

def check_board(board, block_size, check_interval): 
    # 考虑优先级，积分可调 
    # 1. 清空 +5 
    # 2. 三连 +3 
    # 3. 隐藏 +2 
    # 4. 许愿色 + 1 
    # 5. 对对碰 + 1  

    global score, turtle_left
    triples, pairs = check_duplicates(board)

    while triples: 
        for r, c in triples[0]: 
            board[r][c] = None
        score += 3 
        turtle_left += 3 
        update_board(block_size)
        update_screen(block_size)
        wait(check_interval)
        triples = triples[1:]

    while pairs: 
        for r, c in pairs[0]: 
            board[r][c] = None
        score += 1 
        turtle_left += 1 
        update_board(block_size)
        update_screen(block_size)
        wait(check_interval)
        pairs = pairs[1:]

    if check_empty(board): 
        score += 5 
        turtle_left += 5 
        update_screen(block_size)

def game_scene(): 
    add_tur.draw(screen)
    update_board(block_size) 
    update_screen(block_size)
    if board_full(board): 
        wait(check_interval)
        check_board(board, block_size, check_interval)  

def menu_scene(): 
    start_game.draw(screen) 
    display_color_for_wish(75)
    pygame.display.flip() 

if __name__ == "__main__": 
    running = True 
    block_size = 25 
    check_interval = 500  # ms
    scene_manager = "MENU" 
    color_wish = BLACK

    screen.fill(BLACK)

    while running: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                running = False 
            if event.type == pygame.MOUSEBUTTONUP: 
                x, y = event.pos 
                if scene_manager == "MENU": 
                    handle_color_wish(x, y, 75)
            add_tur.check_click(event)
            start_game.check_click(event)
        
        if scene_manager == "GAME": 
            game_scene() 
        elif scene_manager == "LOSE": 
            pass 
        elif scene_manager == "WIN": 
            pass 
        else: 
            if scene_manager != "MENU": 
                print("INVALID SCENE") 
            menu_scene() 

    pygame.quit() 
