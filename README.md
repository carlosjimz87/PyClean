CLEAN CODE IN PYTHON

1. DRY: Dont Repeat Yourself

   - Use decorators (add some decoration to original functions and create new functions that explain better the action they perform)

2. Dont mix logic and implementation details.

   - Use properties (avoiding custom getter and setters).
   - Use magic methods (pythonic)

3. Dont leave resources unavailable or exposed to memory leaked.

   - Use context managers.

4. Don't write unnatended code.

   - Use Python Code Standards (PEP8). Define guidelines in the project and autocheck as part of CI.
   - Use Docstrings (PEP257) / Function Annotations (PEP3107)
   - Use pycodestyle, flake8, pylint, radon or coala.

5. Don't write untested code.
   - Make unit tests for every module and functionality.
   - Use pytest, noseo or unittest.

6. Replace traditional index manipulation with core loopings idioms.

7. Replace traditional index manipulation with core loopings idioms.
