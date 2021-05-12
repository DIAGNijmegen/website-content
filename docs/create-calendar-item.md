# Create a new calendar item

Calendar items can be added by creating a new `.md` file in the `calendar` directory. Each calendar item should have the following items:

1. The date of the event.
2. The `title:` tag with empty content (the content is not used, but is required by Pelican to be present).
3. The `groups` tag to determine which websites needs to include this event.
4. The `content_after` tag to determine the text that has to be shown after the event date.
5. The `content_before` tag to determine the text that has to be shown before the event date.

An example:

```
date: 2020-10-18
title:
groups: diag
content_after: Midas Meijs has succesfully defended his PhD thesis with the title 'Automated Image Analysis and Machine Learning to Detect Cerebral Vascular Pathology in 4D-CTA'.
content_before: Midas Meijs will defend his PhD thesis titled 'Automated Image Analysis and Machine Learning to Detect Cerebral Vascular Pathology in 4D-CTA'. The Date has been postponed because of the COVID-19 outbreak.
```