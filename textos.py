from turtle import Turtle

turtle_score = Turtle(visible=False)
turtle_score.color('white')
turtle_game_over = Turtle(visible=False)
turtle_game_over.color('white')


def score(current_score, high_score):
    turtle_score.penup()
    turtle_score.goto(-30, 270)
    turtle_score.clear()
    turtle_score.write(f'Score: {current_score}     High Score: {high_score}',
                       align='center', font=('Verdana', 15, 'normal'))

def game_over_message():
    turtle_game_over.penup()
    turtle_game_over.goto(-20, 0)
    turtle_game_over.write('GAME OVER', align='center', font=('Verdana', 15, 'normal'))
