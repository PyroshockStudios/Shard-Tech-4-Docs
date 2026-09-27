
# File 3: `loading-documents.md`

# Loading Documents

Documents are loaded via [AssetId](../../../../cs-api-ref/sdt4.managed.core/asset/assetid.md) paths pointing to `.rml` files. Every loaded document is represented by an [RmlDocument](../../../../cs-api-ref/sdt4.managed.ui/rml/rmldocument.md) instance, which inherits from [RmlElement](../../../../cs-api-ref/sdt4.managed.ui/rml/rmlelement.md).

## Synchronous Loading

Synchronous loading parses and builds the DOM immediately. It must be called on the Master Thread:

```csharp
using SDT4.Managed.Core.Asset;
using SDT4.Managed.UI.Rml;

AssetId menuAsset = new("Master/UI/Menus/MainMenu.rml");
RmlDocument? menuDoc = uiContext.LoadDocument(menuAsset);

if (menuDoc != null)
{
    // Documents are hidden by default when loaded
    menuDoc.Show();
}

```

## Asynchronous Loading

Large RML hierarchies with multiple nested style sheets can be loaded on a background task without causing framerate hitches:

```csharp
using System.Threading.Tasks;
using SDT4.Managed.Core;
using SDT4.Managed.Core.Asset;
using SDT4.Managed.UI.Rml;

public async Task LoadGameMenuAsync(RmlContext context, AssetId assetPath)
{
    // Thread-safe async load
    RmlDocument? doc = await context.LoadDocumentAsync(assetPath);

    // Manipulate DOM elements on the Master Thread
    Threads.RunLater(() =>
    {
        if (doc != null)
        {
            doc.Show();
            doc.PullToFront();
        }
    });
}

```

## Visibility and Z-Ordering

[RmlDocument](../../../../cs-api-ref/sdt4.managed.ui/rml/rmldocument.md) exposes methods to control visibility and layering against sibling documents within the same context:

```csharp
// Display document
doc.Show();

// Hide document (keeps DOM state in memory without rendering)
doc.Hide();

// Bring to the top of the context render stack
doc.PullToFront();

// Send to the bottom
doc.PushToBack();

// Read or change document window title
string windowTitle = doc.Title;
doc.Title = "Pause Menu";

```

## Style Hot-Reloading

You can reload RCSS styles on the fly without reloading the entire document structure or losing state:

```csharp
// Re-parses referenced RCSS sheets and updates styles
doc.ReloadRcss();

```

## Document Destruction

Documents are destroyed through the parent [RmlContext](../../../../cs-api-ref/sdt4.managed.ui/rml/rmlcontext.md). Destroying a document unloads its native resources and disposes all child elements.

```csharp
uiContext.DestroyDocument(doc);

```

!!! danger
    Do not invoke DOM operations or properties on an [RmlDocument](../../../../cs-api-ref/sdt4.managed.ui/rml/rmldocument.md) or its children after passing it to `DestroyDocument()`. Doing so throws an `ObjectDisposedException`.