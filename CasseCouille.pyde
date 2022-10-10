from Paddle import Paddle
from Ball import Ball
from Brick import Brick


playingGame = False
endGame = False
bottom = False
bricks = []
score = 0
level = 1

       
def addBrick(x, y, hits):
    brick = Brick(x, y, hits)
    bricks.append(brick)

        

def setup():

    global paddle,ball # on déclare la variable paddle comme globale

    size(605,400)

    paddle = Paddle() # on crée l'objet paddle
    ball = Ball()
    
    for x in range(5, width - 80, 75):
        addBrick(x + 37.5, 50, 3)
        addBrick(x + 37.5, 50, 2)
        addBrick(x + 37.5, 50, 1)


def draw():
    global playingGame, endGame, score, level
    background(loadImage("space.jpg"))

    #appel des méthodes pour le paddle
    ball.loadPic()
    paddle.display() 
    if playingGame:
        #afficher le score
        textSize(20)
        fill("#FFFFFF")
        text("Score:"+str(score),30,40)
        text("Level:"+str(level),30,90)
        textSize(10)
        text("Press S button to pause the game",30,390)
        for i in range (len(bricks)):
            bricks[i].display()
        paddle.checkEdges()
        paddle.update()


        #afficher le menu  
    if playingGame == False:
        textSize(26)
        fill("#FFFFFF")
        text("Le Meilleur Casse-Brique Au Monde",80,100)
        
        textSize(15)
        fill("#FFFFFF")
        text("Par Louis Lacour et Vita Lanko",80,130)
        
        textSize(26)
        fill("#FFFFFF")
        text("(Cliquez Pour commencer)",130,320)
        
        
    for i in range(len(bricks)-1,-1,-1):
        if (ball.meets(bricks[i])):
            bricks.pop(i)
            ball.dir.y*=-1
            score = score + 1
    
    if bricks == []:
        level = level + 1
        ball.vel = ball.vel * 1.1
        for x in range(5, width - 80, 75):
            addBrick(x + 37.5, 50, 3)
            addBrick(x + 37.5, 50, 2)
            addBrick(x + 37.5, 50, 1)
            
# détection des mouvements touches a et d
    ball.display()
    if playingGame:
        ball.checkEdges()
        ball.update()
    if (ball.meets(paddle)):
        if(ball.dir.y > 0):
            ball.dir.y *= -1
            score = score + 1
            
def mousePressed():
    global playingGame
    playingGame = True
    
def keyPressed():

    if key == "a" or key == "A":

        paddle.isMovingLeft = True

    elif key == "d" or key == "D":

        paddle.isMovingRight = True
        
    elif key == "s" or key == "S":
        
        background(51)
        textSize(26)
        fill("#FFFF00")
        text("Pause",250,200)
        noLoop()
        textSize(20)
        fill("#FFFFFF")
        text("Score:"+str(score),30,40)
        text("Level:"+str(level),30,90)
        
    
        

#annulation des mouvements quand on relâche la touche

def keyReleased():

    paddle.isMovingRight = False

    paddle.isMovingLeft = False
    
    loop()
    
    
    
