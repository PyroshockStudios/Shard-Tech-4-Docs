# Project Compilation
Games made in Shard Tech 4 have their compiler managed by the engine, meaning that 

# Visual Studio and Other IDEs

# Custom .NET Analysis Tools
Shard Tech 4 extends the .NET ecosystem by inserting custom code analysis, most notably to:

- Validate attribute usage
- Automatic code expansion
- Improved error messages

This means that the .NET project is entirely managed by the engine to ensure all the steps of the process are fully coherent.

# .NET SDK

The compiler used by Shard Tech 4 is the MSBuild that is included in your .NET SDK installation, and launches the *dotnet* process to perform script compilation.

!!! warning
    Sometimes .NET may hang and cause the engine to get stuck when booting. If boot times are prolongued and nothing happens, check with your system process manager if there are linguering .NET processes, and terminate them before restarting Shard Tech 4.