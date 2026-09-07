# DeviceConnectionEventArgs

## Summary
Provides data for gamepad hardware lifecycle changes, such as connection or disconnection.



## Definition

**Namespace:** `SDT4.Managed.Input.Gamepad.Events`  
**Assembly:** `SDT4.Managed.Input.dll`

```csharp
struct DeviceConnectionEventArgs
```
**Implements:**

##### [IEquatable&lt;DeviceConnectionEventArgs&gt;](https://learn.microsoft.com/dotnet/api/system.iequatable-1)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public get; set; Sender` | [Object?](https://learn.microsoft.com/dotnet/api/system.object) | The source object that dispatched the event, or <see langword="null" />. |
| `public get; set; DeviceId` | [GamepadIdentifier](../gamepadidentifier.md) | The identifier assigned to the gamepad device. |
| `public get; set; DeviceGuid` | [Guid](https://learn.microsoft.com/dotnet/api/system.guid) | The persistent hardware GUID identifying the physical device across reconnections. |
| `public get; set; DeviceName` | [String](https://learn.microsoft.com/dotnet/api/system.string) | The human-readable product or driver name of the device. |
| `public get; set; IsConnected` | [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) | <see langword="true" /> if the device was connected or reconnected; <see langword="false" /> if it was disconnected. |



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
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([DeviceConnectionEventArgs](./deviceconnectioneventargs.md) other)

**Parameters:**

- `other` ([DeviceConnectionEventArgs](./deviceconnectioneventargs.md)): 


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Deconstruct(out [Object?](https://learn.microsoft.com/dotnet/api/system.object) Sender, out [GamepadIdentifier](../gamepadidentifier.md) DeviceId, out [Guid](https://learn.microsoft.com/dotnet/api/system.guid) DeviceGuid, out [String](https://learn.microsoft.com/dotnet/api/system.string) DeviceName, out [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) IsConnected)

**Parameters:**

- `Sender` ([Object?](https://learn.microsoft.com/dotnet/api/system.object)): 

- `DeviceId` ([GamepadIdentifier](../gamepadidentifier.md)): 

- `DeviceGuid` ([Guid](https://learn.microsoft.com/dotnet/api/system.guid)): 

- `DeviceName` ([String](https://learn.microsoft.com/dotnet/api/system.string)): 

- `IsConnected` ([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)): 


---


---