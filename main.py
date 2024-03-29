from ColorPicker import ColorPicker
from ColorWindow import ColorWindow
from ForGroundBackGroundColor import ForGroundBackGroundColor
from utils import *
from Theme import Theme
WIN = pygame.display.set_mode((WIDTH + RIGHT_TOOLBAR_WIDTH, HEIGHT))
pygame.display.set_caption("Pyaint")
STATE = "COLOR"
theme = Theme()
color_picker = ColorPicker()
color_window = ColorWindow(theme)
forbackground = ForGroundBackGroundColor()

def init_grid(rows, columns, color):
    grid = []

    for i in range(rows):
        grid.append([])
        for _ in range(columns):  # use _ when variable is not required
            grid[i].append(color)
    return grid


def draw_grid(win, grid):
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            pygame.draw.rect(win, pixel, (j * PIXEL_SIZE, i *
                             PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

    if DRAW_GRID_LINES:
        for i in range(ROWS + 1):
            pygame.draw.line(win, SILVER, (0, i * PIXEL_SIZE),
                             (WIDTH, i * PIXEL_SIZE))
        for i in range(COLS + 1):
            pygame.draw.line(win, SILVER, (i * PIXEL_SIZE, 0),
                             (i * PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT))


def draw_mouse_position_text(win):
    if theme.mode == "light":
        color = BLACK
    else:
        color=WHITE

    pos = pygame.mouse.get_pos()
    pos_font = get_font(MOUSE_POSITION_TEXT_SIZE, False)
    try:
        if picking:
            color_picker.preview_zoomed_color(win)
        row, col = ColorWindow.get_row_col_from_pos(pos)
        text_surface = pos_font.render(str(row) + ", " + str(col), 1, color)
        win.blit(text_surface, (5, HEIGHT - TOOLBAR_HEIGHT))
    except IndexError:
        for button in buttons:
            if not button.hover(pos):
                continue
            if picking:
                color_picker.preview_zoomed_color(win)
            if button.name == "Clear":
                text_surface = pos_font.render("Clear Everything", 1, color)
                win.blit(text_surface, (10, HEIGHT - TOOLBAR_HEIGHT))
                break
            if button.name == "Erase":
                text_surface = pos_font.render("Erase", 1, color)
                win.blit(text_surface, (10, HEIGHT - TOOLBAR_HEIGHT))
                break
            if button.name == "FillBucket":
                text_surface = pos_font.render("Fill Bucket", 1, color)
                win.blit(text_surface, (10, HEIGHT - TOOLBAR_HEIGHT))
                break
            if button.name == "Brush":
                text_surface = pos_font.render("Brush", 1, color)
                win.blit(text_surface, (10, HEIGHT - TOOLBAR_HEIGHT))
                break
            if button.name == "Theme":
                text_surface = pos_font.render("Swap Theme", 1, color)
                win.blit(text_surface, (10, HEIGHT - TOOLBAR_HEIGHT))
                break

            if button.name == "foreground":
                text_surface = pos_font.render("foreground", 1, color)
                win.blit(text_surface, (10, HEIGHT - TOOLBAR_HEIGHT))
                break
            if button.name == "background":
                text_surface = pos_font.render("background", 1, color)
                win.blit(text_surface, (10, HEIGHT - TOOLBAR_HEIGHT))
                break
            if button.name == "ColorPicker":
                text_surface = pos_font.render("ColorPicker", 1, color)
                win.blit(text_surface, (10, HEIGHT - TOOLBAR_HEIGHT))
                break
            if button.name == "ColorWindow":
                text_surface = pos_font.render("ColorPalette", 1, color)
                win.blit(text_surface, (10, HEIGHT - TOOLBAR_HEIGHT))
                break
            r, g, b = button.color
            text_surface = pos_font.render(
                "( " + str(r) + ", " + str(g) + ", " + str(b) + " )", 1, color)
            win.blit(text_surface, (10, HEIGHT - TOOLBAR_HEIGHT))

        for button in brush_widths:
            if not button.hover(pos):
                continue
            if button.width == size_small:
                text_surface = pos_font.render("Small-Sized Brush", 1, color)
                win.blit(text_surface, (10, HEIGHT - TOOLBAR_HEIGHT))
                break
            if button.width == size_medium:
                text_surface = pos_font.render("Medium-Sized Brush", 1, color)
                win.blit(text_surface, (10, HEIGHT - TOOLBAR_HEIGHT))
                break
            if button.width == size_large:
                text_surface = pos_font.render("Large-Sized Brush", 1, color)
                win.blit(text_surface, (10, HEIGHT - TOOLBAR_HEIGHT))
                break


def draw(win, grid, buttons):

    win.fill(BG_COLOR)
    draw_grid(win, grid)

    for button in buttons:
        button.draw(win)

    draw_brush_widths(win)
    draw_mouse_position_text(win)
    pygame.display.update()


def draw_brush_widths(win):
    brush_widths = [
        Button(rtb_x - size_small/2, 568, size_small,
               size_small, forground.color, None, None, "ellipse"),
        Button(rtb_x - size_medium/2, 568+size_small+5, size_medium,
               size_medium, forground.color, None, None, "ellipse"),
        Button(rtb_x - size_large/2, 568+size_small+size_medium+10,
               size_large, size_large, forground.color, None, None, "ellipse")
    ]
    for button in brush_widths:
        button.draw(win)
        # Set border colour
        border_color = BLACK
        if button.color == BLACK:
            border_color = GRAY
        else:
            border_color = BLACK
        # Set border width
        border_width = 2
        if ((BRUSH_SIZE == 1 and button.width == size_small) or (BRUSH_SIZE == 2 and button.width == size_medium) or (BRUSH_SIZE == 3 and button.width == size_large)):
            border_width = 4
        else:
            border_width = 2
        # Draw border
        pygame.draw.ellipse(win, border_color, (button.x, button.y,
                            button.width, button.height), border_width)  # border


def get_position(pos):
    x, y = pos
    row = y // PIXEL_SIZE
    col = x // PIXEL_SIZE

    return row, col


def paint_using_brush(row, col, size):
    if BRUSH_SIZE == 1:
        grid[row][col] = forground.color
    else:  # for values greater than 1
        r = row-BRUSH_SIZE+1
        c = col-BRUSH_SIZE+1

        for i in range(BRUSH_SIZE*2-1):
            for j in range(BRUSH_SIZE*2-1):
                if r+i < 0 or c+j < 0 or r+i >= ROWS or c+j >= COLS:
                    continue
                grid[r+i][c+j] = forground.color

# Checks whether the coordinated are within the canvas


def inBounds(row, col):
    if row < 0 or col < 0:
        return 0
    if row >= ROWS or col >= COLS:
        return 0
    return 1


def fill_bucket(row, col, color):

    # Visiting array
    vis = [[0 for i in range(101)] for j in range(101)]

    # Creating queue for bfs
    obj = []

    # Pushing pair of {x, y}
    obj.append([row, col])

    # Marking {x, y} as visited
    vis[row][col] = 1

    # Until queue is empty
    while len(obj) > 0:

        # Extracting front pair
        coord = obj[0]
        x = coord[0]
        y = coord[1]
        preColor = grid[x][y]

        grid[x][y] = color

        # Popping front pair of queue
        obj.pop(0)

        # For Upside Pixel or Cell
        if inBounds(x + 1, y) == 1 and vis[x + 1][y] == 0 and grid[x + 1][y] == preColor:
            obj.append([x + 1, y])
            vis[x + 1][y] = 1

        # For Downside Pixel or Cell
        if inBounds(x - 1, y) == 1 and vis[x - 1][y] == 0 and grid[x - 1][y] == preColor:
            obj.append([x - 1, y])
            vis[x - 1][y] = 1

        # For Right side Pixel or Cell
        if inBounds(x, y + 1) == 1 and vis[x][y + 1] == 0 and grid[x][y + 1] == preColor:
            obj.append([x, y + 1])
            vis[x][y + 1] = 1

        # For Left side Pixel or Cell
        if inBounds(x, y - 1) == 1 and vis[x][y - 1] == 0 and grid[x][y - 1] == preColor:
            obj.append([x, y - 1])
            vis[x][y - 1] = 1


run = True
clock = pygame.time.Clock()
grid = init_grid(ROWS, COLS, BG_COLOR)

button_width = 40
button_height = 40
button_y_top_row = HEIGHT - TOOLBAR_HEIGHT/2 - button_height - 1
button_y_bot_row = HEIGHT - TOOLBAR_HEIGHT/2 + 1
button_space = 42

size_small = 25
size_medium = 35
size_large = 50

rtb_x = WIDTH + RIGHT_TOOLBAR_WIDTH/2

background = Button(30, HEIGHT - TOOLBAR_HEIGHT/2 - 15, button_width, button_height,
                    forbackground.getBackgroundColor(), name="background", isBorder=True)
forground = Button(10, HEIGHT - TOOLBAR_HEIGHT/2 - 30, button_width, button_height,
                   forbackground.getForegroundColor(), name="foreground", isBorder=True)
back = False
fore = True


brush_widths = [
    Button(rtb_x - size_small/2, 565, size_small,
           size_small, forground.color, None, "ellipse"),
    Button(rtb_x - size_medium/2, 565+size_small+5, size_medium,
           size_medium, forground.color, None, "ellipse"),
    Button(rtb_x - size_large/2, 565+size_small+size_medium+10,
           size_large, size_large, forground.color, None, "ellipse")
]
# Adding Buttons
buttons = []

for i in range(int(len(COLORS)/2)):
    buttons.append(Button(100 + button_space * i, button_y_top_row,
                   button_width, button_height, COLORS[i], isBorder=True))

for i in range(int(len(COLORS)/2)):
    buttons.append(Button(100 + button_space * i, button_y_bot_row, button_width,
                   button_height, COLORS[i + int(len(COLORS)/2)], isBorder=True))

# Right toolbar buttons
# need to add change toolbar button.
for i in range(10):
    if i == 0:
        buttons.append(Button(WIDTH+RIGHT_TOOLBAR_WIDTH/2 - 65/2-2, (i*button_height)+10,
                       70, 38, WHITE, image_url="assets/dark.png", name="Theme"))  # Dark and Light Theme
    else:
        buttons.append(Button(HEIGHT - 2*button_width, (i*button_height)+15, button_width,
                       button_height, WHITE, "B"+str(i-1), BLACK, isBorder=True))  # append tools

buttons.append(Button(WIDTH - button_space-10, button_y_top_row+4, 51, 27.92,
               WHITE, name="Erase", image_url="assets/eraser.png"))  # Erase Button
buttons.append(Button(WIDTH - button_space-10, button_y_bot_row+4, 51, 27.92,
               WHITE, name="Clear", image_url="assets/clear.png"))  # Clear Button
buttons.append(Button(WIDTH - 3*button_space + 20, button_y_top_row, button_width-5,
               button_height-5, name="FillBucket", image_url="assets/paint-bucket.png"))  # FillBucket
buttons.append(Button(WIDTH - 3*button_space + 20, button_y_bot_row, button_width-5,
               button_height-5, name="Brush", image_url="assets/paint-brush.png"))  # Brush
buttons.append(Button(WIDTH - 3*button_space + 140, 460, 45, 45,
               name="ColorPicker", image_url="assets/color-picker.png"))  # ColorPicker
buttons.append(Button(WIDTH - 3*button_space + 140, 510, 45, 45,
               name="ColorWindow", image_url="assets/color-palette.png"))  # ColorPalette
buttons.append(background)
buttons.append(forground)
picking = False
while run:
    clock.tick(FPS)  # limiting FPS to 60 or any other value

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # if user closed the program
            run = False
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            try:
                row, col = ColorWindow.get_row_col_from_pos(pos)
                if picking:
                    color_picker.preview_zoomed_color(WIN)
                    pickedColor = color_picker.pickColor(WIN)
                    forground.color = pickedColor
                    picking = False
                elif STATE == "COLOR":
                    paint_using_brush(row, col, BRUSH_SIZE)
                elif STATE == "FILL":
                    fill_bucket(row, col, forground.color)
            except IndexError:
                for button in buttons:
                    if not button.clicked(pos):
                        continue
                    if button.name == "ColorPicker":
                        picking = True
                        break
                    elif button.name == "Clear":
                        grid = init_grid(ROWS, COLS, WHITE)
                        forground.color = BLACK
                        background.color = WHITE
                        STATE = "COLOR"
                        break
                    elif button.name == "FillBucket":
                        STATE = "FILL"
                        break
                    elif button.name == "Erase":
                        forground.color = background.color
                        break
                    elif button.name == "Theme" and theme.getMode() == 'dark':
                        theme.setMode('light')
                        buttons.pop(18)
                        buttons.insert(18, Button(WIDTH+RIGHT_TOOLBAR_WIDTH/2 - 65/2-2,
                                       10, 70, 38, WHITE, image_url="assets/dark.png", name="Theme"))
                        BG_COLOR = WHITE
                        break
                    elif button.name == "Theme" and theme.getMode() == 'light':
                        theme.setMode('dark')
                        buttons.pop(18)
                        buttons.insert(18, Button(WIDTH+RIGHT_TOOLBAR_WIDTH/2 - 65/2-2,
                                       10, 70, 38, WHITE, image_url="assets/light.png", name="Theme"))
                        BG_COLOR = DARKGRAY
                        break
                    elif button.name == "Brush":
                        STATE = "COLOR"
                        break
                    if button.name == "ColorPicker":
                        picking= True
                        break
                    elif button.name == "ColorWindow":
                        color_window.run(WIN)
                        break
                    if button.name == "background":
                        back = True
                        fore = False
                        break
                    if button.name == "foreground":
                        fore = True
                        back = False
                    if back:
                        background.color = button.color
                        grid = init_grid(ROWS, COLS, background.color)
                    if fore and picking == False:
                        forground.color = button.color
                    break

                for button in brush_widths:
                    if not button.clicked(pos):
                        continue
                    # set brush width
                    if button.width == size_small:
                        BRUSH_SIZE = 1
                    elif button.width == size_medium:
                        BRUSH_SIZE = 2
                    elif button.width == size_large:
                        BRUSH_SIZE = 3
                    STATE = "COLOR"

    draw(WIN, grid, buttons)

pygame.quit()
