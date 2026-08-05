# Editor viewport vs window

The editor window's render canvas is owned by the GUI, and is thus not accessible. Attempting to create a render canvas for this window will result in an *InvalidOperationException*.

Instead, the enabled viewport is the existing [ViewportRenderInstance](../../../../cs-api-ref/sdt4.managed.renderer/xrp/viewportrenderinstance.md) provided in the entry and exit. This cannot be disposed as it is owned by the editor.

```csharp
using SDT4.Managed.Core;

static class GameEditor 
{
    static void OnEditorStart(EditorRunContext editorRunContext) 
    {
        // After the runtime stops, the editor camera actor is 
        // automatically restored, meaning no manual cleanup is needed. 
        editorRunContext.ViewportRenderInstance.SetCameraActor(...);
    }
}

```