1. Continuous Bag of Words (CBOW)
2. Skip-gram



[**The**, Earth, travels]

[The, **Earth**, travels, around]

[The, Earth, **travels**, around, the]

[Earth, travels, **around**, the, Sun]

[travels, around, **the**, Sun, once]

[around, the, **Sun**, once, per]

[the, Sun, **once**, per, year]

[Sun, once, **per**, year]

[once, per, **year**]

## Continuous Bag of Words (CBOW)

| Input                   | Output  |
| :-                      | :-      |
| Earth, travels          | The     |
| The, travels, around    | Earth   |
| The, Earth, around, the | travels |

## skip-gram

| Input                   | Output  |
| :-                      | :-      |
| **The**, Earth          | true    |
| **The**, travels        | true    |
| **Earth**, The          | true    |
| **Earth**, travels      | true    |
| **Earth**, zebra        | false   |
