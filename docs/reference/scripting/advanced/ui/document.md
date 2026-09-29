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

!!! important
    Unfortunately it's not possible to load documents asynchronously such as with the rest of the Resource management API, so any resources e.g. textures or shaders (planned for the future) may cause a stutter when loaded immediately. For heavy resources, recur to pre-loading them and holding onto the resources in C#.


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