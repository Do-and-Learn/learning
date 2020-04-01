# Example

```bash
$ behave
Feature: Showing off behave # features/example.feature:1

  Scenario: Run a simple test          # features/example.feature:3
    Given we have behave installed     # features/steps/example_steps.py:4
    When we implement 5 tests          # features/steps/example_steps.py:9
    Then behave will test them for us! # features/steps/example_steps.py:15

1 feature passed, 0 failed, 0 skipped
1 scenario passed, 0 failed, 0 skipped
3 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m0.000s
```