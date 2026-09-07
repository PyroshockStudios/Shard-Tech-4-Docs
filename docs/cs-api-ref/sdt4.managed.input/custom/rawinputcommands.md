# RawInputCommands

## Summary
Represents dispatch delegates provided to custom input devices, allowing raw drivers 
to inject button and axis events directly into the engine's central input pipeline.



## Definition

**Namespace:** `SDT4.Managed.Input.Custom`  
**Assembly:** `SDT4.Managed.Input.dll`

```csharp
class RawInputCommands
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔  **RawInputCommands**
**Implements:**

##### [IEquatable&lt;RawInputCommands&gt;](https://learn.microsoft.com/dotnet/api/system.iequatable-1)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `protected get; EqualityContract` | [Type](https://learn.microsoft.com/dotnet/api/system.type) |  |
| `public get; set; PushButtonInput` | [Action&lt;CustomButtonInputEventArgs&gt;](https://learn.microsoft.com/dotnet/api/system.action-1) | A callback delegate used to push a [CustomButtonInputEventArgs](./events/custombuttoninputeventargs.md) into the orchestrator. |
| `public get; set; PushAxisInput` | [Action&lt;CustomAxisInputEventArgs&gt;](https://learn.microsoft.com/dotnet/api/system.action-1) | A callback delegate used to push a [CustomAxisInputEventArgs](./events/customaxisinputeventargs.md) into the orchestrator. |



---

## Methods

#### public virtual [String](https://learn.microsoft.com/dotnet/api/system.string) ToString()

**Returns:**

- [String](https://learn.microsoft.com/dotnet/api/system.string): 

---
#### protected virtual [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) PrintMembers([StringBuilder](https://learn.microsoft.com/dotnet/api/system.text.stringbuilder) builder)

**Parameters:**

- `builder` ([StringBuilder](https://learn.microsoft.com/dotnet/api/system.text.stringbuilder)): 


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---
#### public virtual [Int32](https://learn.microsoft.com/dotnet/api/system.int32) GetHashCode()

**Returns:**

- [Int32](https://learn.microsoft.com/dotnet/api/system.int32): 

---
#### public virtual [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([Object?](https://learn.microsoft.com/dotnet/api/system.object) obj)

**Parameters:**

- `obj` ([Object?](https://learn.microsoft.com/dotnet/api/system.object)): 


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---
#### public virtual [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([RawInputCommands?](./rawinputcommands.md) other)

**Parameters:**

- `other` ([RawInputCommands?](./rawinputcommands.md)): 


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---
#### public virtual [RawInputCommands](./rawinputcommands.md) <Clone>$()

**Returns:**

- [RawInputCommands](./rawinputcommands.md): 

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Deconstruct(out [Action&lt;CustomButtonInputEventArgs&gt;](https://learn.microsoft.com/dotnet/api/system.action-1) PushButtonInput, out [Action&lt;CustomAxisInputEventArgs&gt;](https://learn.microsoft.com/dotnet/api/system.action-1) PushAxisInput)

**Parameters:**

- `PushButtonInput` ([Action&lt;CustomButtonInputEventArgs&gt;](https://learn.microsoft.com/dotnet/api/system.action-1)): 

- `PushAxisInput` ([Action&lt;CustomAxisInputEventArgs&gt;](https://learn.microsoft.com/dotnet/api/system.action-1)): 


---


---