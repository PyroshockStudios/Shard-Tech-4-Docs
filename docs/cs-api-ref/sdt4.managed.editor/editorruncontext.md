# EditorRunContext

## Summary
Contains the editor run data



## Definition

**Namespace:** `SDT4.Managed.Editor`  
**Assembly:** `SDT4.Managed.Editor.dll`

```csharp
sealed class EditorRunContext
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔  **EditorRunContext**
**Implements:**

##### 
---

## Fields

| Name | Type | Description |
| --- | --- | --- |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public get; Instance` | [AppInstance](../sdt4.managed.core/appinstance.md) | Preloaded application instance. |
| `public get; Scene` | [Scene](../sdt4.managed.core/scene.md) | Active scene |
| `public get; SceneScript` | [SceneScript](../sdt4.managed.core/script/scenescript.md) | Active scene script. May be null if the scene has no script associated. |
| `public get; EditorWindow` | [Window](../sdt4.managed.windowing/window.md) | Editor owned window. |
| `public get; PrimaryViewport` | [ViewportRenderInstance](../sdt4.managed.renderer/xrp/viewportrenderinstance.md) | Editor owned master viewport. |
| `public get; SceneRenderer` | [SceneRenderInstance](../sdt4.managed.renderer/xrp/scenerenderinstance.md) | Active scene render instance. |



---

## Methods



---