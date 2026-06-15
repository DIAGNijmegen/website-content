title: AI-driven self-scheduling application for ICU/MC nurses
groups: rtc, diag
closed: true
type: student
picture: vacancies/icu_schedule.jpg
template: vacancy-single
people: Laura Ros, Femke Heutink
description: Development of an artificial intelligence-based scheduling system for IC/MC nurse rostering

## Background

In the high-stakes environment of Intensive Care (IC) and Medium Care (MC) units, the roster is more than just a calendar. It is the backbone of patient safety and staff well-being. However, the current process for creating these schedules has reached a breaking point. What was once a manageable administrative task has evolved into a complex mathematical puzzle that exceeds human cognitive limits.

The difficulty lies in the sheer scale and the web of interdependencies within the IC/MC units. Every shift represents a collision of competing requirements: legal labor laws, diverse contract types, varying clinical experience levels, and personal availability. When a single piece of information—such as a late absence or a shift change—is introduced, it creates a domino effect across the whole roster. Because these variables are often submitted late or incomplete, the planning office is forced into a cycle of reactive ‘firefighting’ that results in an unstable schedule that requires constant, manual revisions.

The main problem is that manual scheduling can find a functional roster, but it rarely finds an optimal or fair one. In a unit of this size, there are trillions of ways to assign shifts. A human planner, overwhelmed by the volume of data, naturally relies on any solution that works rather than the one that is best for the team. As highlighted by Hamster [1], manual scheduling inherently leads to inequality. Without an algorithmic solution, certain units or individuals systematically shoulder a heavier burden of socially demanding shifts, such as nights and weekends. This imbalance directly erodes staff vitality, fuels frustration, and compromises the long-term sustainability of the workforce.

To move beyond these manual limitations, this project proposes the development of an artificial intelligence-based (AI) scheduling system. The goal is to create a model capable of processing the many interdependencies, while balancing the institutional needs with individual preferences. It has already been demonstrated by Hamster [1] that automated scheduling has potential, and this has been recognized by nurses as well [2].

The transition to an automated, algorithmic approach is not merely a matter of convenience. It’s necessary to ensure a fair, predictable, and future-proof workplace for those providing critical care.

## Approach

The primary goal is to develop an AI model that generates fair, predictable, and sustainable rosters while accounting for staff preferences and staffing requirements.

Key research questions include:

- To what extent can an AI model combine individual preferences with staffing requirements without violating hard constraints (e.g., labor laws)?
- Which optimization techniques provide the best balance between fair distribution and overall schedule quality?
- How do nurses perceive the fairness and workload of AI-generated schedules compared to manual methods?
- Is the developed model technically scalable and reproducible for other medical departments?

## Data

This research will utilize one or more years of anonymized scheduling data from the Radboudumc IC/MC units to develop and validate a scheduling model. The technical framework begins with the formalization of constraints, the distinction between hard constraints (e.g., working hours act and mandatory staffing ratios) and soft constraints (e.g., individual preferences). An overview of the input variables and hard- and soft constraints will be available for the student.

## References

[1] Hamster, M. (2025). The Rhythm of the Roster. Master thesis, University of Twente. Available at: https://purl.utwente.nl/essays/108598

[2] Gerlach, M., Renggli, F. J., Bieri, J. S., Sariyar, M., & Golz, C. (2025). Exploring nurse perspectives on AI-based shift scheduling for fairness, transparency, and work-life balance. *BMC Nursing*, 24(1), 1161.

## Requirements

- Knowledge of ML-based optimization algorithms and/or mathematical modeling
- Programming experience with Python and popular data science libraries (e.g., pandas)
- Interest in healthcare logistics and operational management

## Information

**Project duration:** 6 months  
**Location:** Radboud University Medical Center

The student will be embedded within the ICU/MC department. A secure Digital Research Environment (DRE) and standard computing facilities are available for data analysis.

If you are interested in applying for this Master student project, please send an email to: rtcai@radboudumc.nl
