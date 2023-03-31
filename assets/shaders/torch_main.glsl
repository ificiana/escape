#version 330 core

uniform vec2 resolution;
uniform vec2 player_pos;
uniform sampler2D tex;
uniform sampler2D shadow_tex;
uniform float ambient_intensity;
uniform float light_intensity;

in vec2 frag_pos;

out vec4 frag_color;

void main() {
    vec4 tex_color = texture(tex, frag_pos);

    // calculate distance between current pixel and player position
    float dist = length(player_pos - frag_pos);

    // calculate light intensity based on distance and ambient intensity
    float light = ambient_intensity + (light_intensity - ambient_intensity) / (1.0 + pow(dist, 2.0));

    // get shadow intensity from shadow texture
    float shadow = texture(shadow_tex, frag_pos).r;

    // combine light and shadow to get final intensity
    float intensity = light * shadow;

    // apply intensity to texture color
    frag_color = tex_color * vec4(intensity, intensity, intensity, 1.0);
}
