# Debug Hooks

To attach the debug overlay, you can attach a hook.

```csharp
using SDT4.Managed.UI.Rml.Debugging;

...
// Attach debugger overlay to our viewport (Must be associated with a window!)
if (!RmlDebugHook.IsActive)
{
    RmlDebugHook.AttachHook(masterViewport);
}

```