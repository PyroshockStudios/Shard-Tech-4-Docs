# Resource

## Summary
Serves as the abstract base class for engine resources backed by native memory and control blocks.



## Definition

**Namespace:** `SDT4.Managed.Core.Asset`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
abstract class Resource
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔  **Resource**
**Implements:**

##### [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `protected _isDisposed` | [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) | Indicates whether the resource has been disposed. |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public get; Asset` | [AssetId](./assetid.md) | Gets the [AssetId](./assetid.md) associated with this resource. |
| `public get; protected set; ControlBlock` | [IntPtr](https://learn.microsoft.com/dotnet/api/system.intptr) | Gets the immutable pointer to the native control block managing this resource's lifetime. |
| `protected get; ResourcePtr` | [IntPtr](https://learn.microsoft.com/dotnet/api/system.intptr) | Gets the pointer to the underlying native resource instance. |
| `public get; References` | [Int32](https://learn.microsoft.com/dotnet/api/system.int32) | Gets the total number of active references to this asset maintained across native engine systems and the managed runtime. |


##### `ResourcePtr` Remarks
This pointer remains stable in standalone builds, but can change during editor sessions when assets are modified or reloaded.


---

## Methods

#### protected [Void](https://learn.microsoft.com/dotnet/api/system.void) Dispose([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) disposing)


**Summary:**
Releases the unmanaged resources used by the [Resource](./resource.md) and optionally releases managed resources.

**Parameters:**

- `disposing` ([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)): <see langword="true" /> to release both managed and unmanaged resources; <see langword="false" /> to release only unmanaged resources.


---
#### protected virtual [Void](https://learn.microsoft.com/dotnet/api/system.void) Finalize()

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Dispose()


**Summary:**
Releases all resources held by the [Resource](./resource.md) instance.

---
#### public virtual [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([Object?](https://learn.microsoft.com/dotnet/api/system.object) obj)


**Summary:**
Determines whether the specified object is equal to the current resource based on their native control blocks.

**Parameters:**

- `obj` ([Object?](https://learn.microsoft.com/dotnet/api/system.object)): The object to compare with the current instance.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if the specified object is a [Resource](./resource.md) and shares the same native control block; otherwise, <see langword="false" />.

---
#### public virtual [Int32](https://learn.microsoft.com/dotnet/api/system.int32) GetHashCode()


**Summary:**
Serves as the default hash function based on the native control block handle.

**Returns:**

- [Int32](https://learn.microsoft.com/dotnet/api/system.int32): A hash code for the current resource.

---
#### public virtual [String](https://learn.microsoft.com/dotnet/api/system.string) ToString()


**Summary:**
Returns a string describing the resource, including its control block address, asset identifier, and native type.

**Returns:**

- [String](https://learn.microsoft.com/dotnet/api/system.string): A formatted string representing the resource state.

---


---