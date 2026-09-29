# VScriptDebugHook

## Summary
A reserved class for visual scripts.

## Remarks
!!! warning
    Do not use this attribute, it is not intended to be used on hand written methods, and is reserved for visual scripts.

## Definition

**Namespace:** `SDT4.Managed.Core.VScript.Debugging`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
static class VScriptDebugHook
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔  **VScriptDebugHook**
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
| `public static get; protected static set; IsDebugHookActive` | [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) |  |
| `public static get; CurrentNodeId` | [UInt64](https://learn.microsoft.com/dotnet/api/system.uint64) |  |



---

## Methods

#### public static [Void](https://learn.microsoft.com/dotnet/api/system.void) ResetState()

---
#### public static [Void](https://learn.microsoft.com/dotnet/api/system.void) OpSubroutine([ScriptGeneratedAttribute](../../attributes/scriptgeneratedattribute.md) vscriptAttr, [String](https://learn.microsoft.com/dotnet/api/system.string) memberName)

**Parameters:**

- `vscriptAttr` ([ScriptGeneratedAttribute](../../attributes/scriptgeneratedattribute.md)): 

- `memberName` ([String](https://learn.microsoft.com/dotnet/api/system.string)): 


---
#### public static [Void](https://learn.microsoft.com/dotnet/api/system.void) OpUnwindSubroutine()

---
#### public static [Void](https://learn.microsoft.com/dotnet/api/system.void) OpNode([UInt64](https://learn.microsoft.com/dotnet/api/system.uint64) nodeId)

**Parameters:**

- `nodeId` ([UInt64](https://learn.microsoft.com/dotnet/api/system.uint64)): 


---
#### public static [Void](https://learn.microsoft.com/dotnet/api/system.void) OpSetPinVal([UInt64](https://learn.microsoft.com/dotnet/api/system.uint64) nodeId, [String](https://learn.microsoft.com/dotnet/api/system.string) pinKey, [Func&lt;Object&gt;](https://learn.microsoft.com/dotnet/api/system.func-1) valueCallback)

**Parameters:**

- `nodeId` ([UInt64](https://learn.microsoft.com/dotnet/api/system.uint64)): 

- `pinKey` ([String](https://learn.microsoft.com/dotnet/api/system.string)): 

- `valueCallback` ([Func&lt;Object&gt;](https://learn.microsoft.com/dotnet/api/system.func-1)): 


---


---