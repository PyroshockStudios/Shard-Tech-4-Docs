# NamedNodeMap

## Summary
Represents a collection of an element's attributes, exposing DOM-like attribute manipulation 
methods and C# [DynamicObject](https://learn.microsoft.com/dotnet/api/system.dynamic.dynamicobject) member dispatch with camelCase to kebab-case conversion.

## Remarks
!!! danger
    All calls made within this class <strong>MUST</strong> be performed on the Master Thread. 
    See [Threads.RunLater](../../sdt4.managed.core/threads.md#runlater) on how to safely call this from an asynchronous thread.
    Failure to comply with this can cause catastrophical failures as the engine is not designed for this.

## Definition

**Namespace:** `SDT4.Managed.UI.Rml`  
**Assembly:** `SDT4.Managed.UI.dll`

```csharp
sealed class NamedNodeMap
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔ [DynamicObject](https://learn.microsoft.com/dotnet/api/system.dynamic.dynamicobject) ➔  **NamedNodeMap**
**Implements:**

##### [IDynamicMetaObjectProvider](https://learn.microsoft.com/dotnet/api/system.dynamic.idynamicmetaobjectprovider), [IEnumerable&lt;KeyValuePair&lt;String, RmlVariant&gt;&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public get; Length` | [Int32](https://learn.microsoft.com/dotnet/api/system.int32) | Gets the total number of attributes present on the element. Corresponds to JavaScript <c>element.attributes.length</c>. |
| `public get; set; Item` | [RmlVariant](./rmlvariant.md) | Indexed accessor for attributes by name. |
| `public get; Item` | [KeyValuePair&lt;String, RmlVariant&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.keyvaluepair-2) | Indexed accessor for attributes by zero-based index, mirroring JS array indexing on <c>NamedNodeMap</c>. |



---

## Methods

#### public [KeyValuePair&lt;String, RmlVariant&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.keyvaluepair-2) GetItem([Int32](https://learn.microsoft.com/dotnet/api/system.int32) index)


**Summary:**
Retrieves an attribute pair by its zero-based index.
Corresponds to JavaScript <c>element.attributes.item(index)</c>.

**Parameters:**

- `index` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): The zero-based index of the attribute.


**Returns:**

- [KeyValuePair&lt;String, RmlVariant&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.keyvaluepair-2): A key-value pair of the attribute name and variant value.

---
#### public virtual [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) TryGetMember([GetMemberBinder](https://learn.microsoft.com/dotnet/api/system.dynamic.getmemberbinder) binder, out [Object](https://learn.microsoft.com/dotnet/api/system.object) result)


**Summary:**
Provides dynamic property retrieval, converting PascalCase/camelCase properties into kebab-case attribute names.

**Parameters:**

- `binder` ([GetMemberBinder](https://learn.microsoft.com/dotnet/api/system.dynamic.getmemberbinder)): 

- `result` ([Object](https://learn.microsoft.com/dotnet/api/system.object)): 


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---
#### public virtual [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) TrySetMember([SetMemberBinder](https://learn.microsoft.com/dotnet/api/system.dynamic.setmemberbinder) binder, [Object?](https://learn.microsoft.com/dotnet/api/system.object) value)


**Summary:**
Provides dynamic property assignment, converting PascalCase/camelCase properties into kebab-case attribute names.

**Parameters:**

- `binder` ([SetMemberBinder](https://learn.microsoft.com/dotnet/api/system.dynamic.setmemberbinder)): 

- `value` ([Object?](https://learn.microsoft.com/dotnet/api/system.object)): 


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---
#### public [IEnumerator&lt;KeyValuePair&lt;String, RmlVariant&gt;&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1) GetEnumerator()


**Summary:**
Returns an enumerator that iterates through all attributes on the element.

**Returns:**

- [IEnumerator&lt;KeyValuePair&lt;String, RmlVariant&gt;&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1): 

---
#### public virtual [String](https://learn.microsoft.com/dotnet/api/system.string) ToString()

**Returns:**

- [String](https://learn.microsoft.com/dotnet/api/system.string): 

---


---