# Maqarr Go failure/recovery acceptance sample

Disposable public fixture for the independent test environment.
Version: build-fail. Structural CI intentionally passes for both commits.
The build-fail version has one deliberate undefined Go symbol; recovery removes it.
Actual compilation, preserved healthy release and recovery are verified by Maqarr.
