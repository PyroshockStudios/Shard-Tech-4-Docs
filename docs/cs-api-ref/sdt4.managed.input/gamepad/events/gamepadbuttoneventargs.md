# GamepadButtonEventArgs

## Summary
Provides data for gamepad button press, release, and emulated repeat events.



## Definition

**Namespace:** `SDT4.Managed.Input.Gamepad.Events`  
**Assembly:** `SDT4.Managed.Input.dll`

```csharp
struct GamepadButtonEventArgs
```
**Implements:**

##### [IEquatable&lt;GamepadButtonEventArgs&gt;](https://learn.microsoft.com/dotnet/api/system.iequatable-1)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public get; set; Sender` | [Object?](https://learn.microsoft.com/dotnet/api/system.object) | The source object that dispatched the event, or <see langword="null" />. |
| `public get; set; DeviceId` | [GamepadIdentifier](../gamepadidentifier.md) | The identifier of the gamepad that generated the event. |
| `public get; set; Button` | [GamepadButton](../gamepadbutton.md) | The gamepad button that changed state or repeated. |
| `public get; set; IsRepeating` | [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) | Indicates whether this event is an emulated repeat. |



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
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([GamepadButtonEventArgs](./gamepadbuttoneventargs.md) other)

**Parameters:**

- `other` ([GamepadButtonEventArgs](./gamepadbuttoneventargs.md)): 


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Deconstruct(out [Object?](https://learn.microsoft.com/dotnet/api/system.object) Sender, out [GamepadIdentifier](../gamepadidentifier.md) DeviceId, out [GamepadButton](../gamepadbutton.md) Button, out [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) IsRepeating)

**Parameters:**

- `Sender` ([Object?](https://learn.microsoft.com/dotnet/api/system.object)): 

- `DeviceId` ([GamepadIdentifier](../gamepadidentifier.md)): 

- `Button` ([GamepadButton](../gamepadbutton.md)): 

- `IsRepeating` ([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)): 


---


---