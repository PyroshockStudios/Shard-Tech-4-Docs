# SDT4.Managed.Input

## Namespaces

### `SDT4.Managed.Input`

| Type | Description |
| --- | --- |
| [WindowExtensions](./windowextensions.md) |  |

### `SDT4.Managed.Input.Custom`

| Type | Description |
| --- | --- |
| [IRawInputSource](./custom/irawinputsource.md) |  |
| [RawInputCommands](./custom/rawinputcommands.md) | Represents dispatch delegates provided to custom input devices, allowing raw drivers  to inject button and axis events directly into the engine's central input pipeline. |
| [RawInputIngestion](./custom/rawinputingestion.md) |  |

### `SDT4.Managed.Input.Custom.Events`

| Type | Description |
| --- | --- |
| [CustomAxisInputEventArgs](./custom/events/customaxisinputeventargs.md) | Provides event data for continuous analogue, rotational, or positional inputs originating from custom input devices. |
| [CustomButtonInputEventArgs](./custom/events/custombuttoninputeventargs.md) | Provides event data for digital button or binary state changes originating from custom input devices. |

### `SDT4.Managed.Input.Desktop`

| Type | Description |
| --- | --- |
| [InputModifiers](./desktop/inputmodifiers.md) |  |
| [KeyCode](./desktop/keycode.md) |  |
| [MouseButton](./desktop/mousebutton.md) |  |
| [MouseMotionInput](./desktop/mousemotioninput.md) |  |
| [WindowInput](./desktop/windowinput.md) | Provides window-specific and static global input handling for desktop platforms, including event-based callbacks and polling mechanisms for keyboard, mouse, and window state changes. |

### `SDT4.Managed.Input.Desktop.Events`

| Type | Description |
| --- | --- |
| [CharInputEventArgs](./desktop/events/charinputeventargs.md) | Provides data for text input events containing a decoded Unicode character. |
| [KeyEventArgs](./desktop/events/keyeventargs.md) | Provides data for keyboard press, release, and repeat events. |
| [MouseButtonEventArgs](./desktop/events/mousebuttoneventargs.md) | Provides data for mouse button press and release events. |
| [MouseMoveEventArgs](./desktop/events/mousemoveeventargs.md) | Provides data for mouse motion events, including absolute coordinates and frame-to-frame movement delta. |
| [MouseScrollEventArgs](./desktop/events/mousescrolleventargs.md) | Provides data for mouse wheel or touchpad scrolling events. |
| [WindowCloseEventArgs](./desktop/events/windowcloseeventargs.md) | Provides data for events fired when the window gets closed. |
| [WindowCursorEnterEventArgs](./desktop/events/windowcursorentereventargs.md) | Provides data for events fired when the mouse cursor enters or leaves the window client area. |
| [WindowDropEventArgs](./desktop/events/windowdropeventargs.md) | Provides data for external drag-and-drop operations onto a window surface. |
| [WindowFocusChangeEventArgs](./desktop/events/windowfocuschangeeventargs.md) | Provides data for window input focus gain or loss events. |
| [WindowMoveEventArgs](./desktop/events/windowmoveeventargs.md) | Provides data for events fired when the window moves. |
| [WindowResizeEventArgs](./desktop/events/windowresizeeventargs.md) | Provides data for events fired when the window gets resized. |

### `SDT4.Managed.Input.Gamepad`

| Type | Description |
| --- | --- |
| [GamepadAxis](./gamepad/gamepadaxis.md) |  |
| [GamepadButton](./gamepad/gamepadbutton.md) |  |
| [GamepadDevice](./gamepad/gamepaddevice.md) | Manages connected physical and virtual gamepad hardware registries, lifecycle state,  and connection notifications. |
| [GamepadIdentifier](./gamepad/gamepadidentifier.md) |  |
| [GamepadInput](./gamepad/gamepadinput.md) | Provides polling access, configuration settings, and event-driven dispatching  for gamepad buttons and analogue axes across connected devices. |

### `SDT4.Managed.Input.Gamepad.Events`

| Type | Description |
| --- | --- |
| [DeviceConnectionEventArgs](./gamepad/events/deviceconnectioneventargs.md) | Provides data for gamepad hardware lifecycle changes, such as connection or disconnection. |
| [GamepadAxisEventArgs](./gamepad/events/gamepadaxiseventargs.md) | Provides data for gamepad analog axis movement events, supplying both calibrated and raw values. |
| [GamepadButtonEventArgs](./gamepad/events/gamepadbuttoneventargs.md) | Provides data for gamepad button press, release, and emulated repeat events. |

### `SDT4.Managed.Input.Mapper`

| Type | Description |
| --- | --- |
| [IInputReceiver](./mapper/iinputreceiver.md) |  |
| [InputMapper](./mapper/inputmapper.md) |  |

### `SDT4.Managed.Input.Mapper.Attributes`

| Type | Description |
| --- | --- |
| [ActionAttribute](./mapper/attributes/actionattribute.md) | To be used on an <em>enum</em> member. Marks input to be handled as a boolean <strong>button</strong> |
| [ActionInputAttribute](./mapper/attributes/actioninputattribute.md) | Specifies that this field/method/property is an action that maps to an <em>enum</em> with the `InputMapAttribute` attribute. |
| [InputMapAttribute](./mapper/attributes/inputmapattribute.md) | Specifies that an <em>enum</em> is to be used for creating input maps. |
| [RangeAttribute](./mapper/attributes/rangeattribute.md) | To be used on an <em>enum</em> member. Marks input to be handled as a floating <strong>range</strong> |
| [RangeInputAttribute](./mapper/attributes/rangeinputattribute.md) | Specifies that this field/method/property is a range that maps to an <em>enum</em> with the `InputMapAttribute` attribute. |

