# RMLClassTokenList

## Summary


## Remarks
!!! danger
    All calls made within this class <strong>MUST</strong> be performed on the Master Thread. 
    See [Threads.RunLater](../../sdt4.managed.core/threads.md#runlater) on how to safely call this from an asynchronous thread.
    Failure to comply with this can cause catastrophical failures as the engine is not designed for this.

## Definition

**Namespace:** `SDT4.Managed.UI.RML`  
**Assembly:** `SDT4.Managed.UI.dll`

```csharp
sealed class RMLClassTokenList
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔  **RMLClassTokenList**
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



---

## Methods

#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Toggle([String](https://learn.microsoft.com/dotnet/api/system.string) className)

**Parameters:**

- `className` ([String](https://learn.microsoft.com/dotnet/api/system.string)): 


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Toggle([String](https://learn.microsoft.com/dotnet/api/system.string) className, [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) enable)

**Parameters:**

- `className` ([String](https://learn.microsoft.com/dotnet/api/system.string)): 

- `enable` ([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)): 


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Remove([String](https://learn.microsoft.com/dotnet/api/system.string) className, [String[]](https://learn.microsoft.com/dotnet/api/system.string) rest)

**Parameters:**

- `className` ([String](https://learn.microsoft.com/dotnet/api/system.string)): 

- `rest` ([String[]](https://learn.microsoft.com/dotnet/api/system.string)): 


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Remove([IEnumerable&lt;String&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) list)

**Parameters:**

- `list` ([IEnumerable&lt;String&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)): 


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Add([String](https://learn.microsoft.com/dotnet/api/system.string) className, [String[]](https://learn.microsoft.com/dotnet/api/system.string) rest)

**Parameters:**

- `className` ([String](https://learn.microsoft.com/dotnet/api/system.string)): 

- `rest` ([String[]](https://learn.microsoft.com/dotnet/api/system.string)): 


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Add([IEnumerable&lt;String&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) list)

**Parameters:**

- `list` ([IEnumerable&lt;String&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)): 


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Replace([String](https://learn.microsoft.com/dotnet/api/system.string) oldName, [String](https://learn.microsoft.com/dotnet/api/system.string) newName)

**Parameters:**

- `oldName` ([String](https://learn.microsoft.com/dotnet/api/system.string)): 

- `newName` ([String](https://learn.microsoft.com/dotnet/api/system.string)): 


---
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Contains([String](https://learn.microsoft.com/dotnet/api/system.string) className)

**Parameters:**

- `className` ([String](https://learn.microsoft.com/dotnet/api/system.string)): 


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---


---