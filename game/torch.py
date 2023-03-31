from arcade.experimental import Shadertoy


class TorchShaderToy(Shadertoy):
    """ShaderToy program to create a torch with shadow effect."""

    def __init__(self):
        super().__init__()

        # Define the uniforms
        self.set_uniform("time", 0.0)
        self.set_uniform("resolution", (0.0, 0.0))
        self.set_uniform("torch_pos", (0.5, 0.5))
        self.set_uniform("torch_radius", 0.2)
        self.set_uniform("light_intensity", 1.0)

        # Set the fragment shader code
        self.set_fragment_shader(
            """
            #define MAX_STEPS 50
            #define MAX_DIST 200.0
            #define EPSILON 0.001

            uniform vec2 resolution;
            uniform float time;
            uniform vec2 torch_pos;
            uniform float torch_radius;
            uniform float light_intensity;

            float scene(vec3 p)
            {
                float d = length(p.xy - torch_pos) - torch_radius;
                return d;
            }

            float trace(vec3 origin, vec3 direction)
            {
                float total_dist = 0.0;
                for(int i = 0; i < MAX_STEPS; i++)
                {
                    vec3 p = origin + total_dist * direction;
                    float d = scene(p);
                    total_dist += d;
                    if(d < EPSILON || total_dist > MAX_DIST)
                        break;
                }
                return total_dist;
            }

            vec3 calcNormal(vec3 p)
            {
                vec2 offset = vec2(0.001, 0.0);
                float d1 = scene(p - offset.xyy);
                float d2 = scene(p + offset.xyy);
                float d3 = scene(p - offset.yxy);
                float d4 = scene(p + offset.yxy);
                float d5 = scene(p - offset.yyx);
                float d6 = scene(p + offset.yyx);
                return normalize(vec3(d1 - d2, d3 - d4, d5 - d6));
            }

            vec3 calcLight(vec3 p, vec3 n, vec3 dir)
            {
                vec3 l = normalize(vec3(0.0, 0.0, 1.0));
                float intensity = max(dot(n, l), 0.0);
                vec3 color = vec3(1.0, 0.5, 0.2) * intensity * light_intensity;

                // Calculate the shadow factor
                vec3 shadow_dir = normalize(l + dir);
                float dist_to_light = trace(p + n * EPSILON, shadow_dir);
                float shadow = dist_to_light > length(l) ? 1.0 : 0.5;

                return color * shadow;
            }

            void mainImage(out vec4 fragColor, in vec2 fragCoord)
            {
                vec2 uv = (fragCoord.xy / resolution.xy)
            * 2.0 - 1.0;
            uv.x *= resolution.x / resolution.y;

            // Camera position and direction
            vec3 ro = vec3(0.0, 0.0, -3.0);
            vec3 rd = normalize(vec3(uv, 1.0));

            // Trace the ray and get the distance to the closest object
            float dist = trace(ro, rd);

            // Calculate the intersection point
            vec3 p = ro + rd * dist;

            // Calculate the surface normal at the intersection point
            vec3 n = calcNormal(p);

            // Calculate the light color and shadow factor
            vec3 light_color = calcLight(p, n, rd);

            // Combine the light color and background color
            vec3 bg_color = vec3(0.1, 0.1, 0.2);
            vec3 color = mix(bg_color, light_color, light_intensity);

            // Output the final color
            fragColor = vec4(color, 1.0);
        }
    """
        )


def on_update(self, delta_time):
    # Update the time uniform
    self.set_uniform("time", self.time)


def set_torch_pos(self, x, y):
    # Set the torch position uniform
    self.set_uniform("torch_pos", (x, y))


def set_torch_radius(self, radius):
    # Set the torch radius uniform
    self.set_uniform("torch_radius", radius)


def set_light_intensity(self, intensity):
    # Set the light intensity uniform
    self.set_uniform("light_intensity", intensity)
