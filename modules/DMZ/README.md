# DMZ Overview
The DMZ stores shared scripts and classes. If something is exclusively used by the hub or workers, it might need to be in there.

### Submodules
- data_kit:
  - This submodule should handle data manipulation, cleaning, and prepping for the machine learning framework.
- models:
  - This submodule holds the machine learning algorithms this framework is using, along with the classes that are used to select the appropriate model.

### Classes
- ticket:
  - A ticket should contain everything that is required for the completion of a task by a worker. The goal is to keep the number of required items as low as possible to decrease bloat.

This documentation is a work in progress, if you see something that should be here, please tell us.
