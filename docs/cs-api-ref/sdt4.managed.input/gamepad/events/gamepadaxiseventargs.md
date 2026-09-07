# GamepadAxisEventArgs

## Summary
Provides data for gamepad analog axis movement events, supplying both calibrated and raw values.



## Definition

**Namespace:** `SDT4.Managed.Input.Gamepad.Events`  
**Assembly:** `SDT4.Managed.Input.dll`

```csharp
struct GamepadAxisEventArgs
```
**Implements:**

##### [IEquatable&lt;GamepadAxisEventArgs&gt;](https://learn.microsoft.com/dotnet/api/system.iequatable-1)
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
| `public get; set; Axis` | [GamepadAxis](../gamepadaxis.md) | The specific analog axis that changed value. |
| `public get; set; Value` | [Double](https://learn.microsoft.com/dotnet/api/system.double) | The post-processed axis value after applying inner and outer deadzone transformations. |
| `public get; set; RawValue` | [Double](https://learn.microsoft.com/dotnet/api/system.double) | The unfiltered, raw hardware axis value reported by the native backend. |



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
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([GamepadAxisEventArgs](./gamepadaxiseventargs.md) other)

**Parameters:**

- `other` ([GamepadAxisEventArgs](./gamepadaxiseventargs.md)): 


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Deconstruct(out [Object?](https://learn.microsoft.com/dotnet/api/system.object) Sender, out [GamepadIdentifier](../gamepadidentifier.md) DeviceId, out [GamepadAxis](../gamepadaxis.md) Axis, out [Double](https://learn.microsoft.com/dotnet/api/system.double) Value, out [Double](https://learn.microsoft.com/dotnet/api/system.double) RawValue)

**Parameters:**

- `Sender` ([Object?](https://learn.microsoft.com/dotnet/api/system.object)): 

- `DeviceId` ([GamepadIdentifier](../gamepadidentifier.md)): 

- `Axis` ([GamepadAxis](../gamepadaxis.md)): 

- `Value` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 

- `RawValue` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 


---


---