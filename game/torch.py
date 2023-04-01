from arcade.experimental import Shadertoy
from pyglet.math import Vec2

from game.config import SCREEN_WIDTH, SCREEN_HEIGHT


class Torch(Shadertoy):
    """ShaderToy program to create a torch with shadow effect."""

    def __init__(self, size, main_source):
        # super().__init__(size, main_source)
        print("Torch init")
        print(size)
        print(main_source)
        self.shadertoy = None
        # self.channel0 = None
        # self.channel1 = None
        self.load_shader(size, main_source)
        print("Torch init")

    def load_shader(self, size, main_source):
        shader_file_path = main_source
        window_size = size
        self.shadertoy = Shadertoy.create_from_file(window_size, shader_file_path)
        # self.channel0 = self.shadertoy.ctx.framebuffer(
        #     color_attachments=[self.shadertoy.ctx.texture(window_size, components=4)]
        # )
        # self.channel1 = self.shadertoy.ctx.framebuffer(
        #     color_attachments=[self.shadertoy.ctx.texture(window_size, components=4)]
        # )
        # self.shadertoy.channel_0 = self.channel0.color_attachments[0]
        # self.shadertoy.channel_1 = self.channel1.color_attachments[0]
        print("Torch load_shader")

    def draw(self, angle):
        print(angle)

        # self.channel0.use()
        # self.channel0.clear()
        #
        # self.channel1.use()
        # self.channel1.clear()
        # # Draw everything that can be hidden in shadows bur does not cast shadow
        # # self.walls.draw()
        #
        # # self.use()
        # # self.clear()
        self.shadertoy.program["lightPosition"] = Vec2(
            SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2
        )
        self.shadertoy.program["lightSize"] = 300
        self.shadertoy.program["angle"] = angle
        self.shadertoy.render()
