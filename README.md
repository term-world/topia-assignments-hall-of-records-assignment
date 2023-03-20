
| Date              |          |
|:------------------|:---------|
| `todo` | Assigned |
| `todo`| Due      |
| Status            | [![GatorGrader](../../actions/workflows/main.yml/badge.svg)](../../actions/workflows/main.yml) |

# DATA DONE, MAYOR DECREES DECISIVE DEED: CITIZENS TO COMPUTE REPRESENTATIVE RESIDENT CRITERIA

**Reported by `Official Mayor-Endorsed News` on `todo`**g

Maintaining a healthy community is _everyone's job_ and so is neighborhood surveillance! As the Mayor 
described to O.M.E.N. (Offical Mayor Endorsed News), "I, your Mayor, look to you, the great citizens
of `term-world` to help define the ideal citizen contributors. To you, people of this fair city, I (your Mayor) ask for the profile of the most resilient, representative residents!"

As O.M.E.N. has learned, this means trawling through much of the data kept at the newly-restored city `datamart` to uncover the statistics describing the very demonstrative denizens which detail the ideal community member. This data digs deep. Using words that O.M.E.N. was told to say, it covers all of the behaviors that a mindful member of `term-world` must aspire to. "We've been collecting data on you, our citizens, this whole time!" the Mayor reiterated.

Will you, great residents of `term-world` help define the future of this digital world? The Mayor certainly hopes so, saying "[y]our Mayor--of course, that's me--depends on you to compile every last criterion toward identifying the luminaries of our land!" To those who meet the basic benchmarks go all the spoils! Just exactly what those spoils are, the Mayor's Office declines to say.

## Overview

In this set of activities we cover:

* `dictionary` data structures
* a review of `list`s and `iteration` (`for`/`while` loops)
* revisiting `functions`
* exploring more basic data science

You'll complete one main task, supported by three sub-tasks:

* An average of all columns of the data (main task), using
  * a `function` that returns rows matching a minimum value in a given column (sub-task)
  * a `function` that totals the numeric values of a given column (sub-task)
  * a report of the average of a given column (sub-task)

As with `datamart`, there are plenty of opportunities for improvements to how you find various statistics about the data. Keep an open mind and a keen eye to the particularly annoying inconveniences of the `Processor` program.

### Previous Learning Objectives

If you wish to review previous learning objectives from our assignments, you can visit the [`Syllabus`](https://chompe.rs/100-syllabus) for helpful information. However, it's also important to make an effort to retain what we have covered thus far as we progress through the course sections of the Readme might be taken out.

## Completing `hall-of-records` content

The `hall-of-records` has just one file: `Processor.py`. Functionality of the `Processor` has largely been completed for you. The work left up to you is to write the `function`s required to produce the statistical report requested in the `reflection.md`.

This program uses one `global` variable to house the data in the table and the names of columns. Use:

|Variable |Purpose |
|:--------|:-------|
|DATA†     |Holds columns and data from table |

`†` This is a departure from the last assignment; see what conveniences `dictionary`s provide you!

### `main.py`

Leverges the `main` function to:

* Work out options for the Processor's main menu
* Provides _at least_ two `function`s outlined in the `task`/`subtask` breakdown above


|Function name |Parameters  |Return type | Description                                               |
|:-------------|:-----------|:-----------|:----------------------------------------------------------|
|search_rows        |Field to search (`str`), term/number to search (`any`)       |`list`      |Returns _all_ rows which are greater than or equal to a given search criteria |
|total_column       |Field to total (`str`)             |`int`       |Returns the total of all numeric data in a given column |

Your [reflection](office/reflection.md) or [editorial](office/editorial.md) should report the outcomes of these operations.

### Writing

Choose one of the following.

#### Reflection

All of the above tasks completed, finish the reflection located in the `office` folder.

#### Protesting

You may protest completing this assignment by writing an `editorial.md` in the `office` _instead_ of a `reflection.md`. Doing so _does not mean_ not completing the code for this assignment. Rather, it indicates that you should compose an evidence-based argument that uses your analysis to persuade your fellow citizens to your cause.

## Improvement Suggestions

Here are some suggestions for improvements you can, **but are not limited to** use:

|Improvement Suggestions |Description        |
|:--------------------|:------------------|
|Dictionaries         | Add function to edit data |
|Dictionaries         | Add function to find the average of all columns (auto-averager) |    
|Dictionaries         | Dictionaries	Find most common entry in a column                |
|Dictionaries         |	Sort a column (least to greatest, greatest to least)            |
|Dictionaries         | Ability to update multiple cells with a formula                 |
|Dictionaries         |	Add a function to calculate any single other statistical value (median, standard deviation, mode, etc.) |
|Dictionaries         | Write the results of a given operation (average, standard deviation) _as a new column_ |
|Conditional logic    |	Color-code data presentation (uses the `rich` module) |
|Data analytics       | Create a data plot using the `seaborn` module |
|Files, JSON          | Overwrite data (i.e. save the table)          |

**Make sure to link your issue with the pull request you used to make your improvement.**

**If you are not following an improvement suggestion you need to have your improvement suggestion checked by the professor before proceeding.**

## Backup Policy Reminder

**While we may use this server to store code, you are responsible for using GitHub as your main backup.**

In the event that the `term-world` server goes down for any unforeseen reason, your work may be lost. Though this server is backed up on a regular (i.e. weekly) basis, there is no guarantee that up-to-the-minute data for your work will be restored.

Remember: to err is human; to back up your work is *divine*.
