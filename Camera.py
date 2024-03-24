from pygame import Vector2, Surface, Rect

class Camera:
    def __init__(self, subjectSurface: Surface, frame: Rect) -> None:
        self.subjectSurface: Surface = subjectSurface
        self.frame: Rect = frame
        self.screenLocation: Vector2 = Vector2(frame.left, frame.top)
        self.surfaceLocation: Vector2 = Vector2(0, 0)
    
    def draw(self, screenSurface: Surface):
        # focusRect: Rect = Rect(0, 0, self.frame.width, self.frame.height)
        screenSurface.blit(self.subjectSurface.subsurface((self.surfaceLocation.x, self.surfaceLocation.y, self.frame.width, self.frame.height)), self.screenLocation) #, focusRect)
    
    def moveDirection(self, direction: str):
        if direction == "DOWN":
            self.surfaceLocation.y += 16
        if direction == "UP":
            self.surfaceLocation.y -= 16
        if direction == "RIGHT":
            self.surfaceLocation.x += 16
        if direction == "LEFT":
            self.surfaceLocation.x -= 16
        self.clampSurfaceLocation()
        
    def focus(self, boardPosition: Vector2):
        self.surfaceLocation.y = boardPosition.y * 16 - (self.frame.height / 2)
        self.surfaceLocation.x = boardPosition.x * 16 - (self.frame.width  / 2)
        self.clampSurfaceLocation()

    def clampSurfaceLocation(self):
        if (self.surfaceLocation.y + self.frame.height) > self.subjectSurface.get_height():
            self.surfaceLocation.y = self.subjectSurface.get_height() - self.frame.height
        if self.surfaceLocation.y < 0:
            self.surfaceLocation.y = 0
        if (self.surfaceLocation.x + self.frame.width) > self.subjectSurface.get_width():
            self.surfaceLocation.x = self.subjectSurface.get_width() - self.frame.width
        if self.surfaceLocation.x < 0:
            self.surfaceLocation.x = 0