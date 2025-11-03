
# Behavior‑Driven Development (BDD) with `pytest-bdd` — Discussion Post

## Summary

Behavior‑Driven Development (BDD) is a collaborative practice that describes software behavior in plain language so developers, testers, and non‑technical stakeholders can agree on what the system should do before and during implementation. Instead of writing low‑level unit tests first, BDD captures examples of desired behavior using Gherkin (Given/When/Then). Those examples become **living documentation** and **executable tests** at the same time.

For this exercise, I reproduced the classic *cucumbers* example from Andrew Knight’s **behavior‑driven‑python** repository and ran it locally using `pytest-bdd`. The example intentionally keeps the application logic tiny so the focus stays on BDD structure and flow.

## Project Files and What Each One Does

1) **`cucumbers.py`** — Holds a simple `CucumberBasket` class that tracks how many cucumbers are in the basket and provides `add()` and `remove()` operations. Keeping logic small makes behavior easy to specify and verify.

2) **`unit_basic.feature`** — A Gherkin feature file that describes system behavior in natural language. It contains scenarios such as “add cucumbers” and “remove cucumbers,” written as steps:
   - **Given** there are `N` cucumbers
   - **When** I add or remove `K` cucumbers
   - **Then** I should have `M` cucumbers

3) **`test_unit_basic.py`** — Python step definitions that connect each English sentence in the feature file to executable code using decorators `@given`, `@when`, and `@then`. Step functions create the basket, call `add()`/`remove()`, and assert the final count.

Together, these three layers show the heart of BDD:
- Plain‑English specification in the `.feature` file
- Glue code in step definitions
- Lightweight app code under test

## How I Set It Up and Ran the Tests

I used a clean virtual environment and installed the minimum dependencies. Here are the exact commands that worked for me:

```bash
# 1) Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# 2) Install test dependencies
python -m pip install --upgrade pip
pip install pytest pytest-bdd

# 3) Bring in the three example files
#    (copy/paste from the GitHub repo into local files or download them)
#    cucumbers.py
#    unit_basic.feature
#    test_unit_basic.py

# 4) Run the tests
pytest -q
# or run the specific file:
pytest ./test_unit_basic.py -q
```

**What I observed**: Pytest collected the BDD scenarios and executed them as tests. Each scenario’s steps ran in the Given → When → Then order. The run finished with all scenarios **PASSED** in a fraction of a second, demonstrating that the behavior described in English matched the code’s actual behavior.

### A Small Path Gotcha I Solved

Some copies of `test_unit_basic.py` reference the feature file with a relative path like `../features/unit_basic.feature`. If your `unit_basic.feature` sits in the same folder as `test_unit_basic.py`, update the reference to just `"unit_basic.feature"`. After correcting the path, `pytest` collects and runs all scenarios successfully.

## How the Mapping Works (Step‑by‑Step)

- **Gherkin sentence**: “Given there are 10 cucumbers”  
  **Step function**: A `@given` function creates a `CucumberBasket(10)` and returns it as a fixture value available to later steps.

- **Gherkin sentence**: “When I eat 3 cucumbers” (or “add 3 cucumbers”)  
  **Step function**: The `@when` function calls `basket.remove(3)` or `basket.add(3)`.

- **Gherkin sentence**: “Then I should have 7 cucumbers”  
  **Step function**: The `@then` function asserts `basket.count == 7`.

This is the essence of BDD glue code: bind readable steps to concrete Python calls and final assertions.

## Why This Matters Beyond the Toy Example

1) **Shared understanding**: Gherkin makes intent explicit. Everyone can read the `.feature` file and confirm behavior before coding deep details.

2) **Living documentation**: The `.feature` file does not drift because every CI run re‑validates it. Passing scenarios mean the documented behavior still matches reality.

3) **Safer refactoring**: As implementation changes, scenarios guard behavior. Developers can refactor internals with confidence as long as Given/When/Then still pass.

4) **Scales with examples**: Scenario Outlines in Gherkin let one scenario run against many data rows without duplicate step code.

5) **Fits Pytest**: `pytest-bdd` integrates with fixtures and plugins, so you can layer in setup/teardown, parametrization, reporting, and CI easily.

## Quick Troubleshooting Notes

- **Import or path errors**: Keep `unit_basic.feature` and `test_unit_basic.py` aligned on where the feature file lives. Adjust the path passed to `@scenario(...)` or `scenarios(...)` accordingly.
- **Ambiguous steps**: If two step functions match the same text, pytest‑bdd will complain. Make step texts specific, or reuse one step function by adding multiple decorators to it.
- **State sharing**: Use Pytest fixtures to share objects like `basket` across steps in the same scenario in a clean, testable way.

## 30–60 Second Screen‑Capture Plan (what to show in the mp4)

1) Show the project folder with `cucumbers.py`, `unit_basic.feature`, and `test_unit_basic.py`.
2) Open a terminal in the folder, activate the venv, and run:
   ```bash
   pytest ./test_unit_basic.py -v
   ```
3) Let the output show green PASSED lines for each scenario.
4) End with a quick glance at `unit_basic.feature` so the viewer sees Gherkin mapping to the results.

Tip: Use QuickTime (macOS) or OBS Studio to record, 720p or 1080p, no edits needed. Keep it under 60 seconds.

## What I Learned (My Closing Thoughts)

Working through this example clarified the real value of BDD for me. I used to think BDD was only “tests written differently.” Running the cucumbers scenarios changed that. The key win is **communication**. Feature files forced me to write unambiguous behavior first, and only then connect those words to code. When scenarios passed, I felt confident I delivered the behavior stakeholders actually asked for, not my own interpretation.

I also noticed how `pytest-bdd` keeps the ceremony low. I get standard Pytest discovery, fixtures, and reporting, with just enough structure to keep scenarios readable. The step definitions are plain functions. If I need more cases, I can convert a scenario into a **Scenario Outline** and add an **Examples** table rather than duplicating steps. If I migrate to web or API tests later, I can still lean on the same Gherkin patterns, just with different fixtures and helpers.

BDDs biggest discipline is **naming** and **organization**. Feature files should describe user‑visible behavior, not technical trivia. Step texts should be stable, human‑friendly sentences. Step functions should stay light, calling into well‑factored app or helper code. This separation keeps the behavior spec readable for everyone while the Python stays maintainable for engineers.

Overall, I now see BDD as a workflow for clarity and alignment, not merely a different test syntax. The cucumbers example is small, but the habits scale: agree on behavior, codify it in Gherkin, connect it to testable code, run it continuously. That loop creates living documentation and faster, safer iteration.

## References

- behavior‑driven‑python repository (Andrew Knight) — files referenced:
  - `cucumbers.py`: https://github.com/AutomationPanda/behavior-driven-python/blob/master/cucumbers.py
  - `unit_basic.feature`: https://github.com/AutomationPanda/behavior-driven-python/blob/master/pytest-bdd/tests/features/unit_basic.feature
  - `test_unit_basic.py`: https://github.com/AutomationPanda/behavior-driven-python/blob/master/pytest-bdd/tests/step_defs/test_unit_basic.py
- Pytest‑BDD documentation: https://pytest-bdd.readthedocs.io/en/latest/
- Gherkin reference (Cucumber): https://cucumber.io/docs/gherkin/reference/
- Tutorial overview on pytest‑bdd: https://pytest-with-eric.com/bdd/pytest-bdd/

