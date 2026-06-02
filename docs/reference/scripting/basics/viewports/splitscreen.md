# Split Screen

Split screen is very versatile due to the render canvas system. 
There are two ways of implementing split-screen:

1. Render to seperate windows
2. Render in a standard "split-screen" fashion within 1 window.

We will be looking at the second implementation, as it is the easiest to implement.

## Creating a second viewport render instance

Creating another viewport render instance is very straight forward, and it is the same as we've seen before.
The only difference is we must ensure that our viewports do not overlap with each other, and render to their respective regions.

```csharp
using SDT4.Managed.Core;
using SDT4.Managed.Renderer; 
using SDT4.Managed.Renderer.Graphics;
using SDT4.Managed.Renderer.XRP;
using SDT4.Managed.Windowing;

// ...
// recall our render objects
Scene scene = /*...*/; 
Actor player1 = /*...*/;
Window window = /*...*/; 
RenderCanvas windowCanvas = /*...*/
SceneRenderInstance sceneRenderer = /*...*/;
ViewportRenderInstance viewportRendererPlayer1 = /*...*/;

// Now our new player 2 render objects

Actor player2 = /*...*/;

ViewportRenderInstance viewportRendererPlayer2 = sceneRenderer.CreateViewportRenderer("player2", windowCanvas);
// attach our camera
viewportRendererPlayer2.SetCameraActor(player2);

// Let's set up a vertical split-screen
Vector2i region = window.FramebufferSize;
region.x /= 2;

Vector2i offsetP1 = Vector2i.Zero;
Vector2i offsetP2 = new Vector2i(region.x, 0);

// and set our viewports!
viewportRendererPlayer1.SetViewport(extent: region, offset: offsetP1);
viewportRendererPlayer2.SetViewport(extent: region, offset: offsetP2);
```

And that was it, that's how simple it is to implement split screen!

Now just remember to dispose the additional viewport.