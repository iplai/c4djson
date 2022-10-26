import c4d, random, time, math
import numpy as np
from c4d import BaseContainer
from typing import Optional


class GameCore:
    L, U, R, D = 0, 1, 2, 3

    def __init__(self, rows, cols) -> None:
        self.rows, self.cols = rows, cols
        self.reset()

    def __repr__(self) -> str:
        return str(self.board)

    def reset(self):
        rows, cols = self.rows, self.cols
        self.board = np.zeros((rows, cols), dtype=int)
        self.score = 0
        self.anim_moving = []
        self.anim_create = self.new_tile(2)

    def new_tile(self, count=1):
        result = []
        indexes = np.where(self.board == 0)
        indexes = [(row, col) for row, col in zip(indexes[0], indexes[1])]
        if len(indexes) < count:
            return None
        indexes_selected = np.random.choice(len(indexes), count, False)
        for index in indexes_selected:
            row, col = indexes[index]
            value = 2 if random.random() <= 0.9 else 4
            self.board[row, col] = value
            result.append((row, col, value))
        return result

    def move(self, direction):
        self.anim_moving = []
        board = np.rot90(self.board, direction)
        rows, cols = board.shape

        def t(row, col):
            """还原旋转后的坐标"""
            if direction == 0:
                return row, col
            if direction == 1:
                return col, rows - 1 - row
            if direction == 2:
                return rows - 1 - row, cols - 1 - col
            if direction == 3:
                return cols - 1 - col, row

        for i in range(rows):
            k = 0
            merges = [[] for _ in range(cols)]
            for j in range(cols):
                if j == 0:
                    continue
                if board[i][j] != 0 and board[i][j] == board[i][k]:
                    if not merges[k]:
                        merges[k].append((i, k, board[i][k]))
                    self.score += board[i][j] * 2
                    board[i][k] *= 2
                    merges[k].append((i, j, board[i][j]))
                    board[i][j] = 0
                    merges[j] = []
                    k += 1
                elif board[i][j] != 0:
                    if board[i][k] != 0:
                        k += 1
                    if k != j:
                        board[i][k] = board[i][j]
                        merges[k].append((i, j, board[i][j]))
                        board[i][j] = 0
                        merges[j] = []
            for j in range(cols):
                if merges[j]:
                    for item in merges[j]:
                        row, col, value = item
                        self.anim_moving.append((t(row, col), t(i, j), value))
                elif board[i][j] != 0:
                    self.anim_moving.append((t(i, j), t(i, j), board[i, j]))

        self.board = np.rot90(board, 4 - direction)
        self.anim_create = self.new_tile()

    def completed(self):
        return np.count_nonzero(self.board) == self.board.size


class AnimationGuide:
    def __init__(self, duration: float):
        self.start_time = time.time()
        self.duration = duration

    def reached(self):
        passed = time.time() - self.start_time
        return passed >= self.duration

    def progress(self):
        passed = time.time() - self.start_time
        return passed / self.duration


