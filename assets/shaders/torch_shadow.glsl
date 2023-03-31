#version 330 core

uniform vec2 resolution;
uniform vec2 player_pos;
uniform sampler2D tex;
uniform float light_radius;
uniform float falloff;

in vec2 frag_pos;

out vec4 frag_color;

void main() {
    float dist = length(player_pos - frag_pos);
    float alpha = 1.0 - smoothstep(light_radius, light_radius * falloff, dist);

    frag_color = vec4(0.0, 0.0, 0.0, alpha);
}
