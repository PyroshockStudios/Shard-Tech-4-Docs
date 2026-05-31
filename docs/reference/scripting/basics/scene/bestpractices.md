# Best Practices

Scenes are the heaviest resources, as they hold many resources, contain a lot of state information, and are the general drivers of the game. With such great power comes great responsibility, which is what this brief list of DO's and DONT's is here to guide.

## DO's

- DO: Dispose [ISceneAsset](../../modules/sdt4.managed.core/asset/isceneasset.md) as soon as you are not creating the scene again.
    - This reduces memory usage, as well as removes references from assets that may no longer be loaded in the scene, that otherwise would take up precious system resources.
- DO: Use async and await when managing scenes.
    - C# is a very asynchronous capable language, and Shard Tech 4 accomodates that by providing many features to accompany this. Use them!

## DONT's

- DONT: Omit Dispose() when finished with a scene.
    - While the C# garbage collector will eventually clear the data from memory, it may not work expectedly, and if the object is referenced anywhere, it may prevent proper dstruction.