# RmlUi Integration in Shard Tech 4

Shard Tech 4 integrates [RmlUi](https://mikke89.github.io/RmlUiDoc) directly into the XRP rendering architecture to provide lightweight, hardware-accelerated user interfaces using HTML/CSS-like workflows (RML and RCSS).

UIs in SDT4 are driven through managed C# scripts, rendering directly into an engine viewport.

## Master Thread Invariant

!!! danger
    Except where explicitly noted (such as asynchronous document loading), all calls to RmlUi APIs **MUST** be performed on the Master Thread. Calling these functions from background worker threads or tasks will trigger native assertion failures or corrupt internal engine memory.

    To execute UI operations safely from asynchronous code, dispatch them back to the main loop using [Threads.RunLater](../../../../cs-api-ref/sdt4.managed.core/threads.md):
    ```csharp
    Threads.RunLater(() => 
    {
        myElement.InnerText = "Updated from task";
    });
    ```

## Basic Script Setup

The typical entry point for managing UI in a scene is a [SceneScript](../../../../cs-api-ref/sdt4.managed.core/script/scenescript.md), or an [ActorScript](../../../../cs-api-ref/sdt4.managed.core/script/actorscript.md). You instantiate the context during `OnBegin`, attach it to the active viewport, and tear it down during `OnEnd`.

```csharp
using SDT4.Managed.Core;
using SDT4.Managed.Core.Asset;
using SDT4.Managed.Core.Script;
using SDT4.Managed.UI.Rml;

namespace Example.UI;

public sealed class SceneHudScript : SceneScript
{
    private RmlContext _uiContext = null!;
    private RmlDocument? _hudDocument;

    private static readonly AssetId HudAsset = new("Master/UI/HUD.rml");

    private SceneHudScript(SceneScriptToken token) : base(token)
    {
    }

    protected override void OnPreBegin()
    {
        // 1. Create a unique context tied to the scene's primary viewport
        _uiContext = RmlContext.CreateContext("GameHUD", /*master viewport*/);

        // 2. Automatically bind input handling from the active engine window
        _uiContext.SubscribeToWindow(/*primary window*/);

        // 3. Load and display our initial UI document
        _hudDocument = _uiContext.LoadDocument(HudAsset);
        _hudDocument?.Show();
    }

    protected override void OnPostEnd()
    {
        // Unsubscribe input listeners before teardown
        _uiContext.UnsubscribeFromWindow(/*primary window*/);

        // Destroy loaded documents
        if (_hudDocument != null)
        {
            _uiContext.DestroyDocument(_hudDocument);
            _hudDocument = null;
        }

        // Explicitly dispose the context
        _uiContext.Dispose();
    }
}

```

## Manual Disposal

!!! important
    [RmlContext](../../../../cs-api-ref/sdt4.managed.ui/rml/rmlcontext.md) owns unmanaged C++ handles and native texture memory. It **must** be disposed manually when shutting down or changing scenes. Relying on garbage collection finalizers can delay resource destruction past the lifetime of the underlying renderer instance.

---