# This example is not working in Spyder directly (F5 or Run)
# Please type '!python turtle_runaway.py' on IPython console in your Spyder.
import turtle, random
import time

class RunawayGame:
    def __init__(self, canvas, runner, chaser, chaserchaser, catch_radius=50, play_time=30):
        self.canvas = canvas
        self.canvas.title('Turtle Runaway')
        self.runner = runner
        self.chaser = chaser
        self.chaserchaser = chaserchaser
        self.catch_radius2 = catch_radius**2
        self.play_time = play_time

        # Initialize 'runner' and 'chaser' and 'chaserchaser'
        self.runner.shape("data/target.gif")
        self.runner.color('blue')
        self.runner.penup()

        self.chaser.shape("turtle")
        self.chaser.color('red')
        self.chaser.penup()

        self.chaserchaser.shape("data/hammer.gif")
        self.chaserchaser.color('green')
        self.chaserchaser.penup()

        # Instantiate an another turtle for drawing
        self.drawer = turtle.RawTurtle(canvas)
        self.drawer.hideturtle()
        self.drawer.penup()

        # Initialize score
        self.score = 0

        # Initialize time
        self.startTime = time.time()

    def is_runner_catched(self):
        p = self.runner.pos()
        q = self.chaser.pos()
        dx, dy = p[0] - q[0], p[1] - q[1]
        return dx**2 + dy**2 < self.catch_radius2

    def is_chaser_catched(self):
        p = self.chaser.pos()
        q = self.chaserchaser.pos()
        dx, dy = p[0] - q[0], p[1] - q[1]
        return dx**2 + dy**2 < self.catch_radius2

    def start(self, init_dist=400, ai_timer_msec=100):
        self.runner.setpos((-init_dist / 2, 0))
        self.runner.setheading(0)
        self.chaser.setpos((+init_dist / 2, 0))
        self.chaser.setheading(180)

        self.ai_timer_msec = ai_timer_msec
        self.canvas.ontimer(self.step, self.ai_timer_msec)

    def step(self):
        self.runner.run_ai(self.chaser.pos(), self.chaser.heading())
        self.chaser.run_ai(self.runner.pos(), self.runner.heading())
        self.chaserchaser.run_ai(self.chaser.pos(), self.chaser.heading())

        timePassed = time.time() - self.startTime

        isGameOver = False
        if timePassed > self.play_time:
            isGameOver = True

        is_runner_catched = self.is_runner_catched()
        is_chaser_catched = self.is_chaser_catched()

        if is_runner_catched and not isGameOver:
            self.score += 10
        if is_chaser_catched and not isGameOver:
            self.score -= 10

        self.drawer.undo()
        self.drawer.penup()
        self.drawer.setpos(-300, 230)
        if isGameOver:
            self.drawer.write(f'GAME OVER\nyour score is {self.score}',font=["Arial",20,"normal"])
        else:
            self.drawer.write(f'score is {self.score} \ntime left is {self.play_time-int(timePassed)}',font=["Arial",20,"normal"])

        self.canvas.ontimer(self.step, self.ai_timer_msec)

class ManualMover(turtle.RawTurtle):
    def __init__(self, canvas, step_move=10, step_turn=10):
        super().__init__(canvas)
        self.step_move = step_move
        self.step_turn = step_turn

        # Register event handlers
        canvas.onkeypress(lambda: self.forward(self.step_move), 'Up')
        canvas.onkeypress(lambda: self.backward(self.step_move), 'Down')
        canvas.onkeypress(lambda: self.left(self.step_turn), 'Left')
        canvas.onkeypress(lambda: self.right(self.step_turn), 'Right')
        canvas.listen()

    def run_ai(self, opp_pos, opp_heading):
        pass

class RandomMover(turtle.RawTurtle):
    def __init__(self, canvas, step_move=10, step_turn=10):
        super().__init__(canvas)
        self.step_move = step_move
        self.step_turn = step_turn

    def run_ai(self, opp_pos, opp_heading):
        mode = random.randint(0, 2)

        if self.xcor() > 300 or self.xcor() < -300:
            self.right(180)
        elif self.ycor() > 300 or self.ycor() < -300:
            self.right(180)
        elif mode == 0:
            self.left(self.step_turn)
            self.left(self.step_turn)
            self.left(self.step_turn)
        elif mode == 1:
            self.right(self.step_turn)
            self.right(self.step_turn)
            self.right(self.step_turn)

        self.forward(self.step_move)

class IntelligentMover(turtle.RawTurtle):
    def __init__(self, canvas, step_move=20):
        super().__init__(canvas)
        self.step_move = step_move

    def run_ai(self, opp_pos, opp_heading):
        self.setheading(self.towards(opp_pos))
        self.forward(self.step_move)

if __name__ == '__main__':
    canvas = turtle.Screen()
    canvas.addshape("data/hammer.gif")
    canvas.addshape("data/target.gif")

    runner = RandomMover(canvas)
    chaser = ManualMover(canvas)
    chaserchaser = IntelligentMover(canvas)

    game = RunawayGame(canvas, runner, chaser, chaserchaser)
    game.start()
    canvas.mainloop()
