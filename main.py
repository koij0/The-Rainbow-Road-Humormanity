# CREATED BY: KOI JOHNSON
## LAST UPDATED: 5/5/26


# IMPORTS
import pygame
import sys
import random
import textwrap
import os

# For WebAssembly
import asyncio

async def main ():

    # Configuration
    RES_WIDTH, RES_HEIGHT = 640, 480
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    color = WHITE
    r = 255
    g = 0
    b = 0
    MODE = 0
    option = 0
    m = 20
    t = 20
    p = 20
    m_gauge = ""
    t_gauge = ""
    p_gauge = ""
    z1 = 255
    z2 = 0
    z3 = 0
    phase = 0
    ZONE = False
    popup = 0
    round = ""
    i = 0
    q = 0
    result = None
    people = ["friend", "family"]
    major = ["Same-Sex Marriage", "Gender-Affirming Care"]
    start = pygame.Rect(0,0,0,0)
    opt1 = pygame.Rect(0,0,0,0)
    opt2 = pygame.Rect(0,0,0,0)
    opt3 = pygame.Rect(0,0,0,0)
    next = pygame.Rect(0,0,0,0)
    yay = pygame.Rect(0,0,0,0)
    nay = pygame.Rect(0,0,0,0)
    landmark = False

    f = 0
    k = 0
    banned = 0
    st = 0
    part = 0
    waive = False
    violence = 0
    score = 0
  
    


    # SCENARIOS
    scenario1 = []
    action1 = []

    with open('scenarios1.txt', 'r') as file1:
            for line in file1:
                line = line.strip()
                line = line.split(",")
                scenario1.append(line[0])
                action1.append(line[1].split("~"))



    scenario2 = []
    action2 = []

    with open('scenarios2.txt', 'r') as file2:
            for line in file2:
                line = line.strip()
                line = line.split(",")
                scenario2.append(line[0])
                action2.append(line[1].split("~"))

    # LEARN FILE
    question = []
    answer = []
    mchoice = []

    with open('learn.txt', 'r') as learnfile:
            for line in learnfile:
                line = line.strip()
                line = line.split(",")
                question.append(line[0])
                answer.append(line[1])
                mchoice.append(line[2].split("~"))


    # STATES
    state = []
    ban1= []
    ban2 = []

    with open('state.txt', 'r') as statefile:
            for line in statefile:
                line = line.strip()
                line = line.split(",")
                state.append(line[0])
                ban1.append(line[1])
                ban2.append(line[2])


    
                
                

    pygame.mixer.pre_init(48000, -16, 2, 512) 

    pygame.init()
        
    
    #AUDIO
    base_path = os.path.dirname(__file__)
    path = os.path.join(base_path, 'music.ogg')
    music = pygame.mixer.Sound(path)

    screen = pygame.display.set_mode((RES_WIDTH, RES_HEIGHT))
    pygame.display.set_caption("The Rainbow Road")
    clock = pygame.time.Clock()

    # State setup
    state_box = pygame.Rect(195, 150, 250, 50)

    # initials score
    initials = pygame.Rect(250, 150, 100, 50)


    # --- Assets ---
    # Use a monospaced font for that computer terminal feel
    font = pygame.font.Font('courier.ttf', 24)



    def draw_text(text, x, y, color=WHITE):
        img = font.render(text, True, color)
        screen.blit(img, (x, y))

    def wrap(surface, text, sfont, color, x, y, max_width):
                # Split text into lines that fit within max_width
                wrapped_lines = textwrap.wrap(text, width=max_width // (sfont.size(' ')[0] // 2))

                for i, line in enumerate(wrapped_lines):
                    line_surf = sfont.render(line, True, color)
                    surface.blit(line_surf, (x, y + i * sfont.get_height()))


    def draw_sym(x, y, w, l, r):
        # Circle
        pygame.draw.circle(screen, WHITE, (x,y), 30 - r, width=0)
        pygame.draw.circle(screen, BLACK, (x,y), 20 - r, width=0)
        # Left 
        pygame.draw.line(screen, WHITE, (x-60, y-40), (x-22, y-10), 10-l)
        pygame.draw.rect(screen, WHITE, (x-65, y - 45, 8-w, 25-l))
        pygame.draw.rect(screen, WHITE, (x-65, y - 45, 25-w, 8-l))
        pygame.draw.line(screen, WHITE, (x-48, y-10), (x-30, y-35), 8-l)
        # Right 
        pygame.draw.line(screen, WHITE, (x+60, y-40), (x+22, y-10), 10-l)
        pygame.draw.rect(screen, WHITE, (x+60, y - 45, 8-w, 25-l))
        pygame.draw.rect(screen, WHITE, (x+40, y - 45, 25-w, 8-l))
        # Bottom
        pygame.draw.rect(screen, WHITE, (x-5, y + 25, 10-w, 50-l))
        pygame.draw.rect(screen, WHITE, (x-15, y + 40, 30-w, 10-l))

    def draw_start():
        pygame.draw.rect(screen, (r,g,b), (220, 390 , 200, 50))
        draw_text("START", 280, 405, BLACK)
        

    def draw_stats():
        draw_text("- POWER STATS -", 50, 360)
        draw_text(f"Mental Health: {m_gauge} [{m}]", 50, 390)
        draw_text(f"Trauma: {t_gauge} [{t}]", 50, 420)
        draw_text(f"Pride: {p_gauge} [{p}]", 50, 450)

    def draw_cloud(x, y):
        # Draw a simple puffy cloud with 3 circles
        pygame.draw.ellipse(screen, WHITE, (x-40, y, 70, 30))
        pygame.draw.circle(screen, WHITE, (x+22, y-5), 25)
        pygame.draw.ellipse(screen, WHITE, (x+20, y, 70, 30))


    def draw_option1(r, g, b, y):
        pygame.draw.rect(screen, (r,g,b), (40, 150-y, 250, 50))
    def draw_option2(r, g, b, y):
        pygame.draw.rect(screen, (r,g,b), (350, 150-y, 250, 50))
    def draw_option3(r, g, b, x, y):
        pygame.draw.rect(screen, (r,g,b), (195-x, 230-y, 250, 50))
    def draw_next(r, g, b, x, y):
        pygame.draw.rect(screen, (r,g,b), (195-x, 230-y, 250, 50))
        draw_text("NEXT", 290-x, 245-y, color)

    def draw_state():
        pygame.draw.rect(screen, (r,g,b), state_box, 2)
        pygame.draw.rect(screen, (255,0,0), (195, 200, 80, 50))
        pygame.draw.rect(screen, (0,255,0), (365, 200, 80, 50))

    def draw_initial():
        pygame.draw.rect(screen, (r,g,b), initials, 2)
        pygame.draw.rect(screen, (255,0,0), (250, 200, 50, 50))
        pygame.draw.rect(screen, (0,255,0), (300, 200, 50, 50))

    # --- Main Game Loop ---
    while True:
        screen.fill(BLACK)


        # Check for Violence
        if violence != 0 and violence <= 6:
            MODE = -3

        if z1 == 255 and z2 == 255:
            color = BLACK
        else:
            color = WHITE
        

        # Check for Win
        if z1 == 0 and z2 == 0 and z3 == 0:
            MODE = -2

        # Check STATS

        if m <= 0 or t <= 0: 
            MODE = -1
        elif m <= 5: 
            m_gauge = "Detrimental"
        elif m <= 10:
            m_gauge = "Mild"
        elif m <= 15:
            m_gauge = "Good"
        elif m <=20:
            m_gauge = "Harmonious"
        
        if t <= 5: 
            t_gauge = "..."
        elif t <= 10: 
            t_gauge = "In need of a Trauma Dump"
        elif t <= 15: 
            t_gauge = "Healing~"
        elif t <= 20: 
            t_gauge = "I feel so supported :)"

        if p <= 5:
            p_gauge = "It's just a phase..."
        elif p <= 10:
            p_gauge = "It's Slay or be Slayed"
        elif p <= 15:
            p_gauge = "Currently werking it!"
        elif p <= 20:
            p_gauge = "OUT AND PROUD"
        

        # GAME OVER
        if MODE == -1:
            draw_text("GAME OVER.", 250, 90)
            draw_text("TRY AGAIN.", 250, 120)
            draw_stats()
            f = 0
            k = 0
            z1 = 255
            z2 = 0
            z3 = 0
            phase = 0
            waive = False
            firsti = ""
            lasti = ""
            l = 0
            draw_next(r, g, b, 0, 50)
            next = pygame.Rect(195, 180, 250, 50)

        # YOU WIN!
        if MODE == -2:
            music.set_volume(0.5)
            if not pygame.mixer.get_busy():
                music.play()
            draw_text("YOU WON!!!", 250, 50)
            if score == 0:
                wrap(screen, "Congratulations on fostering self-acceptance, building community, and advancing rights through visibility, resistance, and joy! ", font, WHITE, 80, 120, 250)
                draw_text("(Turn Audio On!)", 210, 80)
            
            draw_stats()
            pygame.draw.rect(screen, (r, b, g), (0, 300, RES_WIDTH, 50))
            draw_text("Created by: Koi Johnson", 170, 315, BLACK)

        # ASSAULT
        if MODE == -3:
            draw_text("You were a fatal victim of a Hate Crime...", 30, 90)
            draw_text("GAME OVER.", 250, 120)
            draw_text("TRY AGAIN.", 250, 150)
            wrap(screen, "LGBT people are more likely to experience violent hate crimes with a rate of 6.4 per 1,000, compared with the rate of 0.7 per 1,000 for non-LGBT persons.", font, WHITE, 80, 200, 250)
            f = 0
            k = 0
            z1 = 255
            z2 = 0
            z3 = 0
            waive = False
            phase = 0
            firsti = ""
            lasti = ""
            l = 0
            draw_next(r, g, b, 0, -150)
            next = pygame.Rect(195, 380, 250, 50)
        
        # Background
        pygame.draw.line(screen, (r, g, b), (0, 350), (RES_WIDTH, 350), 2)
        draw_text("THE RAINBOW ROAD", 200, 20, (r, g ,b))
        
        # Play Screen 
        if MODE == 0:
            draw_start()
            start = pygame.Rect(220, 390, 200, 50)
            draw_sym(320, 200, 0, 0, 0)
        
        # Start Screen
        if MODE == 1:
            draw_text("You may:", 100, 100)
            draw_option1(r, g, b, 0)
            opt1 = pygame.Rect(40, 150 , 250, 50)
            draw_option2(r, g, b, 0)
            opt2 = pygame.Rect(350, 150 , 250, 50)
            draw_text("ROAM", 130, 165)
            draw_text("LEARN", 435, 165)
            draw_text("What will you do? ", 100, 230)
            
            if option == 1:
                MODE = 3
                option = 0
            elif option == 2: 
                MODE = 2
                option = 0

        # Learn about the Road
        if MODE == 2:
            wrap(screen, "You are about to begin a great adventure, traveling the 'Rainbow Road' across the traumatic experiences of queer individuals. Your hidden identity and failing mental health, will accompany you from the 'Closet' to the eventual acceptance from society...You may face discrimination, stigma, and violence. Stay focused on the goal of always having to fight for your 'True Self'. Good luck, and watch out for more trauma!", font, WHITE, 30, 50, 300)
            draw_next(r, g, b, -25, -160)
            next = pygame.Rect(220, 390 , 250, 50)

        # Character Choice Screen
        if MODE == 3:
            draw_text("Many kinds of people have 'come out'...", 50, 100)
            draw_option1(r, g, b, 0)
            opt1 = pygame.Rect(40, 150 , 250, 50)
            draw_option2(r, g, b, 0)
            opt2 = pygame.Rect(350, 150 , 250, 50)
            draw_option3(r, g, b, 0, 0)
            opt3 = pygame.Rect(195, 230 , 250, 50)
            draw_text("Gender?", 110, 165)
            draw_text("Sexuality?", 405, 165)
            draw_text("Info?", 280, 245)
            draw_text("What will you do? ", 50, 310)
            if option == 1:
                MODE = 6
                option = 0
            elif option == 2: 
                MODE = 5
                option = 0
            elif option == 3:
                MODE = 4
                option = 0

        # Recieve Choice's Stat Bar - Gender
        if MODE == 6:
            m = 15
            t = 20
            p = 5
            k = 1
            ban = ban2
            choice = scenario1
            action = action1
            MODE = 7

        # Recieve Choice's Stat Bar - Sexuality
        if MODE == 5:
            m = 15
            t = 20
            p = 5
            k = 0
            ban = ban1
            choice = scenario2
            action = action2
            MODE = 7

        # Learn about the choices
        if MODE == 4:
            wrap(screen, "Coming out isn't easy! Coming out is a profoundly personal and often daunting process that can induce significant stress, fear, and anxiety. Key challenges include the risk of rejection by family and friends, discrimination, legal barriers, internalized hate, and the constant need to re-identify in new social situations...If your mental health or trauma drop to 0, it's GAME OVER!! Good luck!", font, WHITE, 50, 50, 280)
            draw_next(r, g, b, -25, -160)
            next = pygame.Rect(220, 390 , 250, 50)

        # Leave the CLOSET
        if MODE == 7:
            draw_text("You are now leaving the CLOSET...", 100, 100)
            draw_text("Good Luck!!!", 150, 150)
            draw_next(r, g, b, 0, 0)
            next = pygame.Rect(195, 230, 250, 50)
        
        # Stats 
        if MODE >= 7:
            draw_stats()

        # Main Screen
        if MODE == 8:
            pygame.draw.rect(screen, (z1, z2, z3), (0, 300, RES_WIDTH, 50))
            draw_text(f"ZONE: ({z1}, {z2}, {z3})", 200, 315, color)
            draw_cloud(90, 220)
            draw_cloud(500, 220)
            if popup >= 0 and popup%2 == 0:
                draw_text("You may:", 50, 50)
                draw_option1(z1, z2, z3, 50)
                opt1 = pygame.Rect(40, 100, 250, 50)
                draw_option2(z1, z2, z3, 50)
                opt2 = pygame.Rect(350, 100, 250, 50)
                draw_text("CONTINUE", 105, 115, color)
                draw_text("THERAPY", 420, 115, color)
                draw_text("What will you do? ", 50, 275)
                # draw_char(600, 400)
                if option == 1:
                    ZONE = True
                    popup = random.randint(1,5)
                    violence = random.randint(1,1000)
                    if m <= 5:
                        t -= 2
                    # Waive status
                    if waive == True:
                        m -= 5
                        t -= 5
                        p -= 5
                    option = 0
                elif option == 2: 
                    violence = random.randint(1,1000)
                    MODE = 10
                    option = 0
            elif popup%2 != 0:
                round = random.choice(choice)
                idx = choice.index(round)
                m += int(action[idx][0])
                t += int(action[idx][1])
                p += int(action[idx][2])
                popup = -2
            elif popup == -2:
                wrap(screen, round, font, WHITE, 50, 70, 250)
                draw_text("Check Power Stats.", 150, 150)
                draw_next(z1, z2, z3, 0, 50)
                next = pygame.Rect(195, 180, 250, 50)
            elif popup == -4:
                draw_text(f"Your {people[f]} suspects you're queer...", 50, 50)
                draw_option1(z1, z2, z3, 50)
                opt1 = pygame.Rect(40, 100, 250, 50)
                draw_option2(z1, z2, z3, 50)
                opt2 = pygame.Rect(350, 100, 250, 50)
                draw_option3(z1, z2, z3, 0, 50)
                opt3 = pygame.Rect(195, 180 , 250, 50)
                draw_text("TALK", 130, 115, color)
                draw_text("IGNORE", 430, 115, color)
                draw_text("INFO", 290, 195, color)
                draw_text("What will you do? ", 50, 275)
                if option == 1:
                    popup = -6
                    landmark = True
                    option = 0
                elif option == 2: 
                    popup = -8
                    landmark = True
                    option = 0
                elif option == 3:
                    MODE = 9
                    option = 0

            elif popup == -6:
                if p >= 10: 
                    draw_text(f"Your {people[f]} supports you!", 50, 70)
                    if landmark == True:
                        m += 3
                        t -= 1
                        p += 3
                        ZONE = True
                    landmark = False
                else:
                    draw_text(f"Your {people[f]} rejects you...", 50, 70)
                    if landmark == True:
                        m -= 3
                        t -= 3
                        p -= 3
                        ZONE = True
                    landmark = False
                    if people[f] == "family":
                        draw_text("They send you to conversion camp...", 50, 130)
                        phase = 0
                        z1 = 255
                        z2= 0
                        z3 = 0
                draw_text("Check Power Stats.", 150, 100)
                draw_next(z1, z2, z3, 0, 50)
                next = pygame.Rect(195, 180, 250, 50)

            elif popup == -8:
                if p >= 5: 
                    draw_text(f"Your {people[f]} don't question more...", 50, 70)
                    if landmark == True:
                        m += 1
                        t -= 1
                        ZONE = True
                    landmark = False
                else:
                    draw_text(f"Your {people[f]} confronts you...", 50, 70)
                    if landmark == True:
                        m -= 3
                        t -= 3
                        p -= 3
                        ZONE = True
                    landmark = False
                    if people[f] == "family":
                        draw_text("They send you to conversion camp...", 50, 130)
                        phase = 0
                        z1 = 255
                        z2= 0
                        z3 = 0
                draw_text("Check Power Stats.", 150, 100)
                draw_next(z1, z2, z3, 0, 50)
                next = pygame.Rect(195, 180, 250, 50)
                

            elif popup == -10:
                draw_text(f"Time to apply for {major[k]}!", 50, 50)
                draw_option1(z1, z2, z3, 50)
                opt1 = pygame.Rect(40, 100, 250, 50)
                draw_option2(z1, z2, z3, 50)
                opt2 = pygame.Rect(350, 100, 250, 50)
                draw_option3(z1, z2, z3, 0, 50)
                opt3 = pygame.Rect(195, 180 , 250, 50)
                draw_text("APPLY", 130, 115, color)
                draw_text("WAIVE", 430, 115, color)
                draw_text("INFO", 290, 195, color)
                draw_text("What will you do? ", 50, 275)
                if option == 1:
                    popup = -12
                    landmark = True
                    option = 0
                elif option == 2: 
                    waive = True
                    ZONE = True
                    option = 0
                    popup = 0
                elif option == 3:
                    MODE = 9
                    part = 1
                    option = 0

            elif popup == -12:
                draw_text("Choose a State to live in: ", 50, 50)
                draw_state()
                draw_text(state[st], 220, 165)
                nay = pygame.Rect(195, 200, 80, 50)
                draw_text("NO", 220, 215)
                yay = pygame.Rect(365, 200, 80, 50)
                draw_text("YES", 385, 215)
                if banned == 1:
                    draw_text(f"{major[k]} is banned here.", 50, 80)
                    draw_text("Choose a different State.", 50, 105)
                    draw_text("Check Power Stats.", 195, 270)
                elif banned == 2:
                    draw_text(f"Congrats on your {major[k]}!", 50, 100)
                    draw_text("Check Power Stats.", 195, 270)
                    if landmark == True:
                        ZONE = True
                    landmark = False
                    draw_next(z1, z2, z3, 0, 80)
                    next = pygame.Rect(195, 150, 250, 50)


                
            

            
        # Advance ZONE
        if ZONE == True:
            if phase == 0:  # Red -> Yellow (add green)
                z2 += 51
                if z2 >= 255:
                    z2 = 255
                    phase = 1

            elif phase == 1:  # Yellow -> Green (remove red)
                z1 -= 51
                if z1 <= 0:
                    z1 = 0
                    phase = 2

            elif phase == 2:  # Green -> Blue (swap green for blue)
                z2 -= 51
                z3 += 51
                if z2 <= 0 and z3 >= 255:
                    z2 = 0
                    z3 = 255
                    phase = 3

            elif phase == 3:  # Blue -> Black (fade out blue)
                z3 -= 51
                if z3 <= 0:
                    z3 = 0
                    phase = 4
        ZONE = False


        # LEARN MINI-GAME
        if MODE == 10:
            if q >= len(question):
                q = 0
            draw_text("Welcome to Therapy!", 180, 50)
            draw_text(f"QUESTION: ", 10, 80)
            wrap(screen, question[q], font, WHITE, 150, 80, 250)
            draw_option1(z1, z2, z3, -50)
            opt1 = pygame.Rect(40, 200, 250, 50)
            draw_option2(z1, z2, z3, -50)
            opt2 = pygame.Rect(350, 200, 250, 50)
            draw_option3(z1, z2, z3, 155, -50)
            opt3 = pygame.Rect(40, 280 , 250, 50)
            draw_text(f"{mchoice[q][0]}", 130, 215, color)
            draw_text(f"{mchoice[q][1]}", 430, 215, color)
            draw_text(f"{mchoice[q][2]}", 135, 295, color)
            if result is None:
                if option > 0:
                    if option == int(answer[q]):
                        result = "correct"
                        i += 1
                        m += 1
                        t += 1
                        p += 1
                    else:
                        result = "incorrect"
            if result == "correct":
                draw_text("CORRECT! Gained Power.", 180, 165)
                draw_next(r, g, b, -155, -50)
                next = pygame.Rect(350, 280, 250, 50)
            elif result == "incorrect":
                draw_text("INCORRECT. Try Again.", 180, 165)
                draw_next(r, g, b, -155, -50)
                next = pygame.Rect(350, 280, 250, 50)
                                
            
        # LANDMARKS
        if z1 == 255 and z2 == 255 and z3 == 0: 
            if popup >= 0 and popup%2 == 0:
                f = 0
                popup = -4
        elif z1 == 0 and z2 == 255 and z3 == 0:
            if popup >= 0 and popup%2 == 0:
                f = 1
                popup = -4
        elif z1 == 0 and z2 == 0 and z3 == 255:
            if popup >= 0 and popup%2 == 0:
                popup = -10


        # Random info
        if MODE == 9:
            if part == 0:
                wrap(screen, "If you have a lot of Pride, the talk will go well! But if you’re not that proud yet, things may go south...so it might be best to avoid confrontation...", font, WHITE, 80, 60, 250)
            elif part == 1:
                if choice == scenario1:
                    wrap(screen, "You're a youth who is hoping to get Gender-Affiming Care. If you WAIVE, you will lose Pride and build Trauma/Mental Health...If you APPLY, there will be additional steps...it's not a quick and easy process...", font, WHITE, 80, 60, 250)
                elif choice == scenario2:
                    wrap(screen, "It's before the Obergefell v. Hodges case. If you WAIVE, you will lose Pride and build Trauma/Mental Health...If you APPLY, there will be additional steps...it's not a quick and easy process...", font, WHITE, 80, 60, 250)
            draw_next(r, g, b, -25, -20)
            next = pygame.Rect(220, 250 , 250, 50)
        

                
        # DISPLAY LOOP
        pygame.display.flip()
        clock.tick(60)

        await asyncio.sleep(0)


        # Change color - background
        if r == 255 and g < 255 and b == 0:
            g += 5
        elif g == 255 and r > 0:
            r -= 5
        elif g == 255 and b < 255:
            b += 5
        elif b == 255 and g > 0:
            g -= 5
        elif b == 255 and r < 255:
            r += 5
        elif r == 255 and b > 0:
            b -= 5

        # Clamp values (just in case)
        r = max(0, min(255, r))
        g = max(0, min(255, g))
        b = max(0, min(255, b))


        # Events 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.quit()
                pygame.quit() # Uninitializes all pygame modules
                sys.exit() 

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Get the (x, y) position of the mouse click
                mouse_pos = event.pos 
                
                # Start Button Click
                if start.collidepoint(mouse_pos):
                    MODE = 1
                    start = pygame.Rect(0,0,0,0)
                # Option Button Click
                elif opt1.collidepoint(mouse_pos):
                    option = 1
                    opt1 = pygame.Rect(0,0,0,0)
                elif opt2.collidepoint(mouse_pos):
                        option = 2
                        opt2 = pygame.Rect(0,0,0,0)
                elif opt3.collidepoint(mouse_pos):
                    option = 3
                    opt3 = pygame.Rect(0,0,0,0)
                elif next.collidepoint(mouse_pos):
                    if MODE >= 7:
                        if result == "correct":
                            q += 1
                        MODE = 8
                        ZONE = False
                        result = None
                        option = 0
                        popup = 0
                    if MODE == -1 or MODE == -3:
                        MODE = 0
                        m = 1
                        t = 1
                        violence = 0
                    if MODE == 2 or MODE == 4 or MODE == 9:
                        MODE -= 1
                        part = 0
                    next = pygame.Rect(0,0,0,0)
                elif yay.collidepoint(mouse_pos):
                    if MODE == 8: 
                        if ban[st] == "True":
                            banned = 1
                            m -= 2
                            t -= 2
                            p -= 2
                        elif ban[st] == "False":
                            banned = 2
                            m += 2
                            t += 2
                            p += 2
                elif nay.collidepoint(mouse_pos):
                    if MODE == 8:
                        st = random.randint(0,49)
                        banned = 0
               
               
               
                
               

            

            
            

        
                            
                        
asyncio.run(main())                       
                        



        
        