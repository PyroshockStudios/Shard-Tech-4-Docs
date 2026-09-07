# GamepadDevice

## Summary
Manages connected physical and virtual gamepad hardware registries, lifecycle state, 
and connection notifications.

## Remarks
!!! danger
    All calls made within this class <strong>MUST</strong> be performed on the Master Thread. 
    See `RunLater` on how to safely call this from an asynchronous thread.
    Failure to comply with this can cause catastrophical failures as the engine is not designed for this.

## Definition

**Namespace:** `SDT4.Managed.Input.Gamepad`  
**Assembly:** `SDT4.Managed.Input.dll`

```csharp
static class GamepadDevice
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔  **GamepadDevice**
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

#### public static [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) IsDeviceConnected([GamepadIdentifier](./gamepadidentifier.md) deviceId)


**Summary:**
Checks whether the gamepad identified by `deviceId` is currently connected and active.

**Parameters:**

- `deviceId` ([GamepadIdentifier](./gamepadidentifier.md)): The identifier representing the target gamepad device.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if the device is connected; otherwise, <see langword="false" />.

---


---