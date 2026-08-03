# Editor viewport vs window

The editor window's render canvas is owned by the GUI, and is thus not accessible. Attempting to create a render canvas for this window will result in an *InvalidOperationException*.

Instead, the enabled viewport is the existing [ViewportRenderInstance](../../../../cs-api-ref/sdt4.managed.renderer/xrp/viewportrenderinstance.md) provided in the entry and exit. This cannot be disposed as it is owned by the editor.

## Additional viewports

The editor may display multiple viewports, and they can be queried in the Viewports field. Once a viewport is closed, it is automatically destroyed and cannot be accessed anymore. It is important to **NOT** rely on them being alive for the duration of the editor.

```csharp
using SDT4.Managed.Core;
using SDT4.Managed.Debugging;
using SDT4.Managed.Editor;
static class GameEditor 
{
    static void OnEditorStart(EditorRunContext editorRunContext) 
    {
        if (editorRunContext.Viewports.Length > 1) 
        {
            DebugConsole.Print("Second viewport is available, attaching optional debug view...");
            // ...
        } 
    }
}

```