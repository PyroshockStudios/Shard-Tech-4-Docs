# DomTokenList

## Summary
Represents a set of space-separated tokens corresponding to an element's <c>class</c> attribute,
mirroring the JavaScript DOM <c>DOMTokenList</c> interface (<c>element.classList</c>).

## Remarks
!!! danger
    All calls made within this class <strong>MUST</strong> be performed on the Master Thread. 
    See [Threads.RunLater](../../sdt4.managed.core/threads.md#runlater) on how to safely call this from an asynchronous thread.
    Failure to comply with this can cause catastrophical failures as the engine is not designed for this.

## Definition

**Namespace:** `SDT4.Managed.UI.Rml`  
**Assembly:** `SDT4.Managed.UI.dll`

```csharp
struct DomTokenList
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



---

## Methods

#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Toggle([String](https://learn.microsoft.com/dotnet/api/system.string) className, [Nullable&lt;Boolean&gt;](https://learn.microsoft.com/dotnet/api/system.nullable-1) force)


**Summary:**
Adds or removes a class token depending on the specified boolean flag.
Corresponds to JavaScript <c>element.classList.toggle(className, force)</c>.

**Parameters:**

- `className` ([String](https://learn.microsoft.com/dotnet/api/system.string)): The name of the class token to toggle.

- `force` ([Nullable&lt;Boolean&gt;](https://learn.microsoft.com/dotnet/api/system.nullable-1)): If included, when <see langword="true" />, adds the class; if <see langword="false" />, removes the class.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Remove([String](https://learn.microsoft.com/dotnet/api/system.string) className, [String[]](https://learn.microsoft.com/dotnet/api/system.string) rest)


**Summary:**
Removes one or more class tokens from the element.
Corresponds to JavaScript <c>element.classList.remove(...tokens)</c>.

**Parameters:**

- `className` ([String](https://learn.microsoft.com/dotnet/api/system.string)): The first class token to remove.

- `rest` ([String[]](https://learn.microsoft.com/dotnet/api/system.string)): Additional class tokens to remove.


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Remove([IEnumerable&lt;String&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) list)


**Summary:**
Removes a collection of class tokens from the element.

**Parameters:**

- `list` ([IEnumerable&lt;String&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)): An enumerable collection of class tokens to remove.


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Add([String](https://learn.microsoft.com/dotnet/api/system.string) className, [String[]](https://learn.microsoft.com/dotnet/api/system.string) rest)


**Summary:**
Adds one or more class tokens to the element.
Corresponds to JavaScript <c>element.classList.add(...tokens)</c>.

**Parameters:**

- `className` ([String](https://learn.microsoft.com/dotnet/api/system.string)): The first class token to add.

- `rest` ([String[]](https://learn.microsoft.com/dotnet/api/system.string)): Additional class tokens to add.


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Add([IEnumerable&lt;String&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) list)


**Summary:**
Adds a collection of class tokens to the element.

**Parameters:**

- `list` ([IEnumerable&lt;String&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)): An enumerable collection of class tokens to add.


---
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Replace([String](https://learn.microsoft.com/dotnet/api/system.string) oldName, [String](https://learn.microsoft.com/dotnet/api/system.string) newName)


**Summary:**
Replaces an existing class token with a new class token.
Corresponds to JavaScript <c>element.classList.replace(oldToken, newToken)</c>.

**Parameters:**

- `oldName` ([String](https://learn.microsoft.com/dotnet/api/system.string)): The class token to be replaced.

- `newName` ([String](https://learn.microsoft.com/dotnet/api/system.string)): The replacement class token.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Contains([String](https://learn.microsoft.com/dotnet/api/system.string) className)


**Summary:**
Determines whether the element currently has the specified class token.
Corresponds to JavaScript <c>element.classList.contains(className)</c>.

**Parameters:**

- `className` ([String](https://learn.microsoft.com/dotnet/api/system.string)): The class token to search for.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if the class token is present; otherwise, <see langword="false" />.

---


---