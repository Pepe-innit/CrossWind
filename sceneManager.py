
class SceneManager:
    def __init__(self):
        self.current_scene = None
        self.main_menu = None
        self.game_scene = None
        self.shop_scene = None

    #--- Methods ---

    def set_scene(self, scene):
        self.current_scene = scene

    def handle_events(self, events):
        if self.current_scene:
            self.current_scene.handle_events(events)

    def update(self):
        if self.current_scene:
            self.current_scene.update()

    def draw(self, screen):
        if self.current_scene:
            self.current_scene.draw(screen)