import arcade
import os
import string
import random

# Game constants
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
SPRITE_SCALING = 0.25

# Game states
WIN_PAGE = 0
LOSE_PAGE = 1
GAME_RUNNING = 2

WORDS = [
    "zambia",
    "england",
    "france",
    "nigeria"
]

CHOSEN_WORD = [word for word in WORDS[random.randrange(len(WORDS))]]
LETTERS = list(string.ascii_lowercase)


class Draw:

    @staticmethod
    def base():
        arcade.draw_lrtb_rectangle_filled(165, 395, 200, 165, arcade.color.BROWN_NOSE)

    @staticmethod
    def vertical_pole():
        arcade.draw_lrtb_rectangle_filled(270, 290, 500, 200, arcade.color.BROWN_NOSE)

    @staticmethod
    def horizontal_pole():
        arcade.draw_lrtb_rectangle_filled(270, 440, 500, 487, arcade.color.BLACK)

    @staticmethod
    def hanger():
        arcade.draw_lrtb_rectangle_filled(430, 440, 487, 450, arcade.color.BROWN_NOSE)

    @staticmethod
    def head():
        arcade.draw_lrtb_rectangle_filled(412, 458, 450, 420, arcade.color.BROWN_NOSE)

    @staticmethod
    def body():
        arcade.draw_lrtb_rectangle_filled(430, 440, 420, 410, arcade.color.BROWN_NOSE)
        arcade.draw_lrtb_rectangle_filled(400, 470, 410, 340, arcade.color.BROWN_NOSE)

    @staticmethod
    def left_hand():
        arcade.draw_lrtb_rectangle_filled(470, 510, 400, 380, arcade.color.BLACK)

    @staticmethod
    def right_hand():
        arcade.draw_lrtb_rectangle_filled(360, 400, 400, 380, arcade.color.BLACK)

    @staticmethod
    def right_leg():
        arcade.draw_lrtb_rectangle_filled(450, 470, 340, 250, arcade.color.BLACK)

    @staticmethod
    def left_leg():
        arcade.draw_lrtb_rectangle_filled(400, 420, 340, 250, arcade.color.BLACK)

    @staticmethod
    def win_post():
        arcade.draw_text("WA WINA!!", 250, 400, arcade.color.GOLDEN_BROWN, 54)
        arcade.draw_text("Click to Restart", 310, 350, arcade.color.BLACK, 23)

    @staticmethod
    def lose_post():
        arcade.draw_text("WA LUZA", 250, 400, arcade.color.RED, 54)
        arcade.draw_text(f"The word is {''.join(CHOSEN_WORD).upper()}", 250, 350, arcade.color.BRIGHT_MAROON, 30)
        arcade.draw_text("Click to Play Again", 290, 300, arcade.color.BLACK, 23)


