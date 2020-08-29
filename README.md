# BPI Challenge 2020

The purpose of this repository is to maintain code and text produced to analyze this year's BPI Challenge: https://icpmconference.org/2020/bpi-challenge/

## Repository Contents
 * Cleaned versions of the event logs (see the [data folder](data/cleaned_logs))
 * A [class diagram](data-model/Classdiagram.png) showing attributes and relations of the logs
 * [Jupyter Notebooks](notebook) we used for analyzing the logs. [Below](#notebooks) you will find a brief overview of the included notebooks and their purposes.


### Notebooks 📓
> ℹ️ *Please note that you need to have [PM4Py](https://pm4py.fit.fraunhofer.de/install) installed in order to be able to execute the notebooks by yourself. However, the notebooks contained in this repository already include the respective results, just click on any notebook name in the table below.*

| Topic           | Notebook                   | Description |
|-----------------|----------------------------|-------------|
| **General**      | [Log Coverage](notebook/Log%20Coverage.ipynb)               | *Analyze the sparseness of case and event attributes.*            |
|                 | [Permit Log](notebook/Permit%20Log%20-%20Multiple%20Declarations.ipynb) / [Merge Logs](notebook/Merge%20Logs.ipynb)    | *Analyze relations between Permit log, International Declarations log, and Prepaid Travel Cost log.*            |
|                 | [Statistical Insights](notebook/Statistical%20Insights.ipynb)       | *Provide high-level insights into the distribution of selected attributes across the event logs.*            |
|                 |                            |             |
| **Performance** | [Bottleneck Analysis](notebook/Bottleneck%20Analysis.ipynb)        | *Identify and analyze systemic constraints of the process.* |
|                 | [Dotted Chart Analysis](notebook/Dotted%20Chart%20Analysis.ipynb)      | *Application of dotted charts to uncover batch-processing.*            |
|                 | [Root Cause Analysis](notebook/Root%20Cause%20Analysis.ipynb)        | *Identify and explain root causes for temporal anomalies in the event logs.* |
|                 |                            |             |
| **Operation**   | [Clusters_ID](notebook/Clusters_ID.ipynb) / [Clusters_PTC](notebook/Clusters_PTC.ipynb) | *Analyze potential differences between projects and organizations for international declarations and prepaid travel costs.*            |
|                 | [Declarations Analysis](notebook/Declarations%20Analysis.ipynb)      |  *Analyzes the number of (re)submissions in the international and domestic declarations logs.*           |
|                 | [Rejection Rate](notebook/Rejection%20rate.ipynb)             | *Analyze the number of rejected declarations in each step of the process.* |
|                 | [Travel Times](notebook/TravelTimes.ipynb)               | *Analyzes the trips and expenses recorded in the Permit log.*            |
|                 |                            |             |
| **Compliance**  | [Double Payments](notebook/Double%20Payments.ipynb)            | *Investigate potential double payments and their financial impact.* |
|                 |                            |             |

