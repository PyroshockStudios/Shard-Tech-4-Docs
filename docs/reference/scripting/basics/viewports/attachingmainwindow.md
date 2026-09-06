# Attaching the Primary Window

When rendering the scene, we must set up our viewport to allow the user to see what's happening!

This is where Shard Tech 4's steeper learning curve hits, however it also provides very powerful features, such as rendering to textures, multi-window split screen and more!

## Getting the swap chain render canvas

A game renders to a window via the *swap chain*, which is a set of at least 2 buffers, where the *back buffer* is where the game renders, and the *front buffer* is what the window *presents* to the user. This swapping is performed automatically in the renderer backend, and therefore a single canvas is necessary.

```csharp
using SDT4.Managed.Core;
using SDT4.Managed.Core.Capabilities;
// For the render canvas
using SDT4.Managed.Renderer; 
using SDT4.Managed.Renderer.Graphics;
// For the window
using SDT4.Managed.Windowing; 

// ...
// remember our app instance!
AppInstance instance = /*...*/;
// We must query the IWindowingCapability interface, 
// which is available in non-headless client builds
if (!instance.TryGetCapability<IWindowingCapability>(out var windowing)) 
{
    throw new NotSupportedException("Windowing is not supported in this build.");
}
// WindowPlatform is the implementor for the IWindowingCapability 
var windowPlatform = (WindowPlatform)windowing;
Window primaryWindow = windowPlatform.PrimaryWindow;

// Now lets get the renderer
if (!instance.TryGetCapability<IRenderingCapability>(out var renderer)) 
{
    throw new NotSupportedException("Rendering is not supported in this build.");
}
// RendererPlatform is the implementor for the IRenderingCapability 
var rendererPlatform = (RendererPlatform)renderer;
// Must be called on the master thread!
RenderCanvas primaryCanvas = rendererPlatform.CreateWindowRenderCanvas(window);

```

Whew! That was step 1, now that we have our render canvas, we can create a SceneRenderInstance and a ViewportRenderInstance 
to attach our newly acquired RenderCanvas.

## Rendering to the canvas

To render to our render canvas, we can either render with custom [Render Effects](../../advanced/renderer/xrpframegraph.md), or 
use the built-in high performance "eXtreme Render Pipeline (XRP)". The Shard Tech 4 XRP contains all the rendering features
related to components in the scene, and allows seamless integration of rendering effects.

```csharp
using SDT4.Managed.Renderer.XRP; // eXtreme Render pipeline
// ...
Scene scene = /*...*/; // get our active scene!
SceneRenderInstance sceneRenderer = rendererPlatform.CreateSceneRenderer(scene);
// Define a unique name, standard convention is "master" for the primary viewport.
ViewportRenderInstance viewportRenderer = sceneRenderer.CreateViewportRenderer("master", primaryCanvas);
// Make sure to use FramebufferSize instead of Size due to DPI awareness!
viewportRenderer.SetViewport(extent: window.FramebufferSize);
// We can use the CameraComponent from an actor to render our canvas! 
Actor cameraActor = /*...*/;
viewportRenderer.SetCameraActor(cameraActor);
// Our scene is now rendered and can be viewed from the perspective of the camera!

```

!!! danger
    All operations performed to SDT4.Managed.Renderer.XRP MUST be performed on the master thread!

## Disposing the canvas

The renderer objects may be disposed when finished using, however when disposing the [Scene](../../../../cs-api-ref/sdt4.managed.core/scene.md),
all the renderer objects related to the scene are automatically disposed. It is still recommended however to manually dispose them.

```csharp
Scene scene = /*...*/; 
SceneRenderInstance sceneRenderer = /*...*/;
ViewportRenderInstance viewportRenderer = /*...*/;
RenderCanvas primaryCanvas = /*...*/;

// Cleanup render objects
viewportRenderer.Dispose();
sceneRenderer.Dispose();
primaryCanvas.Dispose();

// Cleanup scene
scene.Stop();
scene.Dispose();

```

## Window resizing

As you may have noticed, since we manually define the viewport size and the render canvas is created from the window.
Once the window has been resized, the render canvas is outdated, meaning rendering may cause artefacts.

!!! bug
    In some cases due to backend implementations and operating systems, the graphics device **may even crash** 
    if the render canvas is not immediately recreated upon window resize! Therefore **NEVER** assume that 
    it is safe to continue rendering on an outdated render canvas!

The easiest solution is to update the render canvas is to use a Window resize callback

```csharp
// For window input
using SDT4.Managed.Input; // for Window.GetInput() or Window.Input (.NET 10+)
// ...
Window window = /*...*/;
RendererPlatform rendererPlatform = /*...*/;
ViewportRenderInstance viewportRenderer = /*...*/;
RenderCanvas primaryCanvas = /*...*/;

window.GetInput().OnResize += e => 
{ 
    RenderCanvas oldCanvas = primaryCanvas;
    primaryCanvas = rendererPlatform.CreateWindowRenderCanvas(window);
    viewportRenderer.RenderCanvas = primaryCanvas;
    oldCanvas.Dispose(); // release the old canvas
    // update the viewport!
    viewportRenderer.SetViewport(extent: window.FramebufferSize);
};

```