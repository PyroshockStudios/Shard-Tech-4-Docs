# EditorRunContext

## Summary
Contains the editor run data



## Definition

**Namespace:** `SDT4.Managed.Editor`  
**Assembly:** `SDT4.Managed.Editor.dll`

```csharp
struct EditorRunContext
```
**Implements:**

##### 
---

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `public Scene` | [Scene](../sdt4.managed.core/scene.md) | Active scene |
| `public SceneScript` | [SceneScript?](../sdt4.managed.core/script/scenescript.md) | Active scene script. May be null if the scene has no script associated. |
| `public EditorWindow` | [Window](../sdt4.managed.windowing/window.md) | Editor owned window. |
| `public PrimaryViewport` | [ViewportRenderInstance](../sdt4.managed.renderer/xrp/viewportrenderinstance.md) | Editor owned master viewport. |
| `public Viewports` | [IReadOnlyList&lt;ViewportRenderInstance&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1) | Editor owned viewports. Includes master viewport. May change in size. |
| `public SceneRenderer` | [SceneRenderInstance](../sdt4.managed.renderer/xrp/scenerenderinstance.md) | Active scene render instance. |

---


## Properties

| Name | Type | Description |
| --- | --- | --- |

---


## Methods



---