# The RmlContext

An [RmlContext](../../../../cs-api-ref/sdt4.managed.ui/rml/rmlcontext.md) represents an independent UI surface containing its own DOM tree, styling context, loaded documents, data models, and input state.

## Context Creation and Viewport Binding

Contexts are instantiated through the static `CreateContext` factory method. Every context requires a unique identifying string name and an initial viewport target.

```csharp
using SDT4.Managed.UI.Rml;

// Create context attached to main viewport
RmlContext uiContext = RmlContext.CreateContext("MasterContext", masterViewport);

// Re-route context output to a different viewport dynamically
uiContext.AttachToViewport(secondaryViewport);

```

## Input Processing

User interactions must be delivered to the context for focus, hover states, scrolling, and clicks to function.

### Automatic Subscription

For game windows, use `SubscribeToWindow` to automatically listen to keyboard, mouse, and text inputs:

```csharp
uiContext.SubscribeToWindow(primaryWindow);

// When tearing down or disabling UI input
uiContext.UnsubscribeFromWindow(primaryWindow);

```

### Manual Input Dispatch

If you are developing custom editor tools, overlays, or handling inputs manually (e.g. a virtual screen):

```csharp
// Mouse movement (coordinates are relative to the viewport's top-left corner)
uiContext.ProcessMouseMove(cursorX, cursorY, keyModifierState: 0);

// Mouse buttons (0 = Left, 1 = Right, 2 = Middle), Mirrors SDT4.Managed.Input
uiContext.ProcessMouseButtonDown(0, keyModifierState: 0);
uiContext.ProcessMouseButtonUp(0, keyModifierState: 0);

// Mouse scroll wheel (positive is down/right)
uiContext.ProcessMouseWheel(new Vector2d(0, 1.0), keyModifierState: 0);

// Keyboard input, Mirrors SDT4.Managed.Input
uiContext.ProcessKeyDown(keyIdentifier: 0x41, keyModifierState: 0);
uiContext.ProcessKeyUp(keyIdentifier: 0x41, keyModifierState: 0);

// Text typing input (Unicode or ASCII)
uiContext.ProcessTextInput("PlayerName");

// Cursor leaving client area (clears hover states)
uiContext.ProcessMouseLeave();

```

## DPI Scaling

The `Dpi` property controls the ratio between density-independent points (`dp`) and physical pixels (`px`):

```csharp
// Scale the interface up by 150% for high-DPI displays
uiContext.Dpi = 1.5f;

```