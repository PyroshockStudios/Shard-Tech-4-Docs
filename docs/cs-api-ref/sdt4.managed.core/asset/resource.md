# Resource

## Summary




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
| `protected _isDisposed` | [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) |  |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public get; Asset` | [AssetID](./assetid.md) |  |
| `public get; protected set; ControlBlock` | [IntPtr](https://learn.microsoft.com/dotnet/api/system.intptr) |  |
| `protected get; ResourcePtr` | [IntPtr](https://learn.microsoft.com/dotnet/api/system.intptr) | Mutable native pointer. This should not change in a standalone build, however during editor states, this may change upon asset modifications or reloads. |
| `public get; References` | [Int32](https://learn.microsoft.com/dotnet/api/system.int32) | Returns the number of references to this asset. This cannot be manually counted, as this is tightly managed by the native engine, and the C# script runtime. References are tracked as follows: <ul>Components hold strong references</ul> <ul>Asset dependencies hold strong references (e.g. Materials holding references to Textures)</ul> <ul>Resource references within C#. Note in C#, the reference counting is managed by the garbage collector, meaning that resources held in C# may be kept alive longer than usual.</ul> |



---

## Methods

#### protected virtual [Void](https://learn.microsoft.com/dotnet/api/system.void) Dispose([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) disposing)

**Parameters:**

- `disposing` ([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)): 


---
#### protected virtual [Void](https://learn.microsoft.com/dotnet/api/system.void) Finalize()

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Dispose()

---
#### public virtual [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([Object?](https://learn.microsoft.com/dotnet/api/system.object) obj)

**Parameters:**

- `obj` ([Object?](https://learn.microsoft.com/dotnet/api/system.object)): 


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---
#### public virtual [Int32](https://learn.microsoft.com/dotnet/api/system.int32) GetHashCode()

**Returns:**

- [Int32](https://learn.microsoft.com/dotnet/api/system.int32): 

---
#### public virtual [String](https://learn.microsoft.com/dotnet/api/system.string) ToString()

**Returns:**

- [String](https://learn.microsoft.com/dotnet/api/system.string): 

---


---