# IResource



## Definition

**Namespace:** `SDT4.Managed.Core.Asset`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
interface IResource
```
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
| `public get; Type` | [AssetType](./assettype.md) |  |
| `public get; Asset` | [AssetID](./assetid.md) |  |
| `public get; ResourceSize` | [Int64](https://learn.microsoft.com/dotnet/api/system.int64) | Size of this resources in both VRAM and RAM in bytes. |
| `public get; ControlBlock` | [IntPtr](https://learn.microsoft.com/dotnet/api/system.intptr) | Immutable native pointer. This will never change as long as the resource stays alive. |
| `public get; ResourceBlock` | [IntPtr](https://learn.microsoft.com/dotnet/api/system.intptr) | Mutable native pointer. This should not change in a standalone build, however during editor states, this may change upon asset modifications or reloads. Prefer using ControlBlock if you must use a native reference. |
| `public get; References` | [Int32](https://learn.microsoft.com/dotnet/api/system.int32) | Returns the number of references to this asset. This cannot be manually counted, as this is tightly managed by the native engine, and the C# script runtime. References are tracked as follows: <ul>Components hold strong references</ul> <ul>Asset dependencies hold strong references (e.g. Materials holding references to Textures)</ul> <ul>IResource references within C#. Note in C#, the reference counting is managed by the garbage collector, meaning that resources held in C# may be kept alive longer than usual.</ul> |


---

## Methods



---