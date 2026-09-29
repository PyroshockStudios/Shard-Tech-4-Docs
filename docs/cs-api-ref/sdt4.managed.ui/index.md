# SDT4.Managed.UI

## Namespaces

### `SDT4.Managed.UI.Rml`

| Type | Description |
| --- | --- |
| [DomTokenList](./rml/domtokenlist.md) | Represents a set of space-separated tokens corresponding to an element's <c>class</c> attribute, mirroring the JavaScript DOM <c>DOMTokenList</c> interface (<c>element.classList</c>). |
| [NamedNodeMap](./rml/namednodemap.md) | Represents a collection of an element's attributes, exposing DOM-like attribute manipulation  methods and C# `DynamicObject` member dispatch with camelCase to kebab-case conversion. |
| [RcssStyleDeclaration](./rml/rcssstyledeclaration.md) | Represents an element's inline RCSS style declarations, mirroring the DOM <c>CSSStyleDeclaration</c> interface. Supports direct property access, indexers, and dynamic PascalCase/camelCase to kebab-case resolution. |
| [RmlContext](./rml/rmlcontext.md) |  |
| [RmlDocument](./rml/rmldocument.md) | Represents the root RmlUi document window hosting a hierarchy of UI elements, styling rules, and layout contexts. |
| [RmlElement](./rml/rmlelement.md) | Represents an element in the RmlUi DOM tree, providing DOM-like manipulation,  layout inspection, styling, and event handling based on the  <a href="https://mikke89.github.io/RmlUiDoc/pages/cpp_manual/elements.html">RmlUi C++ Element API</a>. |
| [RmlEvent](./rml/rmlevent.md) |  |
| [RmlEventId](./rml/rmleventid.md) |  |
| [RmlEventListener](./rml/rmleventlistener.md) | Event listener |
| [RmlEventParameters](./rml/rmleventparameters.md) |  |
| [RmlEventPhase](./rml/rmleventphase.md) |  |
| [RmlTheme](./rml/rmltheme.md) |  |
| [RmlThemeQuery](./rml/rmlthemequery.md) |  |
| [RmlUnit](./rml/rmlunit.md) |  |
| [RmlVariant](./rml/rmlvariant.md) |  |
| [RmlVariantType](./rml/rmlvarianttype.md) |  |

### `SDT4.Managed.UI.Rml.Data`

| Type | Description |
| --- | --- |
| [IRmlData](./rml/data/irmldata.md) | Base RML data variable interface |
| [IRmlDataArray](./rml/data/irmldataarray.md) | A generic specialisation of `IRmlDataArray`1`  for untyped variables. |
| [IRmlDataArray&lt;T&gt;](./rml/data/irmldataarray`1.md) |  |
| [IRmlDataScalar](./rml/data/irmldatascalar.md) | A scalar data variable, that manages untyped variables. |
| [IRmlDataStruct](./rml/data/irmldatastruct.md) | RML data structure containing members. A class implementing this should contain members with the [`RmlDataVariableAttribute`] attribute. |
| [RmlDataModel](./rml/data/rmldatamodel.md) |  |
| [RmlDataModelToken](./rml/data/rmldatamodeltoken.md) | Initialisation token for `RmlDataModel` |

### `SDT4.Managed.UI.Rml.Data.Attributes`

| Type | Description |
| --- | --- |
| [RmlDataEventAttribute](./rml/data/attributes/rmldataeventattribute.md) |  |
| [RmlDataVariableAttribute](./rml/data/attributes/rmldatavariableattribute.md) |  |

### `SDT4.Managed.UI.Rml.Debugging`

| Type | Description |
| --- | --- |
| [RmlDebugHook](./rml/debugging/rmldebughook.md) | The class for specifying debug overlays |

