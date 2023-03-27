#define N 100
#define FOV 60

uniform vec2 lightPosition;
uniform float lightSize;
uniform float angle;

float terrain(vec2 samplePoint)
{
    float samplePointAlpha = texture(iChannel0, samplePoint).a;
    float sampleStepped = step(0.1, samplePointAlpha);
    float returnValue = 1.0 - sampleStepped;
    return returnValue;
}

void mainImage( out vec4 fragColor, in vec2 fragCoord )
{
    float distanceToLight = length(lightPosition - fragCoord);
    vec2 normalizedFragCoord = fragCoord/iResolution.xy;
    vec2 normalizedLightCoord = lightPosition.xy/iResolution.xy;
    float lightAmount = 1.0;
    vec2 dir = normalizedFragCoord - normalizedLightCoord;
    float thisAngle = atan(dir.y, dir.x);

    // TODO: Fix the angle comparison, angle is is changing somehow
    if(thisAngle < radians(angle)-radians(FOV/2) || thisAngle > radians(angle)+radians(FOV/2))
    {
        // amount of light where it is shadow (0.0 - 1.0)
        lightAmount = 0.0;
    } 
    else 
    {
        for(float i = 0.0; i < N; i++)
        {
            float t = i / N;
            vec2 samplePoint = mix(normalizedFragCoord, normalizedLightCoord, t);
            float shadowAmount = terrain(samplePoint);
            lightAmount *= shadowAmount;
        }
    }
    lightAmount *= 1.0 - smoothstep(0.0, lightSize, distanceToLight);
    vec4 blackColor = vec4(0.0, 0.0, 0.0, 1.0);
    fragColor = mix(blackColor, texture(iChannel1, normalizedFragCoord), lightAmount);
}