class GameGeUserArea(c4d.gui.GeUserArea):
    def __init__(self, game: GameCore) -> None:
        super().__init__()
        self.game = game
        self.tilesize, self.tilespace = 48, 8
        self.fps, self.duration = 50, 0.2
        self.animation: Optional[AnimationGuide] = None

    def tile_offset(self, index: int):
        return index * self.tilesize + index * self.tilespace

    def color2vector(self, color_id: int):
        data = self.GetColorRGB(color_id)
        return c4d.Vector(data["r"], data["g"], data["b"]) / 255

    def perform_move(self, move):
        self.animation = AnimationGuide(self.duration)
        self.SetTimer(1000 // self.fps)
        # print(self.game)
        self.game.move(move)
        # print(self.game.anim_moving)

    def reset(self):
        self.game.reset()
        self.animation = AnimationGuide(self.duration)
        self.SetTimer(1000 // self.fps)

    def draw_tile(self, coord: tuple[int, int], coord_to=None, value=0, progress: float = None):
        row, col = coord
        pos = self.tile_offset(col), self.tile_offset(row)

        if progress is not None and coord_to is not None:
            x0, y0 = pos
            row, col = coord_to
            x1, y1 = self.tile_offset(col), self.tile_offset(row)
            x = round(x1 * progress + x0 * (1.0 - progress))
            y = round(y1 * progress + y0 * (1.0 - progress))
            pos = x, y

        pos = self.origin[0] + pos[0], self.origin[1] + pos[1]

        if value != 0:
            exponent = math.log(value, 2)
            percent = exponent / 11.0
            color = (1.0 - percent) * self.color1 + percent * self.color2
        else:
            color = c4d.COLOR_BG

        size = self.tilesize, self.tilesize

        # Add some nice growth effect to a newly spawned tile.
        if progress is not None and value != 0 and coord_to is None:
            x = round(pos[0] + (size[0] / 2) * (1.0 - progress))
            y = round(pos[1] + (size[1] / 2) * (1.0 - progress))
            pos = x, y
            size = round(size[0] * progress), round(size[1] * progress)

        self.DrawSetPen(color)
        self.DrawRectangle(pos[0], pos[1], pos[0] + size[0], pos[1] + size[1])

        if value != 0:
            # Draw the value of the tile into its center.
            flags = c4d.DRAWTEXT_HALIGN_CENTER | c4d.DRAWTEXT_VALIGN_CENTER
            x = pos[0] + size[0] // 2
            y = pos[1] + size[1] // 2
            self.DrawText(str(value), x, y, flags)

    def get_origin(self):
        """Caculate origin point, since the window size may change"""
        w, h = self.GetMinSize()
        x = (self.GetWidth() - w) // 2 + self.tilespace
        y = (self.GetHeight() - h) // 2 + self.tilespace
        self.origin = x, y

    def InitValues(self) -> bool:
        # The two colors for the tiles which we'll fade between.
        self.color1 = self.color2vector(c4d.COLOR_TEXTFOCUS)
        self.color2 = self.color2vector(c4d.COLOR_SYNTAX_COMMENTWRONG)
        return super().InitValues()

    def DrawMsg(self, x1, y1, x2, y2, msg):
        self.OffScreenOn()

        # Draw total background
        self.DrawSetPen(c4d.COLOR_BGEDIT)
        self.DrawRectangle(x1, y1, x2, y2)

        # Set the text color and font, we only need to do this once.
        self.DrawSetTextCol(c4d.COLOR_BGEDIT, c4d.COLOR_TRANS)
        self.DrawSetFont(c4d.FONT_BOLD)

        self.get_origin()

        rows, cols = self.game.rows, self.game.cols

        # Draw background for each tile
        for row in range(rows):
            for col in range(cols):
                self.draw_tile((row, col))

        board = self.game.board

        progress = None
        if self.animation is not None and self.animation.reached():
            self.animation = None
            self.SetTimer(0)
        elif self.animation:
            progress = self.animation.progress()

        if progress is None:
            indexes = np.where(board != 0)
            indexes = [(row, col) for row, col in zip(indexes[0], indexes[1])]
            for index in indexes:
                row, col = index
                value = board[index]
                self.draw_tile((row, col), None, value, progress)
        else:
            if self.game.anim_create:
                for row, col, value in self.game.anim_create:
                    self.draw_tile((row, col), None, value, progress)
            if self.game.anim_moving:
                for coord, coord_to, value in self.game.anim_moving:
                    self.draw_tile(coord, coord_to, value, progress)

    def Message(self, msg: BaseContainer, result: BaseContainer) -> int:
        return super().Message(msg, result)

    def GetMinSize(self):
        w = self.tile_offset(self.game.cols) + self.tilespace
        h = self.tile_offset(self.game.rows) + self.tilespace
        return (w, h)

    def Timer(self, msg):
        self.Redraw()


class MainDialog(c4d.gui.GeDialog):
    ID_MENU_SUBITEM_CLOSE = 10000
    ID_MENU_SUBITEM_RESET = 10001
    ID_TEXT_SCORE = 10004
    ID_USER_AREA_GAME = 10006

    def __init__(self, gamecore: GameCore) -> None:
        super().__init__()
        self.switch = None
        self.hide = True
        self.gamecore = gamecore
        self.userarea = GameGeUserArea(self.gamecore)

    def input_event(self, msg: BaseContainer):
        """
        The :class:`GeUserArea` class has an overwritable method
        `InputEvent()` but we need to catch it manually in the
        :meth:`Message` method of the dialog.
        """
        if msg.GetInt32(c4d.BFM_INPUT_DEVICE) == c4d.BFM_INPUT_KEYBOARD:
            channel = msg.GetInt32(c4d.BFM_INPUT_CHANNEL)
            handled = True
            if channel == c4d.KEY_UP:
                self.userarea.perform_move(GameCore.U)
            elif channel == c4d.KEY_DOWN:
                self.userarea.perform_move(GameCore.D)
            elif channel == c4d.KEY_LEFT:
                self.userarea.perform_move(GameCore.L)
            elif channel == c4d.KEY_RIGHT:
                self.userarea.perform_move(GameCore.R)
            elif channel == c4d.KEY_BACKSPACE:
                self.userarea.reset()
            else:
                handled = False
            if handled:
                self.sync_gui()
            return handled

        return False

    def sync_gui(self):
        """
        We call this method to synchronize the game state with all
        data that is displayed on the UI. Currently, this will just
        redraw the gameUserArea and update the score.
        """
        self.SetString(self.ID_TEXT_SCORE, "  Score: {0}".format(self.gamecore.score))
        self.LayoutChanged(self.ID_TEXT_SCORE)
        self.userarea.Redraw()

    def CreateLayout(self):
        self.SetTitle("2048")

        self.MenuFlushAll()
        self.MenuSubBegin("Menu")
        self.MenuAddString(self.ID_MENU_SUBITEM_CLOSE, "Close")
        self.MenuAddString(self.ID_MENU_SUBITEM_RESET, "Reset")
        self.MenuSubEnd()
        self.MenuFinished()

        self.GroupBeginInMenuLine()
        bc = c4d.BaseContainer()
        bc[c4d.BITMAPBUTTON_BUTTON] = True
        bc[c4d.BITMAPBUTTON_ICONID1] = c4d.RESOURCEIMAGE_BROWSER_HOME
        bc[c4d.BITMAPBUTTON_TOOLTIP] = "Reset"
        self.AddCustomGui(self.ID_MENU_SUBITEM_RESET, c4d.CUSTOMGUI_BITMAPBUTTON, "Reset", c4d.BFH_CENTER | c4d.BFV_CENTER, 0, 0, bc)
        self.AddStaticText(self.ID_TEXT_SCORE, 0, name=f"  Score: {self.gamecore.score}")
        self.GroupEnd()
        # self.AddButton(self.ID_MENU_SUBITEM_RESET, 0, name="Reset")

        self.AddUserArea(self.ID_USER_AREA_GAME, c4d.BFH_SCALEFIT | c4d.BFV_SCALEFIT)
        self.AttachUserArea(self.userarea, self.ID_USER_AREA_GAME)

        return True

    def InitValues(self) -> bool:
        return super().InitValues()

    def Command(self, id, msg):
        if id == self.ID_MENU_SUBITEM_CLOSE:
            self.Close()
        if id == self.ID_MENU_SUBITEM_RESET:
            self.userarea.reset()
        return True

    def Message(self, msg: BaseContainer, result: BaseContainer) -> int:
        if msg.GetId() == c4d.BFM_INPUT:
            return self.input_event(msg)
        return super().Message(msg, result)


if __name__ == "__main__":
    dialog = MainDialog(GameCore(5, 6))
    dialog.Open(c4d.DLG_TYPE_ASYNC, 0, -2, -2)