class Hangman(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Hangman")

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        arcade.set_background_color(arcade.color.BISQUE)

        self.show_x = 0
        self.show_y = 0

        self.current_state = GAME_RUNNING

        self.score = 10
        self.wrong_answer_count = 0

        self.right_answer_list = []
        self.wrong_answer_list = []
        self.pressed_keys = []

        self.letter_list = []

        self.A = arcade.Sprite("letters/letter_A.png", SPRITE_SCALING)
        self.B = arcade.Sprite("letters/letter_B.png", SPRITE_SCALING)
        self.C = arcade.Sprite("letters/letter_C.png", SPRITE_SCALING)
        self.D = arcade.Sprite("letters/letter_D.png", SPRITE_SCALING)
        self.E = arcade.Sprite("letters/letter_E.png", SPRITE_SCALING)
        self.F = arcade.Sprite("letters/letter_F.png", SPRITE_SCALING)
        self.G = arcade.Sprite("letters/letter_G.png", SPRITE_SCALING)
        self.H = arcade.Sprite("letters/letter_H.png", SPRITE_SCALING)
        self.I = arcade.Sprite("letters/letter_I.png", SPRITE_SCALING)
        self.J = arcade.Sprite("letters/letter_J.png", SPRITE_SCALING)
        self.K = arcade.Sprite("letters/letter_K.png", SPRITE_SCALING)
        self.L = arcade.Sprite("letters/letter_L.png", SPRITE_SCALING)
        self.M = arcade.Sprite("letters/letter_M.png", SPRITE_SCALING)
        self.N = arcade.Sprite("letters/letter_N.png", SPRITE_SCALING)
        self.O = arcade.Sprite("letters/letter_O.png", SPRITE_SCALING)
        self.P = arcade.Sprite("letters/letter_P.png", SPRITE_SCALING)
        self.Q = arcade.Sprite("letters/letter_Q.png", SPRITE_SCALING)
        self.R = arcade.Sprite("letters/letter_R.png", SPRITE_SCALING)
        self.S = arcade.Sprite("letters/letter_S.png", SPRITE_SCALING)
        self.T = arcade.Sprite("letters/letter_T.png", SPRITE_SCALING)
        self.U = arcade.Sprite("letters/letter_U.png", SPRITE_SCALING)
        self.V = arcade.Sprite("letters/letter_V.png", SPRITE_SCALING)
        self.W = arcade.Sprite("letters/letter_W.png", SPRITE_SCALING)
        self.X = arcade.Sprite("letters/letter_X.png", SPRITE_SCALING)
        self.Y = arcade.Sprite("letters/letter_Y.png", SPRITE_SCALING)
        self.Z = arcade.Sprite("letters/letter_Z.png", SPRITE_SCALING)
        self.Empty = arcade.Sprite("letters/letter.png", SPRITE_SCALING)

        self.letter_list.extend([
            self.A, self.B, self.C, self.D, self.E, self.F, self.G, self.H,
            self.I, self.J, self.K, self.L, self.M, self.N, self.O, self.P, self.Q,
            self.R, self.S, self.T, self.U, self.V, self.W, self.X, self.Y, self.Z, self.Empty])

        self.pos_x = 0
        self.pos_y = 0

        self.x_bottom_positions = [100, 170, 240, 310, 380, 450, 520, 690, 780]
        self.x_top_positions = list(range(50, 800, 50))

        self.body_parts = [Draw.base, Draw.vertical_pole, Draw.horizontal_pole, Draw.hanger,
                           Draw.head, Draw.body, Draw.left_hand, Draw.right_hand, Draw.right_leg,
                           Draw.left_leg]

    def on_key_press(self, key, modifiers):

        print(CHOSEN_WORD)

        if chr(key) not in CHOSEN_WORD:
            print("Wrong key pressed")

        elif chr(key) in self.pressed_keys:
            print("Already chosen")

        elif chr(key) in CHOSEN_WORD:
            self.right_answer_list.append(chr(key))
            self.pressed_keys.append(chr(key))

        elif chr(key) in self.wrong_answer_list:
            print("Already chosen")
        else:
            self.wrong_answer_list.append(chr(key))
            self.wrong_answer_count += 1

        print(self.wrong_answer_count)

    def draw_generator(self):
        for func in self.body_parts:
            yield func()

    def draw_game(self):
        for i in range(0, len(CHOSEN_WORD)):
            self.Empty.center_x = self.x_bottom_positions[i]
            self.Empty.center_y = 100
            self.Empty.draw()

        for letter in self.right_answer_list:
            if CHOSEN_WORD.count(letter) > 1:
                second_index = [i for i, n in enumerate(CHOSEN_WORD) if n == letter][1]
                second_letter = CHOSEN_WORD[second_index]
                second_letter_index = LETTERS.index(second_letter)
                self.letter_list[second_letter_index].center_x = self.x_bottom_positions[second_index]
                self.letter_list[second_letter_index].center_y = 100
                self.letter_list[second_letter_index].draw()

            # to get the second index. Won't work for words with triple letters
            index = CHOSEN_WORD.index(letter)
            letter_index = LETTERS.index(letter)
            self.letter_list[letter_index].center_x = self.x_bottom_positions[index]
            self.letter_list[letter_index].center_y = 100
            self.letter_list[letter_index].draw()

        # Display the wrong and used letters
        for letter in self.wrong_answer_list:
            letter_index = LETTERS.index(letter)
            index = self.wrong_answer_list.index(letter)
            self.letter_list[letter_index].center_x = self.x_top_positions[index]
            self.letter_list[letter_index].center_y = 550
            self.letter_list[letter_index].draw()

        drawer = self.draw_generator()
        for count in range(self.wrong_answer_count):
            next(drawer)

    def on_draw(self):
        arcade.start_render()

        if self.wrong_answer_count == 10:
            self.current_state = LOSE_PAGE

        if self.current_state == GAME_RUNNING:
            self.draw_game()

        elif self.current_state == WIN_PAGE:
            Draw.win_post()

        elif self.current_state == LOSE_PAGE:
            self.draw_game()
            Draw.lose_post()

        else:
            self.draw_game()

def main():
    window = Hangman()
    arcade.run()


main()
