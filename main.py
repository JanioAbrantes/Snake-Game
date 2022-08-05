from turtle import Screen
from snake import Snake
from time import sleep
from textos import game_over_message, score
from food import Food

BORDA_X = 380
BORDA_Y = 280

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)  # Tira a animação da tartaruga

snake = Snake()
screen.listen()
comida = Food()

screen.onkey(snake.go_up, 'Up')
screen.onkey(snake.go_down, 'Down')
screen.onkey(snake.go_left, 'Left')
screen.onkey(snake.go_right, 'Right')


def game_over():
    if snake.head.ycor() > BORDA_Y or\
            snake.head.ycor() < -BORDA_Y or\
            snake.head.xcor() > BORDA_X or\
            snake.head.xcor() < -BORDA_X:
        return True

    for parte in range(1, len(snake.minhoca)):
        if snake.head.distance(snake.minhoca[parte]) < 15:
            return True


end_game = False
snake_body = []
high_score_file = open('high_score.txt')
high_score = int(high_score_file.read())
high_score_file.close()

while not end_game:
    current_score = len(snake.minhoca) - 3
    score(current_score, high_score)

    snake.move()
    screen.update()
    sleep(0.1)


    if snake.head.distance(comida) < 15:
        comida.hideturtle()
        comida = Food()
        snake.eat()


    end_game = game_over()

game_over_message()

if current_score > high_score:

    with open('high_score.txt', mode='w') as file:
        file.write(str(current_score))

screen.exitonclick()
