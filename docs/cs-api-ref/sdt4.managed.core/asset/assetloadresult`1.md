# AssetLoadResult&lt;&gt;

## Summary
Represents the result of an asset loading operation, encapsulating an outcome status code and the loaded resource instance if successful.

## Remarks
This struct is immutable and thread-safe for concurrent read access.

## Definition

**Namespace:** `SDT4.Managed.Core.Asset`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
struct AssetLoadResult<>
```
**Implements:**

##### [IEquatable&lt;AssetLoadResult&lt;TResource&gt;&gt;](https://learn.microsoft.com/dotnet/api/system.iequatable-1)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public get; set; ErrorCode` | [AssetErrorCode](./asseterrorcode.md) | The error or status code detailing the outcome of the load attempt. |
| `public get; set; Resource` | TResource | The loaded resource instance, or <see langword="null" /> if the operation failed or produced no resource. |



---

## Methods

#### public virtual [String](https://learn.microsoft.com/dotnet/api/system.string) ToString()

**Returns:**

- [String](https://learn.microsoft.com/dotnet/api/system.string): 

---
#### public virtual [Int32](https://learn.microsoft.com/dotnet/api/system.int32) GetHashCode()

**Returns:**

- [Int32](https://learn.microsoft.com/dotnet/api/system.int32): 

---
#### public virtual [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([Object](https://learn.microsoft.com/dotnet/api/system.object) obj)

**Parameters:**

- `obj` ([Object](https://learn.microsoft.com/dotnet/api/system.object)): 


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([AssetLoadResult&lt;TResource&gt;](./assetloadresult`1.md) other)

**Parameters:**

- `other` ([AssetLoadResult&lt;TResource&gt;](./assetloadresult`1.md)): 


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Deconstruct(out [AssetErrorCode](./asseterrorcode.md) ErrorCode, out TResource Resource)

**Parameters:**

- `ErrorCode` ([AssetErrorCode](./asseterrorcode.md)): 

- `Resource` (TResource): 


---


---