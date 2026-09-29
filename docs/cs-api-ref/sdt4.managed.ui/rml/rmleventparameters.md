# RmlEventParameters

## Summary


## Remarks
!!! danger
    All calls made within this class <strong>MUST</strong> be performed on the Master Thread. 
    See [Threads.RunLater](../../sdt4.managed.core/threads.md#runlater) on how to safely call this from an asynchronous thread.
    Failure to comply with this can cause catastrophical failures as the engine is not designed for this.

## Definition

**Namespace:** `SDT4.Managed.UI.Rml`  
**Assembly:** `SDT4.Managed.UI.dll`

```csharp
struct RmlEventParameters
```
**Implements:**

##### [IReadOnlyDictionary&lt;String, RmlVariant&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlydictionary-2), [IEnumerable&lt;KeyValuePair&lt;String, RmlVariant&gt;&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable), [IReadOnlyCollection&lt;KeyValuePair&lt;String, RmlVariant&gt;&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlycollection-1)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public get; Keys` | [IEnumerable&lt;String&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) |  |
| `public get; Values` | [IEnumerable&lt;RmlVariant&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) |  |
| `public get; Count` | [Int32](https://learn.microsoft.com/dotnet/api/system.int32) |  |
| `public get; Item` | [RmlVariant](./rmlvariant.md) |  |



---

## Methods

#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) ContainsKey([String](https://learn.microsoft.com/dotnet/api/system.string) key)

**Parameters:**

- `key` ([String](https://learn.microsoft.com/dotnet/api/system.string)): 


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) TryGetValue([String](https://learn.microsoft.com/dotnet/api/system.string) key, out [RmlVariant](./rmlvariant.md) value)

**Parameters:**

- `key` ([String](https://learn.microsoft.com/dotnet/api/system.string)): 

- `value` ([RmlVariant](./rmlvariant.md)): 


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---
#### public [IEnumerator&lt;KeyValuePair&lt;String, RmlVariant&gt;&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1) GetEnumerator()

**Returns:**

- [IEnumerator&lt;KeyValuePair&lt;String, RmlVariant&gt;&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1): 

---
#### public virtual [String](https://learn.microsoft.com/dotnet/api/system.string) ToString()

**Returns:**

- [String](https://learn.microsoft.com/dotnet/api/system.string): 

---


---