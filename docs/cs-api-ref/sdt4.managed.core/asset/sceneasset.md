# SceneAsset

## Summary




## Definition

**Namespace:** `SDT4.Managed.Core.Asset`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
class SceneAsset
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔ [Resource](./resource.md) ➔  **SceneAsset**
**Implements:**

##### [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable), [IResourceMapping](./iresourcemapping.md)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public static get; ResourceType` | [AssetType](./assettype.md) |  |



---

## Methods

#### public [Scene](../scene.md) CreateScene([String?](https://learn.microsoft.com/dotnet/api/system.string) name)


**Summary:**
Creates a new [Scene](../scene.md) from this asset.

**Remarks:**
!!! danger
    THIS MUST BE CALLED ON THE MASTER THREAD!

**Parameters:**

- `name` ([String?](https://learn.microsoft.com/dotnet/api/system.string)): Optional debug name for the scene


**Returns:**

- [Scene](../scene.md): Returns a valid [Scene](../scene.md)

---


---