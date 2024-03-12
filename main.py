# Fill me in!
### Background ###
sky = Rect(0, 0, 400, 300, fill=gradient('lightSkyBlue', 'skyBlue'), border='black')
ground = Rect(0, 300, 400, 100, fill=gradient('lawnGreen', 'springGreen', start='left'), border='black')
gameOverScreen = Rect(0, 0, 400, 400, fill='saddlebrown', border='red', dashes = True, visible = False)

### Sprites ###
randomCoconut = randrange(25,375)
randomBomb = randrange(25, 375)
ball = Circle(randomCoconut, 45, 25, fill=gradient('chocolate', 'peru', start='bottom'), border='black', borderWidth = 1)
bomb = Circle(randomBomb, 45, 25, fill=gradient('black', 'gray', start='bottom'), border='black', borderWidth = 1)

crate = Rect(175, 235, 100, 50, fill=gradient('navajoWhite', 'wheat'),border='black', borderWidth=1)
crateHole = Rect(175, 245, 100, 10, fill='red')
crateHole2 = Rect(175, 263, 100, 10, fill='red')

bombLabel = Label('BOMB!', randomBomb, 45, size=10, font='arial', fill='gold', bold=True)
gameOverLabel = Label('GAME OVER!', 200, 200, size = 50, font='monospace', fill='dodgerBlue', bold = True, visible = False)

Label('Score:', 200, 350, size = 22, fill='black', font='monospace')
score = Label(0, 250, 350, size = 22, fill='black', font='monospace')
### Functions ###
def onStep():
    ball.centerY += 7
    bomb.centerY += 8
    bombLabel.centerY += 8
    if (ball.centerY>272):
        ball.centerX=randrange(20,380)
        ball.centerY=45
        score.value -=1
        ball.centerY=25
        ball.centerX=randrange(25, 375)
    if (bomb.centerY>272):
        bombX = randrange(25, 375)
        bomb.centerX=bombX
        bomb.centerY = 45
        bombLabel.centerX = bombX
        bombLabel.centerY = 45
    if (ball.hitsShape(crate)):
        score.value +=1
        ball.centerY=25
        ball.centerX=randrange(25, 375)
    if (bomb.hitsShape(crate)):
        gameOverScreen.toFront()
        gameOverLabel.toFront()
        gameOverScreen.visible=True
        gameOverLabel.visible=True
    
def onKeyHold(key):
    if ('left' in key):
        crate.centerX-=8
        crateHole.centerX-=8
        crateHole2.centerX-=8
    if ('right' in key):
        crate.centerX+=8
        crateHole.centerX+=8
        crateHole2.centerX+=8
    if ('left' in key and 'right' in key):
        crate.centerX+=0
        crateHole.centerX+=0
        crateHole2.centerX+=0
    if (ball.hitsShape(crate)): 
        score.value +=1
        ball.centerY=25
        ball.centerX=randrange(25, 375)
