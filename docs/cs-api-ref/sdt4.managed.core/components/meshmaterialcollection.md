# MeshMaterialCollection

## Summary
Provides access to the collection of material assets assigned to a [Mesh3DComponent](./mesh3dcomponent.md).

## Remarks
!!! danger
    All calls made within this class <strong>MUST</strong> be performed on the Master Thread. 
    See [Threads.RunLater](../threads.md#runlater) on how to safely call this from an asynchronous thread.
    Failure to comply with this can cause catastrophical failures as the engine is not designed for this.

## Definition

**Namespace:** `SDT4.Managed.Core.Components`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
struct MeshMaterialCollection
```
**Implements:**

##### [IList&lt;MaterialAsset&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1), [ICollection&lt;MaterialAsset&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1), [IEnumerable&lt;MaterialAsset&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public get; Count` | [Int32](https://learn.microsoft.com/dotnet/api/system.int32) | Gets the total number of material slots available on the owner mesh component. |
| `public get; IsReadOnly` | [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) | Gets a value indicating whether this collection is read-only. Always returns <see langword="false" /> as existing elements can be reassigned. |
| `public get; set; Item` | [MaterialAsset?](../asset/materialasset.md) | Gets or sets the material asset assigned to the specified slot index. |



---

## Methods

#### public [IEnumerator&lt;MaterialAsset&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1) GetEnumerator()


**Summary:**
Returns an enumerator that iterates through the collection of material assets.

**Returns:**

- [IEnumerator&lt;MaterialAsset&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1): An enumerator for the collection.

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Add([MaterialAsset?](../asset/materialasset.md) item)


**Summary:**
Throws [NotSupportedException](https://learn.microsoft.com/dotnet/api/system.notsupportedexception) because the number of material slots cannot be dynamically increased.

**Parameters:**

- `item` ([MaterialAsset?](../asset/materialasset.md)): The material asset to add.


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Clear()


**Summary:**
Throws [NotSupportedException](https://learn.microsoft.com/dotnet/api/system.notsupportedexception) because the collection size is fixed to the mesh's material slot count.

---
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Remove([MaterialAsset?](../asset/materialasset.md) item)


**Summary:**
Throws [NotSupportedException](https://learn.microsoft.com/dotnet/api/system.notsupportedexception) because the collection size is fixed to the mesh's material slot count.

**Parameters:**

- `item` ([MaterialAsset?](../asset/materialasset.md)): The material asset to remove.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): Never returns a value.

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Insert([Int32](https://learn.microsoft.com/dotnet/api/system.int32) index, [MaterialAsset?](../asset/materialasset.md) item)


**Summary:**
Throws [NotSupportedException](https://learn.microsoft.com/dotnet/api/system.notsupportedexception) because elements cannot be inserted into the fixed-size slot layout.

**Parameters:**

- `index` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): The zero-based index at which to insert.

- `item` ([MaterialAsset?](../asset/materialasset.md)): The material asset to insert.


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) RemoveAt([Int32](https://learn.microsoft.com/dotnet/api/system.int32) index)


**Summary:**
Throws [NotSupportedException](https://learn.microsoft.com/dotnet/api/system.notsupportedexception) because elements cannot be removed from the fixed-size slot layout.

**Parameters:**

- `index` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): The zero-based index of the element to remove.


---
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Contains([MaterialAsset?](../asset/materialasset.md) item)


**Summary:**
Determines whether the collection contains a specific material asset.

**Parameters:**

- `item` ([MaterialAsset?](../asset/materialasset.md)): The material asset to locate in the collection.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if `item` is found; otherwise, <see langword="false" />.

---
#### public [Int32](https://learn.microsoft.com/dotnet/api/system.int32) IndexOf([MaterialAsset?](../asset/materialasset.md) item)


**Summary:**
Determines the index of a specific material asset in the collection.

**Parameters:**

- `item` ([MaterialAsset?](../asset/materialasset.md)): The material asset to locate.


**Returns:**

- [Int32](https://learn.microsoft.com/dotnet/api/system.int32): The zero-based index of the first occurrence if found; otherwise, <c>-1</c>.

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) CopyTo([MaterialAsset[]](../asset/materialasset.md) array, [Int32](https://learn.microsoft.com/dotnet/api/system.int32) arrayIndex)


**Summary:**
Copies the material assets of the collection to an array, starting at a particular array index.

**Parameters:**

- `array` ([MaterialAsset[]](../asset/materialasset.md)): The one-dimensional array that is the destination of the elements copied from the collection.

- `arrayIndex` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): The zero-based index in `array` at which copying begins.


---


---