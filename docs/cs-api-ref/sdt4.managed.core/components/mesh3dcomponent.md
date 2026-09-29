# Mesh3DComponent

## Summary
Represents a 3D mesh component attached to an actor for rendering geometry.

## Remarks
!!! danger
    All calls made within this class <strong>MUST</strong> be performed on the Master Thread. 
    See [Threads.RunLater](../threads.md#runlater) on how to safely call this from an asynchronous thread.
    Failure to comply with this can cause catastrophical failures as the engine is not designed for this.

## Definition

**Namespace:** `SDT4.Managed.Core.Components`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
struct Mesh3DComponent
```
**Implements:**

##### [IActorComponent](./iactorcomponent.md)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public get; set; Owner` | [ActorHandle](../actorhandle.md) |  |
| `public static get; ComponentId` | [Guid](https://learn.microsoft.com/dotnet/api/system.guid) | The unique identity of [Mesh3DComponent](./mesh3dcomponent.md). |
| `public get; set; Model` | [ModelAsset?](../asset/modelasset.md) | Gets or sets the 3D model asset rendered by this component. |
| `public get; set; CastShadows` | [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) | Gets or sets a value indicating whether this mesh casts shadows. |
| `public get; set; RenderMask` | [Bitmask&lt;UInt16&gt;](../utility/bitmask`1.md) | Gets or sets the bitmask controlling the render passes or layers this mesh belongs to. |
| `public get; set; OverrideLod` | [Nullable&lt;Int32&gt;](https://learn.microsoft.com/dotnet/api/system.nullable-1) | Gets or sets the forced level of detail (LOD) index for this mesh, or <see langword="null" /> to rely on automatic LOD selection. |
| `public get; Materials` | [MeshMaterialCollection](./meshmaterialcollection.md) | Gets the collection providing access and assignment to this mesh's materials. |



---

## Methods

#### public virtual [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([Object?](https://learn.microsoft.com/dotnet/api/system.object) obj)


**Summary:**
Determines whether the specified object is equal to the current component.

**Parameters:**

- `obj` ([Object?](https://learn.microsoft.com/dotnet/api/system.object)): The object to compare with the current component.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if the specified object is equivalent to this component; otherwise, <see langword="false" />.

---
#### public virtual [Int32](https://learn.microsoft.com/dotnet/api/system.int32) GetHashCode()


**Summary:**
Returns the hash code for this component.

**Returns:**

- [Int32](https://learn.microsoft.com/dotnet/api/system.int32): A 32-bit signed integer hash code.

---
#### public virtual [String](https://learn.microsoft.com/dotnet/api/system.string) ToString()


**Summary:**
Returns a string representation of the component.

**Returns:**

- [String](https://learn.microsoft.com/dotnet/api/system.string): A string representing the component instance.

---


---